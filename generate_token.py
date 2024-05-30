import secrets

#Metodo por el cual se genera un token de valores aleatorios de 32 caracteres
token = secrets.token_hex(32)

#Eliminar este Print después de pegar el valor correspondiente en el archivo .env
print(f"Generated API token: {token}")