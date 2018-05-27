def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x

print(my_abs(-88))

import math

def move(x, y, step, angle = 0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny

x, y = move(100,100, 60, math.pi / 6)
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

print(power(2,2))
print(power(2))

def add_end(L=[]):
	L.append('end')
	return L

print(add_end([1,2]))
print(add_end([3,4]))
print(add_end())
print(add_end([5,6]))
print(add_end())

def calc(*numbers):
	sum = 0
	for n in numbers:
		sum += n * n
	return sum

print(calc(1,2))
print(calc(1,2,3))
print(calc(1,2,3,4))

num = [1,2,3]
print(calc(*num))

def person(name, age, **kbw):
	print('name:', name, 'age:', age, 'other:', kbw)

person('Bom', 32)
person('Bom', 32, city='Beijing', job='Engineer')

extra = {'city':'Beijing', 'job':'Teacher'}
person('lskyo', 11, **extra)