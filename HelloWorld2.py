L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
r = []
n = 3
for i in range(n):
    r.append(L[i])

print(L)
print(r)
print(L[0:3])
print(L[:3])
print(L[-2:-1])

L = list(range(100))
print(L)
print(L[0:10])
print(L[-10:])
print(L[:10:2])
print(L[::10])

T = tuple(range(100))
print(T)
print(T[::10])

print('ABCDE'[:3])

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for value in d.values():
    print(value)
for k, v in d.items():
    print(k, ':', v)

for ch in 'ABC':
    print(ch)

from collections import Iterable

result = isinstance('ABC', Iterable)
print("'ABC' is Iterable:", result)
result = isinstance([1, 2, 3], Iterable)
print("[1,2,3] is Iterable:", result)
result = isinstance(123, Iterable)
print("123 is Iterable:", result)

for i, value in enumerate('ABC'):
    print(i, ':', value)

L = list(range(1, 11))
print(L)
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)
L = [x * x for x in range(1, 7)]
print(L)
L = [x * x for x in range(1, 8) if x % 2 == 0]
print(L)
L = [m + n for m in 'ABC' for n in 'XYZ']
print(L)
import os

L = [d for d in os.listdir('.')]
print(L)
print(d)
L = [k + '=' + str(v) for k, v in d.items()]
print(L)


g = (x for x in range(10))
for n in g:
    print(n)


print('========fib============')
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(10)

print('========fib generator============')
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(6)
print(f)
print(next(f))

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    print('step 3')
    yield 3
    print('step 4')
    return 4

o = odd()
next(o)
next(o)
next(o)
try:
    x = next(o)
except StopIteration as e:
    print('Generator return value:', e.value)

print('=======Iterable========')
result = isinstance([], Iterable)
print(result)
result = isinstance({}, Iterable)
print(result)
result = isinstance('ABC', Iterable)
print(result)
result = isinstance((), Iterable)
print(result)
result = isinstance(123, Iterable)
print(result)

from collections import Iterator
print('=======Iterator========')
result = isinstance([], Iterator)
print(result)
result = isinstance({}, Iterator)
print(result)
result = isinstance((), Iterator)
print(result)
result = isinstance('ABC', Iterator)
print(result)
result = isinstance(123, Iterator)
print(result)

result = isinstance(iter([]), Iterator)
print(result)
result = isinstance(iter('abc'), Iterator)
print(result)