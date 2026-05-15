CREATE DATABASE atividade_pratica
GO

USE atividade_pratica
GO

CREATE TABLE Categoria (
	codigo INT PRIMARY KEY,
	titulo VARCHAR(100)
);

CREATE TABLE Noticia (
	codigo INT PRIMARY KEY,
	titulo VARCHAR(100),
	descricao VARCHAR(200),
	data_cadastro DATETIME,
	codigo_categoria INT,
	FOREIGN KEY (codigo_categoria) REFERENCES Categoria (codigo)
);
