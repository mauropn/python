num = int(input('digite um número'))
num2 = int(input('digite outro número'))
if num > num2:
    print('{} foi maior que {}'.format(num, num2))
elif num == num2:
    print('{} é igual a {}'.format(num2, num))
else:
    print('{} foi maior que {}'.format(num2, num))
