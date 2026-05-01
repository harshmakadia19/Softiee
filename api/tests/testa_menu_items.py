def test_menu_staff_and_customer(client):
    # 1. Staff: Create/Update/Delete [Staff Question #1]
    item = client.post("/menu/", json={"name": "Salad", "price": 10.0, "category": "Veggie", "calories": 200}).json()
    item_id = item["id"]

    # Update
    client.put(f"/menu/{item_id}", json={"price": 12.0})

    # 2. Customer: Search for Vegetarian [Customer Question #5]
    search = client.get("/menu/search?category=Veggie")
    assert len(search.json()) > 0

    # Delete
    assert client.delete(f"/menu/{item_id}").status_code == 204