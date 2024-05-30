import secrets

#Metodo por el cual se genera un token de valores aleatorios de 32 caracteres
token = secrets.token_hex(32)

#Eliminar este Print
print(f"Generated API token: {token}")