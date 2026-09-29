import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from jinja2 import Environment, FileSystemLoader, select_autoescape

# ── Configuración SMTP ──────────────────────────────────────────────────────
SMTP_HOST     = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT     = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER     = os.getenv("SMTP_USER", "")
SMTP_PASS     = os.getenv("SMTP_PASS", "")
BUSINESS_EMAIL = os.getenv("BUSINESS_EMAIL", SMTP_USER)
BUSINESS_NAME  = os.getenv("BUSINESS_NAME", "La Tienda Gráfica")
SITE_URL       = os.getenv("SITE_URL", "https://latiengrafica.com")
WA_NUMBER      = os.getenv("WA_NUMBER", "573001234567")

# ── Motor de plantillas ─────────────────────────────────────────────────────
_TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")
_jinja = Environment(
    loader=FileSystemLoader(_TEMPLATES_DIR),
    autoescape=select_autoescape(["html"]),
)


def _render(template_name: str, ctx: dict) -> str:
    return _jinja.get_template(template_name).render(**ctx)


def _smtp_connection():
    conn = smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=15)
    conn.ehlo()
    conn.starttls()
    conn.login(SMTP_USER, SMTP_PASS)
    return conn


def _build_message(from_addr: str, to_addr: str, subject: str, html_body: str) -> MIMEMultipart:
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"]    = f"{BUSINESS_NAME} <{from_addr}>"
    msg["To"]      = to_addr
    msg.attach(MIMEText(html_body, "html", "utf-8"))
    return msg


def send_cotizacion_emails(data: dict) -> None:
    """Envía dos correos: confirmación al cliente y notificación al negocio."""
    if not SMTP_USER or not SMTP_PASS:
        raise EnvironmentError("Credenciales SMTP no configuradas (SMTP_USER / SMTP_PASS).")

    ctx = {
        "nombre":       data.get("nombre", ""),
        "empresa":      data.get("empresa", ""),
        "email":        data.get("email", ""),
        "telefono":     data.get("telefono", ""),
        "servicio":     data.get("servicio", ""),
        "cantidad":     data.get("cantidad", ""),
        "descripcion":  data.get("descripcion", ""),
        "fecha":        datetime.now().strftime("%d/%m/%Y %H:%M"),
        "business_name": BUSINESS_NAME,
        "site_url":     SITE_URL,
        "wa_number":    WA_NUMBER,
    }

    html_cliente = _render("email_cliente.html", ctx)
    html_negocio = _render("email_negocio.html", ctx)

    msg_cliente = _build_message(
        SMTP_USER,
        ctx["email"],
        f"✅ Recibimos tu cotización — {BUSINESS_NAME}",
        html_cliente,
    )
    msg_negocio = _build_message(
        SMTP_USER,
        BUSINESS_EMAIL,
        f"🖨️ Nueva cotización de {ctx['nombre']} — {ctx['servicio']}",
        html_negocio,
    )
    # Reply-To del negocio apunta al cliente para responder rápido
    msg_negocio["Reply-To"] = ctx["email"]

    with _smtp_connection() as conn:
        conn.sendmail(SMTP_USER, ctx["email"],    msg_cliente.as_string())
        conn.sendmail(SMTP_USER, BUSINESS_EMAIL,  msg_negocio.as_string())
