def supplier_payload(name="Supplier A"):
    return {"supplier_name": name, "contact_person": "Alice", "contact_number": "0700000000"}

def test_list_suppliers_empty(client):
    assert client.get("/suppliers").json() == []

def test_create_supplier(client):
    response = client.post("/suppliers", json=supplier_payload())
    assert response.status_code == 201
    assert response.json()["supplier_name"] == "Supplier A"

def test_get_supplier(client, supplier):
    response = client.get(f"/suppliers/{supplier.supplier_id}")
    assert response.status_code == 200
    assert response.json()["supplier_name"] == "Test Supplier"

def test_update_supplier(client, supplier):
    response = client.put(f"/suppliers/{supplier.supplier_id}", json={"supplier_name": "Updated Supplier"})
    assert response.status_code == 200
    assert response.json()["supplier_name"] == "Updated Supplier"

def test_delete_supplier(client, supplier):
    response = client.delete(f"/suppliers/{supplier.supplier_id}")
    assert response.status_code == 204
    assert client.get(f"/suppliers/{supplier.supplier_id}").status_code == 404

def test_supplier_validation_error(client):
    assert client.post("/suppliers", json={"supplier_name": "Incomplete"}).status_code == 422


def test_duplicate_supplier_name_is_rejected(client, supplier):
    assert client.post("/suppliers", json=supplier_payload("Test Supplier")).status_code == 400

def test_supplier_missing_resource(client):
    assert client.get("/suppliers/999999").status_code == 404
