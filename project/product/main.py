from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from datetime import date
import os
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

app = Flask(__name__)

# Configuração do banco (seguro)
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')

mysql = MySQL(app)

# ------------------ MODELOS ------------------

class Pessoa:
    def __init__(self, nome, id=None, contato=None, ano_nascimento=None):
        self.nome = nome
        self.id = id
        self.contato = contato
        self.ano_nascimento = ano_nascimento

    def idade(self):
        if self.ano_nascimento:
            return date.today().year - int(self.ano_nascimento)
        return None


class Livro:
    def __init__(self, titulo, id=None, autor=None, ano=None, faixa_etaria=None):
        self.titulo = titulo
        self.id = id
        self.autor = autor
        self.ano = ano
        self.faixa_etaria = faixa_etaria


# ------------------ ROTAS ------------------

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/livro", methods=["GET", "POST"])
def livro():
    cur = mysql.connection.cursor()

    if request.method == "POST":
        titulo = request.form["titulo"]
        autor = request.form["autor"]
        ano = request.form.get("ano")
        faixa_etaria = request.form.get("faixa_etaria")

        cur.execute("""
            INSERT INTO livros (titulo, autor, ano, faixa_etaria)
            VALUES (%s, %s, %s, %s)
        """, (titulo, autor, ano, faixa_etaria))
        mysql.connection.commit()
        return redirect("/livro")

    cur.execute("SELECT id, titulo, autor, ano, faixa_etaria FROM livros")
    livros = cur.fetchall()
    cur.close()
    return render_template("livro.html", livros=livros)


@app.route("/livro/editar/<int:id>", methods=["GET", "POST"])
def editar_livro(id):
    cur = mysql.connection.cursor()

    if request.method == "POST":
        titulo = request.form["titulo"]
        autor = request.form["autor"]
        ano = request.form.get("ano")
        faixa_etaria = request.form.get("faixa_etaria")

        cur.execute("""
            UPDATE livros
            SET titulo=%s, autor=%s, ano=%s, faixa_etaria=%s
            WHERE id=%s
        """, (titulo, autor, ano, faixa_etaria, id))
        mysql.connection.commit()
        return redirect("/livro")

    cur.execute("SELECT id, titulo, autor, ano, faixa_etaria FROM livros WHERE id=%s", (id,))
    livro = cur.fetchone()
    cur.close()
    return render_template("editar_livro.html", livro=livro)


@app.route("/pessoa", methods=["GET", "POST"])
def pessoa():
    cur = mysql.connection.cursor()

    if request.method == "POST":
        nome = request.form["nome"]
        contato = request.form.get("contato")
        ano_nascimento = request.form.get("ano_nascimento")

        cur.execute("""
            INSERT INTO pessoas (nome, contato, ano_nascimento)
            VALUES (%s, %s, %s)
        """, (nome, contato, ano_nascimento))
        mysql.connection.commit()
        return redirect("/pessoa")

    cur.execute("SELECT id, nome, contato, ano_nascimento FROM pessoas")
    pessoas = cur.fetchall()
    cur.close()
    return render_template("pessoa.html", pessoas=pessoas)


@app.route("/emprestimo", methods=["GET", "POST"])
def emprestimo():
    cur = mysql.connection.cursor()
    erro = None

    if request.method == "POST":
        pessoa_id = int(request.form["pessoa_id"])
        livro_id = int(request.form["livro_id"])

        # Buscar idade
        cur.execute("SELECT ano_nascimento FROM pessoas WHERE id=%s", (pessoa_id,))
        pessoa = cur.fetchone()
        idade = date.today().year - pessoa[0]

        # Buscar faixa etária
        cur.execute("SELECT faixa_etaria FROM livros WHERE id=%s", (livro_id,))
        livro = cur.fetchone()
        faixa = livro[0]

        idade_minima = 0 if faixa.lower() == "livre" else int(faixa.replace("+", ""))

        if idade < idade_minima:
            erro = f"Pessoa de {idade} anos não pode pegar livro {faixa}"
        else:
            cur.execute("""
                INSERT INTO emprestimos (pessoa_id, livro_id, data_emprestimo)
                VALUES (%s, %s, %s)
            """, (pessoa_id, livro_id, date.today()))
            mysql.connection.commit()
            return redirect("/emprestimo")

    cur.execute("SELECT id, nome FROM pessoas")
    pessoas = cur.fetchall()

    cur.execute("SELECT id, titulo FROM livros")
    livros = cur.fetchall()

    cur.execute("""
        SELECT e.id, p.nome, l.titulo, e.data_emprestimo, e.data_devolucao
        FROM emprestimos e
        JOIN pessoas p ON e.pessoa_id = p.id
        JOIN livros l ON e.livro_id = l.id
    """)
    emprestimos = cur.fetchall()
    cur.close()

    return render_template("emprestimo.html",
                           pessoas=pessoas,
                           livros=livros,
                           emprestimos=emprestimos,
                           erro=erro)


@app.route("/devolucao/<int:id>", methods=["POST"])
def devolucao(id):
    cur = mysql.connection.cursor()
    cur.execute("UPDATE emprestimos SET data_devolucao=%s WHERE id=%s", (date.today(), id))
    mysql.connection.commit()
    cur.close()
    return redirect("/emprestimo")


if __name__ == "__main__":
    app.run(debug=True)