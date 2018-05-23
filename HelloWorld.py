print('hello, world')
print('I am', 'lskyo')
print("100 + 1 = ", 100+1)
# name = input("Please input your name:")
# print('Hello!' + name)
A = 100
a = 101
print('A == a :', A == a )
print("Are you \"OK\"?")
print('I\' am "ok"')
print('\\\t\\')
print('''b
o
o
m''')
# c = int(input("please input c(int):"))
# print(type(c))
# if c > 100 :
# 	print("c > 100")
# else:
# 	print("c <= 100")
print('10 / 3 =', 10/3)
print('10 // 3 =', 10 // 3)
print('10 % 3 =', 10%3)
print('中文str')
print(ord('中'))
print(chr(25991))
print(b'ABC')
print('中文'.encode('utf-8'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print(len('中文'))
print(len('中文'.encode('utf-8')))
print('%d is good' % 100)
print('%03d is good ,but %.2f is bad' % (1, 3.151))
print('%.2f%%' % 20.291)
print('{0} rate {1:.1f}%'.format('boom',2.139))
classmates = ['Michael', 'Bob', "Rob"]
print(classmates)
print(classmates[0])
print(classmates[-1])
print(len(classmates))
classmates.append('Mike')
print(classmates)
classmates.insert(2, 'Luci')
print(classmates)
print(classmates.pop())
print(classmates.pop(0))
mylist = ['Mike', 123, True, ['newList', 321]]
print(mylist)
mytuple = (1,)
print(mytuple)
mtuple = (1, True, 'MTuple', ["H", "MT"])
print(mtuple)
mtuple[3].append(2)
print(mtuple)

age = 28
if age >= 20:
	print('too old!')
elif age >= 18:
	print('good!')
else:
	print('better!')

if mytuple:
	print(mytuple)

if mylist:
	print(mylist)

for x in range(10):
	if x > 2:
		break
	print(x)

n = 99
sum = 0
while n > 0:
	sum += n
	n -= 1
	if n < 90:
		break
print(sum)

for x in range(10):
	if(x % 2 == 0):
		continue
	print(x)

dictionary = {'Tom':60, 'Mike':80, 'Rob':100}
print(dictionary)
print('Rob :', dictionary['Rob'])
dictionary['lskyo'] = 10000
print(dictionary)
if 'Bom' in dictionary:
	print(dictionary['Bom'])
else:
	dictionary['Bom'] = 10
print(dictionary)
print(dictionary.get('Luci', -1))
print(dictionary.pop('Rob'))
print(dictionary)

s1 = set([1,2,3,1,2,3,'T'])
print(s1)
s1.add(4)
print(s1)
s1.remove(1)
print(s1)

s2 = set([3,4,5])
print(s1 & s2)
print(s1 | s2)