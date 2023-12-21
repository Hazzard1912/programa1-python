from datetime import datetime


def insertar_datos_informacion(db, datos):

  try:    
    cursor = db.cursor()
    sql = 'INSERT INTO informacion(nombrearchivo, cantlineas, cantpalabras, cantcaracteres, fecharegistro) VALUES(%s, %s, %s, %s, %s)';
    cursor.executemany(sql, datos)
    db.commit()
    return True
  
  except Exception as e:
    print('Error al insertar los datos en la tabla informacion', e)
    return False

  finally:
    cursor.close()


def obtener_datos_informacion(db):
  try:
    cursor = db.cursor()
    sql = 'SELECT * FROM informacion'
    cursor.execute(sql)
    datos = cursor.fetchall()
    return datos
  
  except Exception as e:
    print('Error al obtener los datos de la tabla informacion')
    return None

  finally:
    cursor.close()

  
def procesar_archivo(archivo):
  try:
    with open(archivo, 'r') as archivo:
      contenido = archivo.readlines()
      nombrearchivo = archivo.name
      cantlineas = len(contenido)
      cantpalabras = sum(len(linea.rstrip('\n')) for linea in contenido)
      cantcaracteres = sum(len(linea) for linea in contenido)
      fecharegistro = datetime.now()

      datos = [(nombrearchivo, cantlineas, cantpalabras, cantcaracteres, fecharegistro)]

      return datos
  except Exception as e:
    print('Error al procesar el archivo')
    return None