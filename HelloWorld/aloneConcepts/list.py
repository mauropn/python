import random

numbers = range(0, 10)
choseOne = random.choice(numbers)
print(choseOne)

names = [];

names.append(input('Digite seu nome '))
names.append(input('Digite outro nome '))
names.append(input('Digite outro nome '))

print(random.choice(names))

caracteres = input('digite um nome');
print(caracteres[3:8])
print(caracteres[:8])
print(caracteres[10:])
print(caracteres.count('a'))
print(caracteres.find('a'))
print('a' in caracteres)

print(caracteres.replace('a', 'XXXXX'))

print(caracteres.split())
