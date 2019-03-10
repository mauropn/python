num01=input("Primeiro Número: ")
num02=input("Segundo número: ")
soma = num01 + num02

print('A soma entre ', num01, ' e ', num02, 'foi: ', int(num01) + int(num02))
print('A soma entre {} e {} é igual a {}'.format(num01, num02, soma))

num01 = int(input('Digite novamente o 1o. numero'))
num02 = int(input('Digite novamente o 2o. numero'))
soma = num01 + num02

print('OTIMIZADO: A soma entre {} e {} é igual a {}'.format(num01, num02, soma))
print('Soma = ', int(num01) + int(num02))
print('Sub = ', int(num01) - int(num02))
print('Multi = ', int(num01) * int(num02))
print('Divi = ', int(num01) / int(num02))
print('Expo = ', int(num01) ** int(num02))
print('Expo = ', pow(num01,num02))
print('Divi exata = ', int(num01) // int(num02))
print('resto = ', int(num01) % int(num02))
print( 'Numero formatado {:.3f}'.format(num01 ** num02))
print( 'Sucessor de {} é {}'.format(num01, ++num02))
