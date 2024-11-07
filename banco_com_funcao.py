import sqlite3

def criar_banco(nome_banco):
    conexao = sqlite3.connect(nome_banco)
    return conexao



# Criar uma tabela
criar_banco('funcionarios2.db')


