def test_ingredient_crud(client):
    resp = client.post("/ingredients/", json={"name":"Cheese","amount":100.0,"unit":"slices"})
    assert resp.status_code == 200
    ing_id = resp.json()["id"]
    assert client.get(f"/ingredients/{ing_id}").json()["name"] == "Cheese"