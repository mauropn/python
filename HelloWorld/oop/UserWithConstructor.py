class Users:
    def __init__(self):
        self.name = 'Mauro'
        self.age = 39

    def update(self):
        self.age = 60


    def compare(self, other):
        if self.age == other.age:
            print(True)
        else:
            print(False)


u1 = Users()
u2 = Users()

print(u1.age)

u1.compare(u2)
u1.update()

print(u1.age)