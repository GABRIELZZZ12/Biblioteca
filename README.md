# 📚 Sistema de Biblioteca com Flask

Sistema web desenvolvido com Flask para gerenciamento de livros, pessoas e empréstimos.

---

## 🚀 Tecnologias utilizadas

- Python 3.11+
- Flask
- MySQL
- HTML/CSS
- Jinja2 (Templates)

---

## ⚙️ Funcionalidades

- ✅ Cadastro de livros
- ✅ Cadastro de pessoas
- ✅ Controle de empréstimos
- ✅ Validação de faixa etária
- ✅ Edição e exclusão de registros
- ✅ Interface web amigável

---

## 📁 Estrutura do projeto
Biblioteca/
└── project/
└── product/
├── main.py # Arquivo principal da aplicação
└── templates/ # Templates HTML
├── base.html # Template base
├── index.html # Página inicial
├── livro.html # Gerenciar livros
├── pessoa.html # Gerenciar pessoas
├── emprestimo.html # Gerenciar empréstimos
└── editar_livro.html # Editar livros

text

---

## 🛠️ Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/GABRIELZZZ12/Biblioteca.git
cd Biblioteca
Importante: Todos os comandos abaixo devem ser executados a partir da raiz do repositório (pasta Biblioteca/).

2. Instale as dependências
bash
pip install -r requirements.txt
Se não tiver o arquivo requirements.txt, instale manualmente:

bash
pip install flask mysql-connector-python python-dotenv
3. Configure o banco de dados MySQL
Abra o MySQL e execute os comandos abaixo:

sql
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
4. Configure as variáveis de ambiente
Crie um arquivo chamado .env na raiz do projeto (Biblioteca/) e adicione:

env
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=sua_senha
MYSQL_DB=biblioteca
⚠️ Atenção: Substitua sua_senha pela sua senha real do MySQL. O arquivo .env não é enviado ao GitHub por segurança.

5. Execute o projeto
bash
cd project/product
python main.py
6. Acesse no navegador
Abra o navegador e acesse o endereço local que aparecer no prompt de comando

Para parar o servidor, pressione Ctrl + C no terminal.

📝 Possíveis problemas e soluções
Erro: TemplateNotFound: index.html
Solução: Certifique-se de que a pasta templates está dentro de project/product/ e contém todos os arquivos HTML.

Erro: ModuleNotFoundError: No module named 'flask'
Solução: Instale as dependências novamente:

bash
pip install flask mysql-connector-python python-dotenv
Erro de conexão com MySQL
Solução: Verifique se:

O MySQL está rodando

As credenciais no arquivo .env estão corretas

O banco de dados biblioteca foi criado


💡 Observações importantes
O arquivo .env não é enviado para o repositório por segurança (está no .gitignore)

Certifique-se de que o MySQL está rodando antes de executar o projeto

O servidor Flask executa em modo debug por padrão (recarrega automaticamente ao salvar alterações)

📦 Criar arquivo requirements.txt
Se ainda não existe, gere o arquivo com:

bash
pip freeze > requirements.txt
Conteúdo esperado:

text
flask
mysql-connector-python
python-dotenv
👨‍💻 Autor
Gabriel Rodrigues

GitHub: @GABRIELZZZ12

📄 Licença
Este projeto está sob a licença MIT