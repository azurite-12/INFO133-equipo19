-- Crear la base de datos
CREATE DATABASE Comunas;

-- Usar la base de datos
USE Comunas;

-- Crear la tabla Pais
CREATE TABLE Pais (
  Nombre_P VARCHAR(30) PRIMARY KEY
);

-- Crear la tabla Region
CREATE TABLE Region (
  Codigo_R TINYINT PRIMARY KEY,
  Nombre_R VARCHAR(50)
);

-- Crear la tabla Comuna
CREATE TABLE Comuna (
  Codigo_C SMALLINT PRIMARY KEY,
  Nombre_C VARCHAR(30),
  Provincia VARCHAR(30),
  Alcalde VARCHAR(100)
);

-- Crear la tabla Lugar_Clave
CREATE TABLE Lugar_Clave (
  Ubicacion VARCHAR(100) PRIMARY KEY,
  Nombre_L VARCHAR(100)
  Categoria VARCHAR(30),
  Tipo VARCHAR(20),
);

-- Crear la tabla Indicador
CREATE TABLE Indicador (
  Nombre_I VARCHAR(20) PRIMARY KEY,
  Descripcion VARCHAR(100)
);