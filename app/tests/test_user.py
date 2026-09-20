def user_payload(username="newuser"):
    return {"username": username, "password_hash": "hashed-value", "user_role": "cashier"}

def test_list_users(client):
    assert client.get("/users").status_code == 200

def test_create_user(client):
    response = client.post("/users", json=user_payload())
    assert response.status_code == 201
    assert response.json()["username"] == "newuser"

def test_get_user(client, test_user):
    response = client.get(f"/users/{test_user.user_id}")
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

def test_update_user(client, test_user):
    response = client.put(f"/users/{test_user.user_id}", json={"user_role": "manager"})
    assert response.status_code == 200
    assert response.json()["user_role"] == "manager"

def test_delete_user(client, test_user):
    response = client.delete(f"/users/{test_user.user_id}")
    assert response.status_code == 204
    assert client.get(f"/users/{test_user.user_id}").status_code == 404

def test_user_validation_error(client):
    assert client.post("/users", json={"username": "missing"}).status_code == 422


def test_duplicate_username_is_rejected(client, test_user):
    assert client.post("/users", json=user_payload("testuser")).status_code == 400

def test_user_missing_resource(client):
    assert client.get("/users/999999").status_code == 404
