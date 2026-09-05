"""RutaLogix - microservicio de ubicacion (GPS) en tiempo real.

Uno de los varios microservicios independientes del caso. Se despliega
por separado del microservicio de facturacion (billing_service).
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Ultima posicion conocida por vehiculo (simulado en memoria)
_positions = {}


@app.get("/health")
def health():
    return jsonify(status="ok", service="location-service"), 200


@app.post("/vehicles/<vehicle_id>/position")
def update_position(vehicle_id):
    data = request.get_json(silent=True) or {}
    lat, lng = data.get("lat"), data.get("lng")
    if lat is None or lng is None:
        return jsonify(error="lat y lng son obligatorios"), 400
    _positions[vehicle_id] = {"lat": lat, "lng": lng}
    return jsonify(vehicle_id=vehicle_id, position=_positions[vehicle_id]), 200


@app.get("/vehicles/<vehicle_id>/position")
def get_position(vehicle_id):
    position = _positions.get(vehicle_id)
    if position is None:
        return jsonify(error="Vehiculo sin posicion registrada"), 404
    return jsonify(vehicle_id=vehicle_id, position=position), 200


if __name__ == "__main__":
    app.run(port=5001)
