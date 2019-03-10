class VisualStudio:
    def execute(self):
        print("compiling")
        print("running")


class MyEditor:
    def execute(self):
        print("spell check")
        print("convention check")
        print("compiling")
        print("running")


class Laptop:
    def code(self, ide):
        ide.execute()


ide = VisualStudio() #Ou MyEditor também funciona. Uma vez que ele obedece o conceito.
lap = Laptop()
lap.code(ide)