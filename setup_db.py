import mysql.connector
from mysql.connector import errorcode
from flask_bcrypt import generate_password_hash

import os
from dotenv import load_dotenv

load_dotenv()

print("Conectando...")
try:
    conn = mysql.connector.connect(
        host="127.0.0.1", user="root", password=f"{os.getenv('MY_SQL_PASSWORD')}"
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Existe algo errado no nome de usuário ou senha")
    else:
        print(err)

cursor = conn.cursor()
cursor.execute("DROP DATABASE IF EXISTS `my_game_collection`;")
cursor.execute("CREATE DATABASE `my_game_collection`;")
cursor.execute("USE `my_game_collection`;")

# criando tabelas
TABLES = {}
TABLES[
    "Games"
] = """
      CREATE TABLE `games` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `name` varchar(50) NOT NULL,
      `category` varchar(40) NOT NULL,
      `console` varchar(20) NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;"""

TABLES[
    "Users"
] = """
      CREATE TABLE `users` (
      `name` varchar(50) NOT NULL,
      `username` varchar(8) NOT NULL,
      `password` varchar(100) NOT NULL,
      PRIMARY KEY (`username`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;"""

for tabela_nome in TABLES:
    tabela_sql = TABLES[tabela_nome]
    try:
        print("Criando tabela {}:".format(tabela_nome), end=" ")
        cursor.execute(tabela_sql)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Já existe")
        else:
            print(err.msg)
    else:
        print("OK")

# inserindo usuarios
usuario_sql = "INSERT INTO users (name, username, password) VALUES (%s, %s, %s)"
usuarios = [
    ("Rodrigo Meneses", "rfm", generate_password_hash("1234").decode("utf-8")),
    ("Marta Regina", "maregs", generate_password_hash("4321").decode("utf-8")),
]
cursor.executemany(usuario_sql, usuarios)

cursor.execute("select * from my_game_collection.users")
print(" -------------  Usuários:  -------------")
for user in cursor.fetchall():
    print(user[1])

# inserindo jogos
jogos_sql = "INSERT INTO games (name, category, console) VALUES (%s, %s, %s)"
jogos = [
    ("Tetris", "Puzzle", "Atari"),
    ("God of War", "Hack n Slash", "PS2"),
    ("Mortal Kombat", "Luta", "PS2"),
    ("Valorant", "FPS", "PC"),
    ("Crash Bandicoot", "Hack n Slash", "PS2"),
    ("Need for Speed", "Corrida", "PS2"),
]
cursor.executemany(jogos_sql, jogos)

cursor.execute("select * from my_game_collection.games")
print(" -------------  Jogos:  -------------")
for jogo in cursor.fetchall():
    print(jogo[1])

# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()
