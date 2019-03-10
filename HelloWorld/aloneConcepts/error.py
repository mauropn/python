try:
    a = 5
    b = 0
    print('Abrindo conexao')
    print (a/b)
    print('Fechando conexao')
except ZeroDivisionError:
    print("Deu ruim com zero!")

except Exception as e:
    print("Deu ruim!" + e)

finally:
    print('Fechando conexao')