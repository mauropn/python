a = 10

def something():
    global a
    a = 100
    print(a)



def somethingDifferent():
    globals() ['a'] #agora, recebemos todas as variáveis globais...
    a = 100
    print(a)


print(a)
something()
print(a)