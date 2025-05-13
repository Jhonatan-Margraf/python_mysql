import mysql.connector

# Conexão com o banco de dados
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='sua_senha',
    database='biblioteca'
)

cursor = conn.cursor()

# Função para inserir usuário
def inserir_usuario():
    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")

    query = """
    INSERT INTO usuarios (nome, email, telefone, endereco)
    VALUES (%s, %s, %s, %s)
    """
    valores = (nome, email, telefone, endereco)

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