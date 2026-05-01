def test_junction_recipe(client):
    resp = client.post("/item-ingredients/", json={"menu_item_id":1,"ingredient_id":1,"quantity_required":2.0})
    assert resp.status_code in [200, 400]