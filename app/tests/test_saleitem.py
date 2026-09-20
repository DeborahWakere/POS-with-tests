def saleitem_payload(sale_id=None, product_id=None):
    return {"quality": 2, "unit_price": "100.00", "sale_id": sale_id, "product_id": product_id}

def test_list_saleitems_empty(client):
    assert client.get("/saleitems").json() == []

def test_create_saleitem(client, sale, product):
    response = client.post("/saleitems", json=saleitem_payload(sale.sale_id, product.id))
    assert response.status_code == 201
    assert response.json()["quality"] == 2

def test_get_saleitem(client, sale_item):
    response = client.get(f"/saleitems/{sale_item.sale_item_id}")
    assert response.status_code == 200
    assert response.json()["quality"] == 2

def test_update_saleitem(client, sale_item):
    response = client.put(f"/saleitems/{sale_item.sale_item_id}", json={"quality": 4})
    assert response.status_code == 200
    assert response.json()["quality"] == 4

def test_delete_saleitem(client, sale_item):
    response = client.delete(f"/saleitems/{sale_item.sale_item_id}")
    assert response.status_code == 204
    assert client.get(f"/saleitems/{sale_item.sale_item_id}").status_code == 404

def test_saleitem_validation_error(client):
    assert client.post("/saleitems", json={"quality": 1}).status_code == 422

def test_saleitem_missing_resource(client):
    assert client.get("/saleitems/999999").status_code == 404
