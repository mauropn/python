class A:
    def show(self):
        print("show de A")

class B(A):
    pass
    # def show(self):
    #    print("show de B")


q = B()
q.show()