import sqlite3

#CRIAR TABELA
def criar_banco(nome_banco):
    conexao = sqlite3.connect(nome_banco)
    return conexao

# CRIAR DADOS DA TABELA
def criar_dados_tabela(conexao):
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE funcionarios2(
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            cargo TEXT NOT NULL,
            dataContratacao TEXT NOT NULL
        )
    ''')
    conexao.commit




# CRIAR UMA TABELA
conexao = criar_banco('funcionarios2.db')

# CRIAR DADOS DA TABELA
criar_dados_tabela(conexao)
