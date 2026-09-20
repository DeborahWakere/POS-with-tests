from datetime import datetime, timezone

def sale_payload(user_id=None, customer_id=None):
    return {"sale_date": datetime.now(timezone.utc).isoformat(), "total_amount": "150.00", "user_id": user_id, "customer_id": customer_id}

def test_list_sales_empty(client):
    assert client.get("/sales").json() == []

def test_create_sale(client, test_user, customer):
    response = client.post("/sales", json=sale_payload(test_user.user_id, customer.customer_id))
    assert response.status_code == 201
    assert response.json()["total_amount"] .startswith("150.00")

def test_get_sale(client, sale):
    response = client.get(f"/sales/{sale.sale_id}")
    assert response.status_code == 200
    assert response.json()["total_amount"] .startswith("200.00")

def test_update_sale(client, sale):
    response = client.put(f"/sales/{sale.sale_id}", json={"total_amount": "250.00"})
    assert response.status_code == 200
    assert response.json()["total_amount"] .startswith("250.00")

def test_delete_sale(client, sale):
    response = client.delete(f"/sales/{sale.sale_id}")
    assert response.status_code == 204
    assert client.get(f"/sales/{sale.sale_id}").status_code == 404

def test_sale_validation_error(client):
    assert client.post("/sales", json={"total_amount": "10.00"}).status_code == 422

def test_sale_missing_resource(client):
    assert client.get("/sales/999999").status_code == 404
