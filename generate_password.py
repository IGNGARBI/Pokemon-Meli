import secrets

#Metodo por el cual se genera una contraseña de valores aleatorios de 32 caracteres

password = secrets.token_hex(32)

#Eliminar este Print
print(f"Generated API password: {password}")