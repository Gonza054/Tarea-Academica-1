from app import app


def client():
    return app.test_client()


def test_health():
    res = client().get("/health")
    assert res.status_code == 200


def test_create_invoice():
    res = client().post("/invoices", json={"vehicleId": "V1", "km": 10})
    assert res.status_code == 201
    body = res.get_json()
    assert body["amount"] == 18.0


def test_create_invoice_missing_fields():
    res = client().post("/invoices", json={"km": 10})
    assert res.status_code == 400


def test_create_invoice_negative_km():
    res = client().post("/invoices", json={"vehicleId": "V1", "km": -5})
    assert res.status_code == 400


def test_list_invoices():
    c = client()
    c.post("/invoices", json={"vehicleId": "V1", "km": 5})
    res = c.get("/invoices")
    assert res.status_code == 200
    assert isinstance(res.get_json(), list)
