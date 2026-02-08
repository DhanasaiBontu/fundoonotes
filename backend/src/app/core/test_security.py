from src.app.core.security import hash_password, verify_password

h = hash_password("test123")
print("HASH:", h)
print("CORRECT PASSWORD:", verify_password("test123", h))
print("WRONG PASSWORD:", verify_password("wrong", h))