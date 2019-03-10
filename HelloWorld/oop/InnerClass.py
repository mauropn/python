class Estudante:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.treinamento = self.Curso()

    def show(self):
        print(self.nome, self.idade)
        self.treinamento.show()

    class Curso:
        def __init__(self):
            self.nome = 'SLDF'
            self.periodo = 4

        def show(self):
            print(self.nome, self.periodo)


e1 = Estudante("Mauro", 20)

e1.show()

