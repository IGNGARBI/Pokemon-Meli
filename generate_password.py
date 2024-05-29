import secrets

password = secrets.token_hex(32)
print(f"Generated API password: {password}")