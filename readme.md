## Configuración

Esta aplicación requiere la creación de dos archivos `.env` para funcionar correctamente.

### Archivo `.env` de la carpeta raíz

Crea un archivo `.env` en la carpeta raíz del proyecto y establece las siguientes variables:

- DB_HOST=
- DB_PORT=
- DB_DATABASE=
- DB_USER=
- DB_PASSWORD=

### Archivo `.env` de la carpeta `data`

Crea un archivo `.env` en la carpeta `data` y establece las siguientes variables:

- MYSQL_ROOT_PASSWORD=
- MYSQL_DATABASE=
- MYSQL_USER=
- MYSQL_PASSWORD=

## Levantamiento del contenedor

Una vez que hayas creado los archivos `.env`, puedes ejecutar el proyecto con el siguiente comando:

`docker-compose up -d`

## Instalado dependencias

Se debe crear el entorno virtual, activarlo e instalar las dependencias señaladas en _requirements.txt_

## Ejecución

El programa se debe utilizar de la siguiente manera:

`python programa1.py <archivo.txt>`
