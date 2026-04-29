# 📚 Sistema de Biblioteca com Flask

Sistema web desenvolvido com Flask para gerenciamento de livros, pessoas e empréstimos.

---

## 🚀 Tecnologias utilizadas

* Python
* Flask
* MySQL
* HTML

---

## ⚙️ Funcionalidades

* Cadastro de livros
* Cadastro de pessoas
* Controle de empréstimos
* Validação de faixa etária

---

## 🛠️ Como rodar o projeto

### 1. Clonar o repositório

git clone https://github.com/seu-usuario/biblioteca-flask.git

---

### 2. Instalar dependências

pip install -r requirements.txt

---

### 3. Configurar o banco de dados

Abra o MySQL e execute:

```sql
CREATE DATABASE biblioteca;
USE biblioteca;

CREATE TABLE pessoas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    contato VARCHAR(100),
    ano_nascimento INT
);

CREATE TABLE livros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100),
    autor VARCHAR(100),
    ano INT,
    faixa_etaria VARCHAR(10)
);

CREATE TABLE emprestimos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pessoa_id INT,
    livro_id INT,
    data_emprestimo DATE,
    data_devolucao DATE,
    FOREIGN KEY (pessoa_id) REFERENCES pessoas(id),
    FOREIGN KEY (livro_id) REFERENCES livros(id)
);
```

---

### 4. Criar arquivo `.env`

Crie um arquivo chamado `.env` na raiz do projeto e adicione:

MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=sua_senha
MYSQL_DB=biblioteca

---

### 5. Executar o projeto

python project/product/main.py

---

### 6. Acessar no navegador

http://localhost:5000

---

## 💡 Observações

* O arquivo `.env` não é enviado para o repositório por segurança
* Certifique-se de que o MySQL está rodando

---

## 👨‍💻 Autor

Gabriel Rodrigues
