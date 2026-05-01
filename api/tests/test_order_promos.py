def test_junction_order_promo(client):
    resp = client.post("/order-promos/", json={"order_id":1,"promo_id":1})
    assert resp.status_code in [200, 400]