from datetime import date

def test_staff_analytics(client):
    # 1. Daily Revenue [Staff Question #6]
    today = date.today().isoformat()
    rev = client.get(f"/analytics/revenue/{today}")
    assert rev.status_code == 200

    # 2. Stock Alerts [Staff Question #2]
    alerts = client.get("/analytics/alerts/low-stock")
    assert alerts.status_code == 200

    # 3. Unpopular Dishes [Staff Question #4]
    unpopular = client.get("/analytics/dishes/unpopular")
    assert unpopular.status_code == 200