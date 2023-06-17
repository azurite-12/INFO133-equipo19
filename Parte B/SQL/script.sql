CREATE DATABASE Comunas;

USE Comunas;

CREATE TABLE Pais (
  Nombre_P VARCHAR(30) PRIMARY KEY
);

CREATE TABLE Region (
  FK_nombreP VARCHAR(50),
  Codigo_R TINYINT PRIMARY KEY,
  Nombre_R VARCHAR(50),
  FOREIGN KEY (FK_nombreP) REFERENCES Pais (Nombre_P)
);

CREATE TABLE Comuna (
  Codigo_C SMALLINT PRIMARY KEY,
  Nombre_C VARCHAR(30),
  Provincia VARCHAR(30),
  Alcalde VARCHAR(100)
);

CREATE TABLE Lugar_Clave (
  FK_codigoC SMALLINT,
  Ubicacion VARCHAR(100) PRIMARY KEY,
  Nombre_L VARCHAR(100),
  Categoria VARCHAR(30),
  Tipo VARCHAR(20),
  FOREIGN KEY (FK_codigoC) REFERENCES Comuna(Codigo_C)
);

CREATE TABLE Indicador (
  Nombre_I VARCHAR(20) PRIMARY KEY,
  Descripcion VARCHAR(100)
);

CREATE TABLE Poseer (
  FK_codigoR TINYINT,
  FK_codigoC SMALLINT,
  PRIMARY KEY (FK_codigoR, FK_codigoC),
  FOREIGN KEY (FK_codigoR) REFERENCES Region(Codigo_R),
  FOREIGN KEY (FK_codigoC) REFERENCES Comuna(Codigo_C)
);

CREATE TABLE Tener_Valor (
  Fecha SMALLINT,
  Total FLOAT,
  FK_nombreI VARCHAR(20),
  FK_codigoC SMALLINT,
  PRIMARY KEY (FK_nombreI, FK_codigoC),
  FOREIGN KEY (FK_nombreI) REFERENCES Indicador(Nombre_I),
  FOREIGN KEY (FK_codigoC) REFERENCES Comuna(Codigo_C)
);