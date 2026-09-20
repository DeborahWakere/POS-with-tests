from app.core.security import create_access_token, decode_access_token, hashed_password, verify_password

def test_hash_password():
    password = "testpassword"
    password_hash = hashed_password(password)
    assert isinstance(password_hash, str)
    assert password_hash != password

def test_verify_password():
    password_hash = hashed_password("testpassword")
    assert verify_password("testpassword", password_hash)
    assert not verify_password("wrong", password_hash)

def test_access_token_round_trip():
    token = create_access_token(123)
    payload = decode_access_token(token)
    assert payload["sub"] == "123"

def test_invalid_access_token_is_rejected(client):
    response = client.get("/products", headers={"Authorization": "Bearer invalid-token"})
    assert response.status_code == 401
