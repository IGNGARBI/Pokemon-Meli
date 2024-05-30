import secrets

#Metodo por el cual se genera un username de valores aleatorios de 32 caracteres
user = secrets.token_hex(32)

#Eliminar este Print
print(f"Generated API user: {user}")