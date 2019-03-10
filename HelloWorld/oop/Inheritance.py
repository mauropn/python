class A:
    def funcao1(self):
        print("função 1")

    def funcao2(self):
        print("função 2")


class B(A):
    def funcao3(self):
        print("função 3")

    def funcao4(self):
        print("função 4")


class C(B):
    def funcao5(self):
        print("função 5")

class D(A, D): # Possível, mas cuidado com a referencia circular. Isso é só um exemplo de Herança Dupla.
    def funcao6(self):
        print("função 6")

