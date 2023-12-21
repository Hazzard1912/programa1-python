import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

# Cargamos las variables de entorno:
load_dotenv()

# Establecemos la conexion:
def connect_db():

  try:
    connection = mysql.connector.connect(
      host=os.getenv("DB_HOST"),
      port=os.getenv("DB_PORT"),
      database=os.getenv("DB_DATABASE"),
      user=os.getenv("DB_USER"),
      password=os.getenv("DB_PASSWORD")
    )

    if connection.is_connected():
      db_info = connection.get_server_info()
      print("Conectado a MySQL Server version ", db_info)
      cursor = connection.cursor()
      cursor.execute("select database();")
      record = cursor.fetchone()
      print("Conectado a la base de datos ", record)
      return connection
    
  except Error as e:
    print("Error al conectar a MySQL", e)
    return None