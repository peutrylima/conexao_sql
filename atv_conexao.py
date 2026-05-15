import pyodbc
from datetime import datetime

conn_str = (
    'Driver={SQL Server};'
    'Server=PMW-L06N41GK10\SQLEXPRESS;'
    'Database=atividade_pratica;'
    'UID=Sa;'
    'PWD=1234;'
)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

def inserir_categoria(codigo, titulo):
    cursor.execute(
        'INSERT INTO Categoria (codigo, titulo) VALUES (?, ?)',
        (codigo, titulo)
    )
    conn.commit()

def inserir_noticia(codigo, titulo, descricao, data_cadastro, codigo_categoria):
    cursor.execute(
        'INSERT INTO Noticia (codigo, titulo, descricao, data_cadastro, codigo_categoria) VALUES (?, ?, ?, ?, ?)',
        (codigo, titulo, descricao, data_cadastro, codigo_categoria)
    )
    conn.commit()

def consultar_categorias():
    cursor.execute('SELECT * FROM Categoria')
    for row in cursor.fetchall():
        print(row)

def consultar_noticias():
    cursor.execute('SELECT * FROM Noticia')
    for row in cursor.fetchall():
        print(row)

def atualizar_categoria(codigo, novo_titulo):
    cursor.execute(
        'UPDATE Categoria SET titulo = ? WHERE codigo = ?',
        (novo_titulo, codigo)
    )
    conn.commit()

def atualizar_noticia(codigo, novo_titulo):
    cursor.execute(
        'UPDATE Noticia SET titulo = ? WHERE codigo = ?',
        (novo_titulo, codigo)
    )
    conn.commit()

def deletar_categoria(codigo):
    cursor.execute(
        'DELETE FROM Categoria WHERE codigo = ?',
        (codigo,)
    )
    conn.commit()

def deletar_noticia(codigo):
    cursor.execute(
        'DELETE FROM Noticia WHERE codigo = ?',
        (codigo,)
    )
    conn.commit()

inserir_categoria(1, 'Tecnologia')
inserir_noticia(1, 'Nova IA', 'Descrição da notícia', datetime.now(), 1)

print('Categorias:')
consultar_categorias()

print('\nNotícias:')
consultar_noticias()

atualizar_categoria(1, 'Tech')
atualizar_noticia(1, 'IA Atualizada')

print('\nApós atualização:')
consultar_categorias()
consultar_noticias()

deletar_noticia(1)
deletar_categoria(1)

print('\nApós deleção:')
consultar_categorias()
consultar_noticias()


cursor.close()
conn.close()