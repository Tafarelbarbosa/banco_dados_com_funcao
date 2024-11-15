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

# LISTAR TODOS OS DADOS DA TABELA
def listar_dados():
    cursor.execute("SELECT * FROM funcionarios2")
    funcionarios = cursor.fetchall()
    print(funcionarios)

# Alterar dados de uma tabela
def update_data():
    id = input ("Informe o número do id: ")
    cargo = input("Digite o cargo para alterar: ")
    up = cursor.execute("UPDATE funcionarios2 SET cargo = ? WHERE id = ?",(cargo,id))
    conexao.commit()
    return up

# Excluir dados de uma tabela
def del_table():
    id = input ('Digite um id do funcionário que você deseja remover: ')
    deletar = cursor.execute("DELETE FROM funcionarios2 WHERE id = ?", (id))
    conexao.commit()
    return deletar

# CRIAR UMA TABELA
conexao = criar_banco('funcionarios2.db')

# CRIAR DADOS DA TABELA
cursor = criar_dados_tabela(conexao)

# Adicionar novos dados na tabela
def updatenew_data():
    nome = input("Digite o nome do funcionário: ")
    cargo = input("Digite o cargo: ")
    data = input("Digite a data: ")
    up_new = cursor.execute("INSERT INTO funcionarios2 (id,nome,cargo,dataContratacao) VALUES (NULL,?,?,?)",
                (nome,cargo,data))
    conexao.commit()
    return up_new
# INSERINDO FUNCIONARIOS NA TABELA
# nome,cargo,data = func_na_tabela()
# cursor.execute("INSERT INTO funcionarios2 (id,nome,cargo,dataContratacao) VALUES (NULL,?,?,?)",(
#     nome,cargo,data))
# conexao.commit()

# nome,cargo,data = func_na_tabela()
# cursor.execute("INSERT INTO funcionarios2 (id,nome,cargo,dataContratacao) VALUES (NULL,?,?,?)",(
#     nome,cargo,data))
# conexao.commit()

# LISTAR TODOS OS DADOS DA TABELA
listar_dados()

# Alterar dados de uma tabela
# update_data()

# Excluir dados de uma tabela
# del_table()

# Adicionar novos dados na tabela
updatenew_data()

conexao.close()