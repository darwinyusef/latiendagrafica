# Comandos para correr el proyecto

## Desarrollo local

### 1. Activar entorno e instalar dependencias (solo la primera vez)

```powershell
cd G:\websitee\backend
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. Correr el backend

```powershell
cd G:\websitee\backend
.\venv\Scripts\Activate.ps1
python app.py
```

Backend disponible en: `http://127.0.0.1:5000`

Verificar que corre: `http://127.0.0.1:5000/health` → debe devolver `{"status": "ok"}`

### 3. Correr el frontend

Abrir `index.html` con **Live Server** en VS Code (clic derecho → *Open with Live Server*).

Frontend disponible en: `http://127.0.0.1:5500`

---

## Producción (Docker)

```powershell
cd G:\websitee
docker-compose up --build
```

Sitio completo en: `http://localhost`

Para detener:

```powershell
docker-compose down
```

---

## Endpoints del API

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/health` | Estado del servidor |
| GET | `/api/servicios` | Lista de servicios |
| GET | `/api/catalogo` | Catálogo (param: `?categoria=`) |
| GET | `/api/portafolio` | Portafolio (param: `?categoria=`) |
| POST | `/api/cotizacion` | Enviar cotización |
| PUT | `/api/<tipo>/<id>/imagen` | Actualizar imagen |
