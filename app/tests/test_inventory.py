def inventory_payload(product_id, quantity=10):
    return {"product_id": product_id, "quantity": quantity, "location": "Main Store"}

def test_list_inventory_empty(client):
    assert client.get("/inventory").json() == []

def test_create_inventory(client, product):
    response = client.post("/inventory", json=inventory_payload(product.id))
    assert response.status_code == 201
    assert response.json()["quantity"] == 10

def test_get_inventory(client, inventory):
    response = client.get(f"/inventory/{inventory.inventory_id}")
    assert response.status_code == 200
    assert response.json()["quantity"] == 25

def test_update_inventory(client, inventory):
    response = client.patch(f"/inventory/{inventory.inventory_id}", json={"quantity": 40})
    assert response.status_code == 200
    assert response.json()["quantity"] == 40

def test_delete_inventory(client, inventory):
    response = client.delete(f"/inventory/{inventory.inventory_id}")
    assert response.status_code == 204
    assert client.get(f"/inventory/{inventory.inventory_id}").status_code == 404

def test_inventory_duplicate_product_is_rejected(client, product, inventory):
    response = client.post("/inventory", json=inventory_payload(product.id))
    assert response.status_code == 400

def test_inventory_validation_error(client):
    assert client.post("/inventory", json={"quantity": 10}).status_code == 422

def test_inventory_missing_resource(client):
    assert client.get("/inventory/999999").status_code == 404
