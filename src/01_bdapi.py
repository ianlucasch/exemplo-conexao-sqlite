import sqlite3

conexao = sqlite3.connect("../data/meu_bd.sqlite")

cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

def criar_tabela(cursor):
    cursor.execute("""CREATE TABLE clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(100),
                email VARCHAR(150)
                )""")
    conexao.commit()

def inserir_dados(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?);", data)
    conexao.commit()

def inserir_lote_dados(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?, ?);", dados)
    conexao.commit()

def atualizar_dados(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    conexao.commit()

def remover_dados(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    conexao.commit()

def recuperar_cliente(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id=?;", (id,))
    return cursor.fetchone()

cliente = recuperar_cliente(cursor, 1)
print(dict(cliente))
print(cliente["id"], "-", cliente["nome"], "-", cliente["email"])
print(f"Seja bem-vindo ao sistema {cliente["nome"]}.")

def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes ORDER BY nome;")

clientes = listar_clientes(cursor)
for cliente in clientes:
    print(dict(cliente))

def excluir_bd(cursor):
    return cursor.execute("DROP TABLE clientes")

criar_tabela(cursor)

inserir_dados(conexao, cursor, "nome", "email")

dados = [
        ("nome", "email"),
        ("nome", "email"),
        ("nome", "email"),
    ]
inserir_lote_dados(conexao, cursor, dados)

atualizar_dados(conexao, cursor, "nome", "email", "id")

remover_dados(conexao, cursor, 1)

excluir_bd(cursor)

conexao.close()