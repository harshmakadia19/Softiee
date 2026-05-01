from datetime import date, timedelta


def test_order_full_flow(client):
    # 1. Create Guest Customer [Customer Question #1]
    cust = client.post("/customer/", json={"name": "Guest", "email": "g@g.com", "phone": "123", "address": "NC"}).json()

    # 2. Place Order (Takeout/Delivery) [Customer Question #3]
    order_resp = client.post("/orders/", json={
        "customer_id": cust["id"], "order_type": "delivery",
        "status": "pending", "total_price": 50.0, "tracking_number": "TMP"
    })
    assert order_resp.status_code == 201
    order_id = order_resp.json()["id"]
    track_num = order_resp.json()["tracking_number"]

    # 3. View Specific Order Details [Staff Question #3]
    detail_resp = client.get(f"/orders/{order_id}")
    assert detail_resp.status_code == 200
    assert detail_resp.json()["order_type"] == "delivery"

    # 4. Track by Number [Customer Question #4]
    track_resp = client.get(f"/orders/track/{track_num}")
    assert track_resp.status_code == 200

    # 5. Date Range Filter [Staff Question #7]
    today = date.today().isoformat()
    tomorrow = (date.today() + timedelta(days=1)).isoformat()
    range_resp = client.get(f"/orders/?start_date={today}&end_date={tomorrow}")
    assert range_resp.status_code == 200
    assert len(range_resp.json()) > 0