# My Game Collection

Introdução ao Flask baseado no conteúdo da Alura.

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

Consulte **[Implantação](#-implanta%C3%A7%C3%A3o)** para saber como implantar o projeto.

### 📋 Pré-requisitos

Para esse projeto será necessário:
```
Python: 3.10.5
Flask: 2.0.2
SQLAlchemy: 1.4.41
MySQL : 8.0.x
Bootstrap: 5.1.x
``` 


### 🔧 Instalação

Com o Python instalado, é recomendado a criação de um ambiente virtual:

```
python -m venv <nome_ambiente_virtual>
```

Após criar o ambiente virtual e devidamento ativado, é necessário instalar as dependências:

```
pip install -r requirements.txt
```

Termine com um exemplo de como obter dados do sistema ou como usá-los para uma pequena demonstração.

Com tudo devidamente instalador, primeiro é necessário criar o banco de dados com o comando:
```
python setup_db.py
```

Então para rodar o programa basta utilizar o comando:
```
flask run
```

### Informações

Lista de endpoints implementados:

 - Views:
```
/       : Visualiza os jogos cadastrados.
/login  : Acessa o sistema como um usuário.
/logout : Volta para o estado de visitante do sistema.
/new    : Cadastra um jogo. obs: Apenas usuários podem cadastrar
```
 - Administrativas
```
/create         : Insere o jogo cadastrado no Banco de dados e na visualização.
/authenticate   : Autentica o login do usuário no sistema.
```
