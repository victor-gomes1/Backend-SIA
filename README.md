# Sistema integrado acadêmico 

Este projeto é um backend desenvolvido com **FastAPI** para controle de acesso de usuários e gerenciamento de chaves em um ambiente institucional.

O sistema permite:

* Autenticação de usuários 🔐
* Validação de acesso via QR Code 📱
* Registro de entradas 🚪
* Controle de retirada e devolução de chaves 🔑
* Consulta de histórico 📊

---

## 🧱 Arquitetura do Projeto

O backend foi estruturado de forma **modular**, separando as responsabilidades em diferentes arquivos dentro da pasta `routes`.

Cada módulo representa uma área do sistema:

* **auth.py** → autenticação de usuários
* **acessos.py** → controle de entrada via QR Code
* **chaves.py** → gerenciamento de chaves
* **usuarios.py** → listagem de usuários

Essa abordagem melhora a organização, manutenção e escalabilidade do sistema.

---

## 📁 Estrutura do Projeto

```
backend/
│
├── main.py
├── database.py
│
└── routes/
    ├── auth.py
    ├── acessos.py
    ├── chaves.py
    └── usuarios.py
```

---

## ⚙️ Tecnologias Utilizadas

* Python 🐍
* FastAPI ⚡
* PostgreSQL 🐘
* SQLAlchemy 🧱

---

## 🚀 Como executar o projeto

1. Clone o repositório
2. Instale as dependências:

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary
```

3. Configure a conexão com o banco de dados no arquivo `database.py`

4. Execute o servidor:

```bash
python -m uvicorn main:app --reload
```

5. Acesse a documentação automática (Swagger):

```
http://127.0.0.1:8000/docs
```

---

## 📌 Endpoints da API

### 🔐 Autenticação

* `POST /auth/login` → Realiza login do usuário

---

### 📱 Acessos

* `POST /acessos/validar-qr` → Valida QR Code
* `POST /acessos/registrar-acesso` → Registra entrada

---

### 🔑 Chaves

* `POST /chaves/retirar-chave` → Retirar chave
* `POST /chaves/devolver-chave` → Devolver chave
* `GET /chaves/historico-chave/{chave_id}` → Histórico da chave

---

### 👥 Usuários

* `GET /usuarios/` → Listar usuários

---

## 🧠 Regras de Negócio

* Apenas usuários com status **"Ativo"** podem acessar o sistema
* Uma chave só pode ser retirada se estiver **disponível**
* A devolução só ocorre se houver uma retirada em aberto
* Todas as ações são registradas para controle e histórico

---

## 🔐 Segurança

As senhas estão armazenadas em formato simples apenas para fins acadêmicos.

---

## 🎯 Objetivo do Projeto

Este projeto foi desenvolvido como atividade acadêmica, com foco em:

* Prática de desenvolvimento backend
* Organização de código (boas práticas)
* Integração com banco de dados
* Simulação de um sistema real de controle

---

## 👨‍💻 Autor

Victor Gomes

Estudante de Análise e Desenvolvimento de Sistemas – SENAC

---


