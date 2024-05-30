import os
import hashlib
from flask import request, jsonify
from functools import wraps
from dotenv import load_dotenv

load_dotenv()

# Valores traidos desde el archivo .env donde se guarda de forma segura las variables de entorno
original_token = os.getenv('API_TOKEN')
original_username = os.getenv('API_USERNAME')
original_password = os.getenv('API_PASSWORD')

# Se generan los hash de los valores importados del .env para mayor seguridad
stored_hashed_token = hashlib.sha256(original_token.encode()).hexdigest()
stored_hashed_username = hashlib.sha256(original_username.encode()).hexdigest()
stored_hashed_password = hashlib.sha256(original_password.encode()).hexdigest()

#Hay que eliminar esto porque es como una falla de seguridad
print("Original Token:", original_token)
print("Original Username:", original_username)
print("Original Password:", original_password)
print("Stored Hashed Token:", stored_hashed_token)
print("Stored Hashed Username:", stored_hashed_username)
print("Stored Hashed Password:", stored_hashed_password)


#Se hace una request para traer  los valores de username, password y token con los valores traidos del .env
def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_username = request.headers.get('Username')
        auth_password = request.headers.get('Password')
        auth_token = request.headers.get('Token')

        if not auth_username or not auth_password or not auth_token:
            return jsonify({"message": "Unauthorized"}), 401

        # Se verifican las credenciales de username, password y token respectivamente. Si no coinciden, se devuelve un mensaje de "No autorizado"
        received_hashed_username = hashlib.sha256(auth_username.encode()).hexdigest()
        received_hashed_password = hashlib.sha256(auth_password.encode()).hexdigest()
        received_hashed_token = hashlib.sha256(auth_token.encode()).hexdigest()

        if received_hashed_username != stored_hashed_username or received_hashed_password != stored_hashed_password or received_hashed_token != stored_hashed_token:
            return jsonify({"message": "Unauthorized"}), 401

        return f(*args, **kwargs)
    return decorated_function