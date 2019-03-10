from functools import reduce

f = lambda a, b: a+b

result = f(5,6)
print(result)


nums = [3,2, 5, 4, 2, 1]
evens = list(filter(lambda n: n%2 == 0, nums))
doubles = list(map(lambda n: n*2, evens))
sum = reduce(lambda  a, b: a+b, doubles)

print(evens)
print(doubles)
print(sum)