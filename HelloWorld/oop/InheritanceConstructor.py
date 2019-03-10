class A:
    def __init__(self):
        print('construtor de A')

    def funcao1(self):
        print("função 1")

    def funcao2(self):
        print("função 2")


class B(A):
    def __init__(self):
        super().__init__()
        print('construtor de B')

    def funcao3(self):
        print("função 3")

    def funcao4(self):
        print("função 4")



A1 = B()