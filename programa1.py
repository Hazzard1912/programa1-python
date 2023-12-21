import sys
from flask import Flask, render_template, send_file
from flask_restful import Api
from reportlab.pdfgen import canvas

from database import connect_db, InformacionResource

from utils import procesar_archivo, insertar_datos_informacion, obtener_datos_informacion

app = Flask(__name__)
api = Api(app)
api.add_resource(InformacionResource, '/informacion', '/informacion/<int:page>')

@app.route('/download-pdf/<int:page>')
def download_pdf(page):
  filename = 'informacion.pdf'
  generate_pdf(filename, page)
  return send_file(filename, as_attachment=True)

def generate_pdf(filename, page):
  db = connect_db()
  if db:
    cursor = db.cursor()
    query = f"SELECT * FROM informacion LIMIT 10 OFFSET {(page-1) * 10}"
    cursor.execute(query)
    records = cursor.fetchall()

    with open(filename, 'w+b') as file:
      pdf = canvas.Canvas(file)
      pdf.setFont('Helvetica', 12)
      pdf.drawString(50, 800, f'Información página: {page}')
      pdf.setFont('Helvetica', 8)
      y = 780
      
      for row in records:
        y -= 20
        pdf.drawString(50, y, 
        f"Codigo: {row[0]}," + 
        f" Nombre: {row[1]}," + 
        f" Cant. Lineas: {row[2]}," +
        f" Cant. Palabras: {row[3]}," +
        f" Cant. Caracteres: {row[4]}," +
        f" Fecha de Registro: {row[5]}")

      pdf.save()

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

  # registros = obtener_datos_informacion(db)

  db.close()

if __name__ == '__main__':
  if len(sys.argv) == 2:
    archivo = sys.argv[1]
    main(archivo)
    app.run(debug=True)
  else:
    print('Error: cantidad de parametros invalida')
    print('Uso: python3 programa1.py <archivo>')