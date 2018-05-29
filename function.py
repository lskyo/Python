def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-88))

import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x)
print(y)


def power(x):
    return x * x


print(power(5))


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(2, 2))
print(power(2))


def add_end(L=[]):
    L.append('end')
    return L


print(add_end([1, 2]))
print(add_end([3, 4]))
print(add_end())
print(add_end([5, 6]))
print(add_end())


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum


print(calc(1, 2))
print(calc(1, 2, 3))
print(calc(1, 2, 3, 4))

num = [1, 2, 3]
print(calc(*num))


def person(name, age, **kbw):
    print('name:', name, 'age:', age, 'other:', kbw)


person('Bom', 32)
person('Bom', 32, city='Beijing', job='Engineer')

extra = {'city': 'Beijing', 'job': 'Teacher'}
person('lskyo', 11, **extra)


def person(name, age, **kw):
    if 'city' in kw:
        print('city', kw['city'])
    if 'job' in kw:
        print('job', kw['job'])
    print('name', name, 'age', age, 'other', kw)


person('Jack', 23, city='Hangzhou', job='Student', H='1')


def person(name, age, *, city, job):
    print(name, age, city, job)


person('lskyo', 12, city='Shenzhen', job='Engineer')


def person(name, age, *args, city, job):
    print(name, age, *args, city, job)


person('lskyo', 24, city='Zhongshan', job='Engineer')


def person(name, age, *, city='Guangdong', job):
    print(name, age, city, job)


person("lskyo", 13, job='Engineer')


def f1(a, b, c=0, *args, **kw):
    print('a:', a, 'b:', b, 'c:', c, 'args:', args, 'kw:', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a:', a, 'b:', b, 'c:', c, 'd:', d, 'kw:', kw)


f1(1, 2)
f1(1, 2, 3)
f1(1, 2, 3, 4)
f1(1, 2, 3, 4, 5)
f1(1, 2, 3, '4', '5')
f1(1, 2, 3, '4', 5, x='x')
f1(1, 2, x='x', y=1)
args = (1, 2, 3)
kw = {'x': 1, 'd': 4}
f1(*args, **kw)
f2(*args, **kw)


def fact(n):
    if (n == 1):
        return 1
    return n * fact(n - 1)


print(fact(1))
print(fact(5))


def fact(n):
	return fact_iter(n,1)

def fact_iter(num, product):
	if num == 1:
		return product
	return fact_iter(num - 1, num * product)


print(fact(5))