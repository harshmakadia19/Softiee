def test_customer_full_crud(client):
    # Create
    resp = client.post("/customer/", json={"name":"Test","email":"t@t.com","phone":"123","address":"NC"})
    assert resp.status_code == 200
    cust_id = resp.json()["id"]
    # Read One & All
    assert client.get(f"/customer/{cust_id}").status_code == 200
    assert len(client.get("/customer/").json()) > 0
    # Update
    assert client.put(f"/customer/{cust_id}", json={"name":"Updated"}).json()["name"] == "Updated"
    # Delete
    assert client.delete(f"/customer/{cust_id}").status_code == 204
    assert client.get(f"/customer/{cust_id}").status_code == 404