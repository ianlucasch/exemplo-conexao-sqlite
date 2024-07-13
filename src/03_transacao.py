import sqlite3

conexao = sqlite3.connect("../data/meu_bd.sqlite")

cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

try:
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?);", ("Teste 2", "teste2@gmail.com"))
    cursor.execute("INSERT INTO clientes (id, nome, email) VALUES (?, ?, ?);", ("id", "Teste 3", "teste3@gmail.com"))
    conexao.commit()
except Exception as exc:
    print(f"Ops! Ocorreu um erro inesperado. {exc}")
    conexao.rollback()