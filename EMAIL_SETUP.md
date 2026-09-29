# Guía de Integración de Correo Electrónico

Sistema de envío automático de cotizaciones para **La Tienda Gráfica**.  
Cuando un cliente envía el formulario, se emiten dos correos: confirmación al cliente y notificación interna al negocio.

---

## Requisitos

- Cuenta Gmail con **verificación en 2 pasos activa**
- Docker y Docker Compose instalados
- Archivo `.env` creado en la raíz del proyecto

---

## 1. Generar App Password en Gmail

> Las App Passwords son contraseñas de 16 caracteres que Google genera para aplicaciones externas. **No uses tu contraseña normal de Gmail.**

### Paso a paso

1. Abre [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
2. Inicia sesión con la cuenta que recibirá las cotizaciones
3. En el campo **"Nombre de la aplicación"** escribe `La Tienda Grafica`
4. Haz clic en **Crear**
5. Google muestra una clave de 16 caracteres — **cópiala de inmediato**, no vuelve a mostrarse

```
Ejemplo: abcd efgh ijkl mnop
```

> Si no ves la opción, primero activa la verificación en 2 pasos:  
> Cuenta Google → Seguridad → Verificación en 2 pasos

---

## 2. Configurar el archivo `.env`

Crea el archivo `.env` en la raíz del proyecto (junto a `docker-compose.yml`):

```bash
cp .env.example .env
```

Luego edítalo con tus datos reales:

```env
# Servidor SMTP
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=tucorreo@gmail.com
SMTP_PASS=abcdefghijklmnop

# Negocio
BUSINESS_EMAIL=tucorreo@gmail.com
BUSINESS_NAME=La Tienda Gráfica
SITE_URL=https://tudominio.com
WA_NUMBER=573001234567
```

| Variable | Descripción |
|---|---|
| `SMTP_USER` | Tu correo Gmail completo |
| `SMTP_PASS` | App Password de 16 caracteres (sin espacios) |
| `BUSINESS_EMAIL` | Correo donde llegarán las notificaciones de cotización |
| `BUSINESS_NAME` | Nombre que aparece en los correos enviados |
| `SITE_URL` | URL pública del sitio (aparece en el pie del correo) |
| `WA_NUMBER` | Número de WhatsApp con código de país, sin `+` ni espacios |

---

## 3. Levantar el proyecto con Docker

```bash
# Construir y levantar todos los servicios
docker compose up -d

# Ver que los contenedores están corriendo
docker compose ps
```

Deberías ver dos servicios activos:

```
NAME        STATUS          PORTS
backend     running         5000/tcp
web         running         0.0.0.0:80->80/tcp
```

---

## 4. Verificar que el correo funciona

Prueba el endpoint directamente desde la terminal:

```bash
curl -X POST http://localhost/api/cotizacion \
  -H "Content-Type: application/json" \
  -d '{
    "nombre":      "Juan Prueba",
    "email":       "tucorreo@gmail.com",
    "servicio":    "DTF — Estampado Textil",
    "cantidad":    "50 camisetas",
    "descripcion": "Prueba del sistema de correo"
  }'
```

**Respuesta esperada:**

```json
{ "ok": true, "message": "¡Cotización enviada! Revisa tu correo." }
```

Deberías recibir dos correos en `tucorreo@gmail.com`:
- Uno como **cliente** (confirmación con resumen)
- Uno como **negocio** (ficha interna con botones de respuesta)

---

## 5. Qué ocurre en cada envío

```
Cliente envía formulario
        │
        ▼
POST /api/cotizacion  (JSON)
        │
        ▼
Flask valida campos requeridos
(nombre, email, servicio, descripcion)
        │
        ▼
email_service.py renderiza plantillas Jinja2
        │
        ├─► email_cliente.html  →  correo de confirmación al cliente
        │       • Resumen de la solicitud
        │       • Botón WhatsApp para contacto rápido
        │
        └─► email_negocio.html  →  notificación interna al negocio
                • Todos los datos del cliente
                • Botón "Responder por Email"
                • Botón "WhatsApp" (si dejó teléfono)
```

Si el servidor no responde, el formulario hace **fallback automático a WhatsApp** para no perder la cotización.

---

## 6. Ver logs en tiempo real

```bash
# Logs del backend (Flask)
docker compose logs -f backend

# Logs de Nginx
docker compose logs -f web

# Todos los logs
docker compose logs -f
```

Una cotización exitosa genera estas líneas en el backend:

```
INFO  POST /api/cotizacion 200
INFO  Cotización enviada para Juan Prueba <cliente@email.com>
```

---

## 7. Solución de problemas frecuentes

### `535 Username and Password not accepted`
Estás usando tu contraseña normal de Gmail. Genera una **App Password**.

### `App passwords not available`
No tienes verificación en 2 pasos activa.  
Ve a: Cuenta Google → Seguridad → Verificación en 2 pasos → Activar.

### `Connection refused` o timeout
El puerto 587 puede estar bloqueado por tu proveedor de hosting.  
Cambia en `.env`:
```env
SMTP_PORT=465
```
Y en `email_service.py` cambia `starttls()` por SSL:
```python
conn = smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, timeout=15)
conn.login(SMTP_USER, SMTP_PASS)
```

### El correo llega a spam
Agrega un registro **SPF** en el DNS de tu dominio:
```
TXT  @  v=spf1 include:_spf.google.com ~all
```

### Cambié variables en `.env` y no aplican
Las variables se cargan al iniciar el contenedor. Reinicia el backend:
```bash
docker compose restart backend
```

---

## 8. Usar otro proveedor SMTP (opcional)

El sistema es compatible con cualquier servidor SMTP. Solo cambia las variables:

**Outlook / Hotmail**
```env
SMTP_HOST=smtp.office365.com
SMTP_PORT=587
```

**Brevo (antes Sendinblue) — recomendado para producción**
```env
SMTP_HOST=smtp-relay.brevo.com
SMTP_PORT=587
SMTP_USER=tucorreo@tudominio.com
SMTP_PASS=xsmtpsib-xxxxxxxx   # API key de Brevo
```

**Amazon SES**
```env
SMTP_HOST=email-smtp.us-east-1.amazonaws.com
SMTP_PORT=587
SMTP_USER=AKIAIOSFODNN7EXAMPLE
SMTP_PASS=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

> Para producción con alto volumen se recomienda **Brevo** o **Amazon SES** en lugar de Gmail, que tiene límite de 500 correos/día.

---

## Estructura de archivos relevantes

```
websitee/
├── .env                          ← credenciales (nunca subir a git)
├── .env.example                  ← plantilla sin datos sensibles
├── docker-compose.yml            ← orquestación de servicios
├── Dockerfile                    ← imagen del backend Python
├── nginx.conf                    ← proxy + archivos estáticos
├── cotizacion.html               ← formulario (envía a /api/cotizacion)
└── backend/
    ├── app.py                    ← rutas Flask
    ├── email_service.py          ← lógica SMTP + Jinja2
    └── templates/
        ├── email_cliente.html    ← correo de confirmación
        └── email_negocio.html    ← notificación interna
```

---

## Seguridad — importante

Agrega `.env` a tu `.gitignore` para no exponer credenciales:

```bash
echo ".env" >> .gitignore
```

Nunca subas el archivo `.env` real a GitHub o cualquier repositorio público.
