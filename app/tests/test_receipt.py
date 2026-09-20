from datetime import datetime, timezone

def receipt_payload(sale_id=None, payment_id=None, customer_id=None):
    return {"receipt_barcode": 123456, "issued_at": datetime.now(timezone.utc).isoformat(), "sale_id": sale_id, "payment_id": payment_id, "customer_id": customer_id}

def test_list_receipts_empty(client):
    assert client.get("/receipts").json() == []

def test_create_receipt(client, sale, payment, customer):
    response = client.post("/receipts", json=receipt_payload(sale.sale_id, payment.payment_id, customer.customer_id))
    assert response.status_code == 201
    assert response.json()["receipt_barcode"] == 123456

def test_get_receipt(client, receipt):
    response = client.get(f"/receipts/{receipt.receipt_id}")
    assert response.status_code == 200
    assert response.json()["receipt_barcode"] == 100001

def test_update_receipt(client, receipt):
    response = client.put(f"/receipts/{receipt.receipt_id}", json={"receipt_barcode": 999999})
    assert response.status_code == 200
    assert response.json()["receipt_barcode"] == 999999

def test_delete_receipt(client, receipt):
    response = client.delete(f"/receipts/{receipt.receipt_id}")
    assert response.status_code == 204
    assert client.get(f"/receipts/{receipt.receipt_id}").status_code == 404

def test_receipt_duplicate_barcode_is_rejected(client, receipt):
    payload = receipt_payload(receipt.sale_id, receipt.payment_id, receipt.customer_id)
    payload["receipt_barcode"] = receipt.receipt_barcode
    response = client.post("/receipts", json=payload)
    assert response.status_code == 400

def test_receipt_validation_error(client):
    assert client.post("/receipts", json={}).status_code == 422

def test_receipt_missing_resource(client):
    assert client.get("/receipts/999999").status_code == 404
