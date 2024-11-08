import sqlite3

#CRIAR TABELA
def criar_banco(nome_banco):
    conexao = sqlite3.connect(nome_banco)
    return conexao

# CRIAR DADOS DA TABELA
def criar_dados_tabela(conexao):
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS funcionarios2(
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            cargo TEXT NOT NULL,
            dataContratacao TEXT NOT NULL
        )
    ''')
    conexao.commit()
    return cursor

# INSERINDO FUNCIONARIOS NA TABELA
def func_na_tabela():
    nome = input('Digite um nome: ')
    cargo = input('Digite um cargo: ')
    data = input('Digite uma data no formato aaaa-mm-dd: ')
    return nome,cargo,data


# CRIAR UMA TABELA
conexao = criar_banco('funcionarios2.db')

# CRIAR DADOS DA TABELA
cursor = criar_dados_tabela(conexao)

# INSERINDO FUNCIONARIOS NA TABELA
nome,cargo,data = func_na_tabela()
cursor.execute("INSERT INTO funcionarios2 (id,nome,cargo,dataContratacao) VALUES (NULL,?,?,?)",(
    nome,cargo,data))
conexao.commit()

nome,cargo,data = func_na_tabela()
cursor.execute("INSERT INTO funcionarios2 (id,nome,cargo,dataContratacao) VALUES (NULL,?,?,?)",(
    nome,cargo,data))
conexao.commit()