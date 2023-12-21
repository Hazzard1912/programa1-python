import sys
from database import connect_db
from utils import procesar_archivo, insertar_datos_informacion, obtener_datos_informacion

def main(archivo):

  db = connect_db()

  if not db:
    print('Error al conectar a la base de datos')
    return

  datos = procesar_archivo(archivo)

  if datos:
    if insertar_datos_informacion(db, datos):
      print('Datos insertados correctamente')
    else:
      print('Error al insertar los datos en la tabla informacion')
  else:
    print('Error al procesar el archivo')

  registros = obtener_datos_informacion(db)

  for registro in registros:
    print(registro)

  db.close()

if __name__ == '__main__':
  if len(sys.argv) == 2:
    archivo = sys.argv[1]
    main(archivo)
  else:
    print('Error: cantidad de parametros invalida')
    print('Uso: python3 programa1.py <archivo>')