import secrets

user = secrets.token_hex(32)
print(f"Generated API user: {user}")