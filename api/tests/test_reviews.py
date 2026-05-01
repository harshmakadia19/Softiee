def test_reviews_per_dish(client):
    # 1. Create a review first
    # We include all fields to satisfy schema validation
    client.post("/reviews/", json={
        "order_id": 1,
        "menu_item_id": 1,
        "rating": 5,
        "review_text": "Great service and delicious food!"
    })

    # 2. Filter by dish using the consolidated Query Parameter route
    # Instead of /reviews/dish/1, we use the optional query parameter
    resp = client.get("/reviews/?menu_item_id=1")

    assert resp.status_code == 200
    assert len(resp.json()) > 0
    assert resp.json()[0]["menu_item_id"] == 1