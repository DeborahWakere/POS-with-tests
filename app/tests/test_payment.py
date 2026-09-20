def payment_payload(sale_id=None):
    return {"payment_method": "cash", "amount_paid": "200.00", "sale_id": sale_id}

def test_list_payments_empty(client):
    assert client.get("/payments").json() == []

def test_create_payment(client, sale):
    response = client.post("/payments", json=payment_payload(sale.sale_id))
    assert response.status_code == 201
    assert response.json()["payment_method"] == "cash"

def test_get_payment(client, payment):
    response = client.get(f"/payments/{payment.payment_id}")
    assert response.status_code == 200
    assert response.json()["amount_paid"].startswith("200.00")

def test_update_payment(client, payment):
    response = client.put(f"/payments/{payment.payment_id}", json={"payment_method": "card"})
    assert response.status_code == 200
    assert response.json()["payment_method"] == "card"

def test_delete_payment(client, payment):
    response = client.delete(f"/payments/{payment.payment_id}")
    assert response.status_code == 204
    assert client.get(f"/payments/{payment.payment_id}").status_code == 404

def test_payment_validation_error(client):
    assert client.post("/payments", json={"payment_method": "cash"}).status_code == 422

def test_payment_missing_resource(client):
    assert client.get("/payments/999999").status_code == 404
