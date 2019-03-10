class Users:
    def __init__(self, nome, idade): # como se fosse nosso construtor.
        self.nome = nome
        self.age = idade # para demonstrar que poderia ter sido qualquer nome.

    def printSomething(self):
        print("opa!", self.nome, self.age) # por esse motivo, usamos o self....


usu = Users("mauro", 30)

usu.printSomething()
# or....
Users.printSomething(usu)
