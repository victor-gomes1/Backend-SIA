# Sistema de Controle de Acesso e Chaves

Este projeto foi desenvolvido como atividade acadêmica com o objetivo de criar um sistema backend para controle de acesso e gerenciamento de chaves físicas.

---

## 📌 Tecnologias Utilizadas

* Python
* FastAPI
* Uvicorn
* PostgreSQL
* Supabase
* DBeaver

---

## 🎯 Funcionalidades

### 🔐 Autenticação

* Login de usuários com email e senha

### 📱 Controle de Acesso

* Validação de acesso via QR Code
* Registro de entradas (logs de acesso)

### 🔑 Controle de Chaves

* Retirada de chaves
* Bloqueio de uso enquanto a chave está em posse de alguém
* Devolução de chaves
* Liberação automática após devolução

### 📋 Histórico

* Registro completo de uso das chaves
* Consulta de quem utilizou, quando retirou e devolveu

---

## ⚙️ Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

### 2. Acessar a pasta

```bash
cd seu-repositorio
```

### 3. Instalar dependências

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary
```

### 4. Configurar conexão com banco

A conexão com o banco de dados é realizada utilizando PostgreSQL (via Supabase).

Para executar o projeto, configure as variáveis de ambiente com os dados da sua conexão:

- Host
- Porta
- Usuário
- Senha
- Nome do banco

---

### 5. Rodar o servidor

```bash
python -m uvicorn main:app --reload
```

---

### 6. Acessar documentação da API

```plaintext
http://127.0.0.1:8000/docs
```

---

## 🧪 Principais Rotas

### 🔐 Login

`POST /login`

---

### 👥 Usuários

`GET /usuarios`

---

### 📱 QR Code

`POST /validar-qr`

---

### 🚪 Registro de Acesso

`POST /registrar-acesso`

---

### 🔑 Chaves

* `POST /retirar-chave`
* `POST /devolver-chave`

---

### 📋 Histórico

`GET /historico-chave/{chave_id}`

---

## 🧠 Descrição do Projeto

O sistema foi projetado para simular um ambiente real de controle de acesso em instituições, permitindo:

* Gerenciamento de usuários
* Controle de entrada e saída
* Monitoramento de recursos físicos (chaves)
* Registro de todas as ações realizadas

---

## 👨‍💻 Autor

Victor Gomes

---

## 📌 Observação

Este projeto tem fins acadêmicos e utiliza dados fictícios.
