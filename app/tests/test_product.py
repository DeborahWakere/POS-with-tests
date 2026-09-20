def product_payload(category_id, supplier_id, sku="sku123"):
    return {"name": "Coca Cola", "sku": sku, "price": "100.00", "cost": "60.00", "category_id": category_id, "supplier_id": supplier_id}

def test_list_products(client, auth_headers):
    response = client.get("/products", headers=auth_headers)
    assert response.status_code == 200 and response.json() == []

def test_create_product(client, auth_headers, category, supplier):
    response = client.post("/products", json=product_payload(category.category_id, supplier.supplier_id), headers=auth_headers)
    assert response.status_code == 201
    assert response.json()["name"] == "Coca Cola"

def test_get_product(client, auth_headers, product):
    response = client.get(f"/products/{product.id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["sku"] == "SKU-001"

def test_update_product(client, auth_headers, product, category, supplier):
    response = client.put(f"/products/{product.id}", json=product_payload(category.category_id, supplier.supplier_id, "SKU-002"), headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["sku"] == "SKU-002"

def test_delete_product(client, auth_headers, product):
    response = client.delete(f"/products/{product.id}", headers=auth_headers)
    assert response.status_code == 204
    assert client.get(f"/products/{product.id}", headers=auth_headers).status_code == 404

def test_create_product_with_missing_name_returns_422(client, auth_headers, category, supplier):
    payload = product_payload(category.category_id, supplier.supplier_id)
    payload.pop("name")
    assert client.post("/products", json=payload, headers=auth_headers).status_code == 422


def test_duplicate_product_sku_is_rejected(client, auth_headers, category, supplier):
    payload = product_payload(category.category_id, supplier.supplier_id, "DUP-001")
    assert client.post("/products", json=payload, headers=auth_headers).status_code == 201
    assert client.post("/products", json=payload, headers=auth_headers).status_code == 400

def test_product_missing_resource(client, auth_headers):
    assert client.get("/products/999999", headers=auth_headers).status_code == 404

def test_create_product_with_missing_category_returns_404(client, auth_headers, supplier):
    assert client.post("/products", json=product_payload(999999, supplier.supplier_id), headers=auth_headers).status_code == 404

def test_create_product_with_missing_supplier_returns_404(client, auth_headers, category):
    assert client.post("/products", json=product_payload(category.category_id, 999999), headers=auth_headers).status_code == 404

def test_listing_products_without_credentials_return_401(client):
    assert client.get("/products").status_code == 401
