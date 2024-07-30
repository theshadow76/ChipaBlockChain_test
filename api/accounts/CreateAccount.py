import json
import uuid
import hashlib

class CreateAccount:
    def __init__(self) -> None:
        pass
    def Create(self, name: str, password: str, email: str):
        str_to_hash = f"{name}_{password}_{email}"
        str_to_hash = str_to_hash.encode()
        token = hashlib.sha256(str_to_hash).hexdigest()
        print(token)

# test
acc = CreateAccount()
acc.Create("Vigo", "1234567", "vigopaul05@gmail.com")