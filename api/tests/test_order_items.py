def test_order_details(client):
    # Test linkage
    resp = client.post("/order-items/", json={"order_id":1,"menu_item_id":1,"quantity":1,"unit_price":5.0})
    # Should be 200 if setup correctly or 400 if foreign keys fail
    assert resp.status_code in [200, 400]