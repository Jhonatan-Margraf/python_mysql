import mysql.connector
from datetime import date

# Conexão com o banco de dados
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='biblioteca'
)

cursor = conn.cursor()

# Função para inserir usuário
def inserir_usuario():
    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")
    data_cadastro = date.today()  # Usa a data atual do sistema

    query = """
    INSERT INTO usuarios (nome, email, telefone, endereco, data_cadastro)
    VALUES (%s, %s, %s, %s, %s)
    """
    valores = (nome, email, telefone, endereco, data_cadastro)

    try:
        cursor.execute(query, valores)
        conn.commit()
        print("Usuário inserido com sucesso!")
    except mysql.connector.Error as err:
        print("Erro:", err)
        conn.rollback()

# Executa a função
inserir_usuario()

# Fecha conexão
cursor.close()
conn.close()
