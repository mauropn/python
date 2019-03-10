def greet():
    print('Opa!')
    print('Bora programar')

def add(x, y):
    c = x+y
    print(c)

def retornaAlgo():
    return 1000;

def retornaMultiplos():
    return 1000, 'a';

greet()
add(20, 10)

result = retornaAlgo()
print(result)

result, outroResult = retornaMultiplos()
print(result, outroResult)