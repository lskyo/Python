from types import MethodType
import time


class Student(object):
    __slots__ = ('name', 'age', 'set_age')
    pass


s = Student()
s1 = Student()
s.name = 'Mickael'
print(s.name)


def set_age(self, age):
    self.age = age


s.set_age = MethodType(set_age, s)
s.set_age(20)
print(s.age)

Student.set_age = set_age
s1.set_age(21)
print(s1.age)

s2 = Student()


# s2.score = 100
# print(s2.score)

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2018 - self._birth


stu = Student()
stu.score = 99
print(stu.score)
stu.birth = 1995
print(stu.age)


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name


print(Student("Michael"))


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a


for n in Fib():
    print(n)


class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


f = Fib()
print(f[1])
print(f[2])
print(f[3])
print(f[4])
print(f[5])
print(f[2:6])


class Student(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, item):
        if item == 'score':
            return 99
        if item == 'age':
            return lambda: 20


s = Student()
print(s.name)
print(s.score)
print(s.age())


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.abc.bbb)

class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print('My name is %s.' % self.name)

s = Student('Michael')
print(callable(s))
s()
