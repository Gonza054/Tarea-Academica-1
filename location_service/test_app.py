from app import app


def client():
    return app.test_client()


def test_health():
    res = client().get("/health")
    assert res.status_code == 200
    assert res.get_json()["status"] == "ok"


def test_update_and_get_position():
    c = client()
    res = c.post("/vehicles/V1/position", json={"lat": -12.05, "lng": -77.03})
    assert res.status_code == 200

    res = c.get("/vehicles/V1/position")
    assert res.status_code == 200
    assert res.get_json()["position"]["lat"] == -12.05


def test_update_position_missing_fields():
    res = client().post("/vehicles/V2/position", json={"lat": -12.05})
    assert res.status_code == 400


def test_get_position_not_found():
    res = client().get("/vehicles/UNKNOWN/position")
    assert res.status_code == 404
