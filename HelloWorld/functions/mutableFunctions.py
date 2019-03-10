def update(x):
    print(id(x))
    x = 10
    print(id(x))

x = 1
print(x)
update(id(x))
print(x)


def updateUnmutable(lst):
    print("x", id(lst))
    lst[1] = 25
    #id(lst))
    #print("x",  lst)

lst = [10,20,30]
print("i" , id(lst)) #qual o endereço dessa lista?
updateUnmutable(lst)
print("i", lst)