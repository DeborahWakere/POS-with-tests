from datetime import datetime, timedelta, timezone

import jwt
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()
jwt_secret = "4eebc67988202cf48d154401e393c5a3aef2d7bc03859dca8884e8a0e3d5838f"
jwt_algorithm = "HS256"


def hashed_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(plain_password: str, hashed_pass: str) -> bool:
    return password_hash.verify(plain_password, hashed_pass)


def create_access_token(user_id: int, expires_delta: timedelta | None = None) -> str:
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
    payload = {"sub": str(user_id), "exp": expire}
    return jwt.encode(payload, jwt_secret, algorithm=jwt_algorithm)


def decode_access_token(token: str) -> dict:
    return jwt.decode(token, jwt_secret, algorithms=[jwt_algorithm])
