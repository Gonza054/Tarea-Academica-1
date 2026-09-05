"""RutaLogix - microservicio de facturacion de rutas recorridas.

Segundo microservicio independiente del caso; se despliega por separado
del microservicio de ubicacion (location_service).
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

RATE_PER_KM = 1.8  # tarifa simulada en soles por km

_invoices = []


@app.get("/health")
def health():
    return jsonify(status="ok", service="billing-service"), 200


@app.post("/invoices")
def create_invoice():
    data = request.get_json(silent=True) or {}
    vehicle_id = data.get("vehicleId")
    km = data.get("km")

    if not vehicle_id or km is None:
        return jsonify(error="vehicleId y km son obligatorios"), 400
    if km < 0:
        return jsonify(error="km no puede ser negativo"), 400

    amount = round(km * RATE_PER_KM, 2)
    invoice = {"id": len(_invoices) + 1, "vehicleId": vehicle_id, "km": km, "amount": amount}
    _invoices.append(invoice)
    return jsonify(invoice), 201


@app.get("/invoices")
def list_invoices():
    return jsonify(_invoices), 200


if __name__ == "__main__":
    app.run(port=5002)
