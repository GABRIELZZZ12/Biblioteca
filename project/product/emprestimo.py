class Emprestimo:
    def __init__(self, livro, pessoa, data_emprestimo=None, data_devolucao=None):
        self.livro = livro
        self.pessoa = pessoa
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
#emprestimo 