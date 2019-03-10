from threading import *
from time import sleep


class Oi(Thread):
    def run(self):
        for i in range(10):
            sleep(1)
            print("Oi")


class Opa(Thread):
    def run(self):
        for i in range(10):
            sleep(1)
            print("Opa")


obj_oi = Oi()
obj_opa = Opa()

obj_oi.start()
sleep(0.1)
obj_opa.start()

# Para que a Main thread espere as mensagens terminarem... antes de executar o Foi... a gente manda eles juntarem.
obj_oi.join()
obj_opa.join()

print("Foi...")