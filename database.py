import os
import datetime
from flask_restful import Resource
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

class InformacionResource(Resource):
  def get(self, page=1):
    connection = connect_db()
    if connection:
      try:
        cursor = connection.cursor()
        query = f"SELECT * FROM informacion LIMIT 10 OFFSET {(page-1) * 10}"
        cursor.execute(query)
        records = cursor.fetchall()
        cursor.close()
        connection.close()

        # Convertir objetos datetime a cadenas de texto
        for i in range(len(records)):
          record = list(records[i])
          if isinstance(record[5], datetime.datetime):
            record[5] = record[5].strftime('%Y-%m-%d %H:%M:%S')
          records[i] = tuple(record)
                
        return records

      except Error as e:
        print("Error al consultar datos", e)
        return None
    
    else:
      print("Error al conectar a la base de datos")
      return None