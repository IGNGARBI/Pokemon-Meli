Este proyecto es una API de Pokémon desarrollada en Flask que proporciona información sobre Pokémon y permite realizar consultas sobre tipos de Pokémon, obtener Pokémon aleatorios por tipo y encontrar el Pokémon con el nombre más largo de un tipo específico. La autenticación se maneja mediante un sistema de tokens.

# Requisitos

- Python 3.x
- pip (el gestor de paquetes de Python)

# Instalación

1. **Clonar el repositorio:**

    ```sh
    git clone https://github.com/tu-usuario/tu-repo.git
    cd tu-repo
    ```

2. **Crear y activar un entorno virtual (opcional pero recomendado):**

    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. **Instalar las dependencias:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Crear un archivo `.env` en la raíz del proyecto con las siguientes variables de entorno:**

    ```dotenv
    API_TOKEN=Valor correspondiente al Token
    API_USERNAME=Valor correspondiente al Username
    API_PASSWORD=Valor correspondiente al Password
    ```

## Funcionamiento

1. **Ejecutar la aplicación:**

    ```sh
    python app.py
    ```

    La aplicación estará disponible en `http://127.0.0.1:5000`.

2. **Probar los endpoints con `curl`:**

    ```sh
    curl -H "Username: Valor correspondiente al Token" \
         -H "Password: Valor correspondiente al Username" \
         -H "Token:Valor correspondiente al Password" \
         http://127.0.0.1:5000/pokemon/type/pikachu

    ```
    ## En caso de NO coincidir alguno de los valores en el curl con los valores guardados en el .env, se devuelve un mensaje de "Unauthorized" 

    ### Endpoints disponibles

    - **GET /pokemon/type/<name>**

        Obtener los tipos de un Pokémon por su nombre.

        ```sh
        curl -H "Username: Valor correspondiente al Username" \
             -H "Password:Valor correspondiente al Password" \
             -H "Token: Valor correspondiente al Token" \
             http://127.0.0.1:5000/pokemon/type/<name>
        ```

    - **GET /pokemon/random/<type_name>**

        Obtener un Pokémon aleatorio de un tipo específico.

        ```sh
        curl -H "Username: Valor correspondiente al Username" \
             -H "Password: Valor correspondiente al Password" \
             -H "Token: Valor correspondiente al Token" \
             http://127.0.0.1:5000/pokemon/random/<type_name>
        ```

    - **GET /pokemon/longest_name/<type_name>**

        Obtener el Pokémon con el nombre más largo de un tipo específico.

        ```sh
        curl -H "Username:Valor correspondiente al Username" \
             -H "Password:Valor correspondiente al Password" \
             -H "Token: Valor correspondiente al Token" \
             http://127.0.0.1:5000/pokemon/longest_name/<type_name>
        ```

## Desarrollo


### Estructura del proyecto

```
.
├── .env
├── .gitignore
├── app.py
├── auth.py
├── generate_password.py
├── generate_user.py
├── generate_token.py
├── requirements.txt
└── README.md

```

## Aclaraciones de seguridad

Para mayor seguridad las credenciales del .env se generan utilizando el modulo secrets de Python y tokens.
Al correr el archivo generate_password.py, generate_token.py y/o generate_user.py se genera una contraseña/valor de 32 bytes en forma hexagesimal

Al probar el correcto funcionamiento del proyecto, se sugiere crear el archivo .env y rellenar los valores con los resultados generados por el modulo secrets en cada archivo correspondiente
