-- Creamos la base de datos
CREATE DATABASE IF NOT EXISTS datosdb;

USE datosdb;

-- Creamos la tabla informacion
CREATE TABLE IF NOT EXISTS informacion (
  codigo INT AUTO_INCREMENT PRIMARY KEY,
  nombrearchivo VARCHAR(100) NOT NULL,
  cantlineas INT NOT NULL,
  cantpalabras INT NOT NULL,
  cantcaracteres INT NOT NULL,
  fecharegistro TIMESTAMP NOT NULL
);