def test_list_categories_empty(client):
    response = client.get("/categories")
    assert response.status_code == 200
    assert response.json() == []

def test_create_category(client):
    response = client.post("/categories", json={"name": "Drinks"})
    assert response.status_code == 201
    body = response.json()
    assert body["name"] == "Drinks"
    assert "id" in body

def test_get_category(client, category):
    response = client.get(f"/categories/{category.category_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Drinks"

def test_update_category(client, category):
    response = client.put(f"/categories/{category.category_id}", json={"name": "Food"})
    assert response.status_code == 200
    assert response.json()["name"] == "Food"

def test_delete_category(client, category):
    response = client.delete(f"/categories/{category.category_id}")
    assert response.status_code == 204
    assert client.get(f"/categories/{category.category_id}").status_code == 404

def test_category_validation_error(client):
    response = client.post("/categories", json={})
    assert response.status_code == 422

def test_category_missing_resource(client):
    response = client.get("/categories/999999")
    assert response.status_code == 404
