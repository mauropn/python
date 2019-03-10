def sum(a, *b):
    s = a
    for i in b:
        s +=i
    print(s)


sum(10,20, 30, 40)
