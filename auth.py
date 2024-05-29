import os
import hashlib
from flask import request, jsonify
from functools import wraps
from dotenv import load_dotenv

load_dotenv()

# Leer el token, el nombre de usuario y la contraseña del archivo .env
original_token = os.getenv('API_TOKEN')
original_username = os.getenv('API_USERNAME')
original_password = os.getenv('API_PASSWORD')

# Generar los hash de los valores originales
stored_hashed_token = hashlib.sha256(original_token.encode()).hexdigest()
stored_hashed_username = hashlib.sha256(original_username.encode()).hexdigest()
stored_hashed_password = hashlib.sha256(original_password.encode()).hexdigest()

print("Original Token:", original_token)
print("Original Username:", original_username)
print("Original Password:", original_password)
print("Stored Hashed Token:", stored_hashed_token)
print("Stored Hashed Username:", stored_hashed_username)
print("Stored Hashed Password:", stored_hashed_password)

def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_username = request.headers.get('Username')
        auth_password = request.headers.get('Password')
        auth_token = request.headers.get('Token')

        if not auth_username or not auth_password or not auth_token:
            return jsonify({"message": "Unauthorized"}), 401

        # Verificar las credenciales
        received_hashed_username = hashlib.sha256(auth_username.encode()).hexdigest()
        received_hashed_password = hashlib.sha256(auth_password.encode()).hexdigest()
        received_hashed_token = hashlib.sha256(auth_token.encode()).hexdigest()

        if received_hashed_username != stored_hashed_username or received_hashed_password != stored_hashed_password or received_hashed_token != stored_hashed_token:
            return jsonify({"message": "Unauthorized"}), 401

        return f(*args, **kwargs)
    return decorated_function