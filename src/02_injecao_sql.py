import sqlite3

conexao = sqlite3.connect("../data/meu_db.sqlite")

cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

# Forma incorreta:
id_cliente = input("Informe o id do cliente: ")
cursor.execute(f"SELECT * FROM clientes WHERE id={id_cliente};")
clientes = cursor.fetchall()
for cliente in clientes:
    print(dict(cliente))