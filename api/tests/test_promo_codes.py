def test_promos(client):
    resp = client.post("/promo-codes/", json={"code":"PIZZA50","discount_pct":50.0,"expiration_date":"2026-12-31"})
    assert resp.status_code == 200
    assert resp.json()["code"] == "PIZZA50"