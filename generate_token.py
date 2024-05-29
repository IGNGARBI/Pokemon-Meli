import secrets

token = secrets.token_hex(32)
print(f"Generated API token: {token}")