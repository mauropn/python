x = ['mauro', 23, 234.23]

for i in x:
    print(i)

x = 'mauro'

for i in x:
    print(i)

for i in [1,3,23,2,3,4,4,5,6,7,7]:
    print(i)

print('==='*10)

for i in range(10):
    print(i)

print('==='*10)

for i in range(10,1, -1):
    print(i)

print('==='*10)

for i in range(1,10):
    if i%5!=0:
        print(i)

print('==='*10)

for i in range(1,1000):
    if i % 5 == 0 or i % 9 == 0:
        continue
    print(i)

print('==='*10)

for i in range(1, 1000):
    if i % 2 == 0:
        pass
    else:
        print(i)
