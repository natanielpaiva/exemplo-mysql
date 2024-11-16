import mysql.connector
from faker import Faker
import random

# Configuração da conexão com o banco de dados
conn = mysql.connector.connect(
    host="localhost",
    user="nataniel",
    password="nataniel123",
    database="DBExemplo"
)
cursor = conn.cursor()

# Inicializa o Faker
fake = Faker()

# Gera algumas categorias fixas e realistas
categories = [
    "Electronics", "Books", "Clothing", "Home Appliances",
    "Sports Equipment", "Toys", "Furniture", "Beauty",
    "Health", "Automotive", "Groceries", "Stationery"
]

# Função para gerar dados e inserir registros
def insert_products(cursor, num_records):
    sql = """
        INSERT INTO products (name, category, price, stock)
        VALUES (%s, %s, %s, %s)
    """
    for _ in range(num_records):
        # Remove a necessidade de unicidade
        name = f"{fake.word().capitalize()} {_}"  # Usa um contador para evitar duplicatas
        category = random.choice(categories)
        price = round(random.uniform(10.0, 1000.0), 2)  # Preços entre 10 e 1000
        stock = random.randint(1, 500)  # Estoque entre 1 e 500 unidades
        cursor.execute(sql, (name, category, price, stock))

# Insere 100 mil registros
print("Inserindo registros...")
insert_products(cursor, 1000000)
conn.commit()
print("Registros inseridos com sucesso!")

# Fecha a conexão
cursor.close()
conn.close()