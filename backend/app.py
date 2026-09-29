import os
import copy
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from email_service import send_cotizacion_emails
from data import SERVICIOS, CATALOGO, PORTAFOLIO

load_dotenv()

app = Flask(__name__)
CORS(app)
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

# Mutable in-memory stores (imagen se puede actualizar sin reiniciar)
_servicios  = copy.deepcopy(SERVICIOS)
_catalogo   = copy.deepcopy(CATALOGO)
_portafolio = copy.deepcopy(PORTAFOLIO)

_STORES = {"servicios": _servicios, "catalogo": _catalogo, "portafolio": _portafolio}


@app.route("/api/cotizacion", methods=["POST"])
def cotizacion():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"ok": False, "message": "Cuerpo JSON inválido"}), 400

    required = ["nombre", "email", "servicio", "descripcion"]
    missing = [f for f in required if not data.get(f, "").strip()]
    if missing:
        return jsonify({"ok": False, "message": f"Campos requeridos: {', '.join(missing)}"}), 422

    try:
        send_cotizacion_emails(data)
        app.logger.info("Cotización enviada para %s <%s>", data["nombre"], data["email"])
        return jsonify({"ok": True, "message": "¡Cotización enviada! Revisa tu correo."})
    except Exception as exc:
        app.logger.error("Error enviando correo: %s", exc)
        return jsonify({"ok": False, "message": "No se pudo enviar el correo. Intenta de nuevo."}), 500


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


# ── Datos ──────────────────────────────────────────────────────────────────────

@app.route("/api/servicios", methods=["GET"])
def get_servicios():
    return jsonify(_servicios)


@app.route("/api/catalogo", methods=["GET"])
def get_catalogo():
    cat = request.args.get("categoria", "").strip()
    if cat and cat != "todos":
        return jsonify([p for p in _catalogo if p["categoria"] == cat])
    return jsonify(_catalogo)


@app.route("/api/portafolio", methods=["GET"])
def get_portafolio():
    cat = request.args.get("categoria", "").strip()
    if cat and cat != "todos":
        return jsonify([p for p in _portafolio if p["categoria"] == cat])
    return jsonify(_portafolio)


# ── Actualizar imagen ─────────────────────────────────────────────────────────

@app.route("/api/<string:tipo>/<string:item_id>/imagen", methods=["PUT"])
def update_imagen(tipo, item_id):
    store = _STORES.get(tipo)
    if store is None:
        return jsonify({"ok": False, "message": "Tipo inválido. Usa: servicios, catalogo, portafolio"}), 404

    body = request.get_json(silent=True) or {}
    imagen_url = body.get("imagen")  # None limpia la imagen y vuelve al icono

    item = next((x for x in store if x["id"] == item_id), None)
    if item is None:
        return jsonify({"ok": False, "message": f"Item '{item_id}' no encontrado en {tipo}"}), 404

    item["imagen"] = imagen_url
    app.logger.info("Imagen actualizada: %s/%s → %s", tipo, item_id, imagen_url or "(eliminada)")
    return jsonify({"ok": True, "item": item})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
