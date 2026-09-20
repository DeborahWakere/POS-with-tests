def customer_payload():
    return {"first_name": "Jane", "last_name": "Doe", "phone_number": "0700000000", "loyalty_points": 5}

def test_list_customers_empty(client):
    assert client.get("/customers").json() == []

def test_create_customer(client):
    response = client.post("/customers", json=customer_payload())
    assert response.status_code == 201
    assert response.json()["first_name"] == "Jane"

def test_get_customer(client, customer):
    response = client.get(f"/customers/{customer.customer_id}")
    assert response.status_code == 200
    assert response.json()["last_name"] == "Doe"

def test_update_customer(client, customer):
    response = client.put(f"/customers/{customer.customer_id}", json={"first_name": "Janet"})
    assert response.status_code == 200
    assert response.json()["first_name"] == "Janet"

def test_delete_customer(client, customer):
    response = client.delete(f"/customers/{customer.customer_id}")
    assert response.status_code == 204
    assert client.get(f"/customers/{customer.customer_id}").status_code == 404

def test_customer_validation_error(client):
    response = client.post("/customers", json={"first_name": "Only"})
    assert response.status_code == 422

def test_customer_missing_resource(client):
    assert client.get("/customers/999999").status_code == 404
