def test_reviews_per_dish(client):
    # Create review
    client.post("/reviews/", json={"order_id":1,"menu_item_id":1,"rating":5,"review_text":"Great!"})
    # Filter by dish
    resp = client.get("/reviews/dish/1")
    assert resp.status_code == 200