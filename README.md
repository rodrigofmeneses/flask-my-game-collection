# My Game Collection

Introdução ao Flask baseado no conteúdo da Alura.

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

Consulte **[Implantação](#-implanta%C3%A7%C3%A3o)** para saber como implantar o projeto.

### 📋 Pré-requisitos

Para esse projeto será necessário:
```
Python: 3.10.5
MySQL : 8.0.x
``` 


### 🔧 Instalação

Com todos os pré requisitos devidamente instalados, na raiz do projeto crie um ambiente virtual:

```
python -m venv venv
```


Após criar o ambiente virtual é necessário ativa-lo, ```venv\Scripts\activate``` no terminal do Windows, ou ```source bin/activate``` no linux.

Se tudo ocorreu bem, em algum local no terminal terá o nome do ambiente ativado ```(venv)```.

Feito isso, agora é necessário instalar as dependências:

```
pip install -r requirements.txt
```

### ▶️ Execução

Primeiramente é necessário criar o banco de dados executando o comando:
```
python setup_db.py
```

Então para rodar o programa basta utilizar o comando:
```
flask run
```

Se tudo ocorreu bem, o terminal deverá apresentar algo como:

```
 * Serving Flask app 'mgc:app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 423-939-601
```

## ⚠️ Atenção

Verifique as credenciais do Banco de dados no ```.env``` e as credencias dos usuários cadastrados em ```setup_db.py```!