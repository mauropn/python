def person(name, **data):
    print(name)
    print(data)

    for i, j in data.items():
        print(i,j)


person('Mauro', idade=10, cidade='São Paulo', telefone=24234234)
