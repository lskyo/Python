import types


class Student(object):
    pass


print(Student)
print(Student())


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print(self.name, ':', self.score)

    def get_grade(self):
        if self.score >= 90:
            print('A')
            return 'A'
        elif self.score >= 60:
            print('B')
            return 'B'
        else:
            print('C')
            return 'C'


student = Student('lskyo', 60)
print(student.name, ":", student.score)
student.print_score()
student.get_grade()


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def print_score(self):
        print('%s : %s' % (self.__name, self.__score))


student2 = Student('Roli', 90)
student2.print_score()
print(student2.get_name())
student2.set_score(99)
print(student2.get_score())
student2.__score = 10
print(student2._Student__score)
print(student2.__score)


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def eat(self):
        print('Dog is eating...')

    def run(self):
        print('Dog is running...')

    def __len__(self):
        return 100


class Cat(Animal):
    pass


animal = Animal()
dog = Dog()
cat = Cat()

animal.run()
dog.run()
dog.eat()
cat.run()

print(isinstance(dog, Cat))
print(isinstance(dog, Dog))
print(isinstance(dog, Animal))


def animal_run(arg):
    arg.run()


animal_run(dog)
animal_run(animal)

print(type(dog))
print(type(animal_run) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))
print(dir(dog))
print(len(dog))


class MyObject(object):

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()
print(hasattr(obj, 'x'))
print(hasattr(obj, 'power'))
print(hasattr(obj, 'y'))
obj.y = 10
print(hasattr(obj, 'y'))
print(getattr(obj,'y'))
fn = getattr(obj, 'power')
print(fn())



class Teacher(object):
    name = 'TeacherName'

tea = Teacher()
print(Teacher.name)
print(tea.name)
tea.name = '123'
print(tea.name)
print(Teacher.name)
Teacher.name = '456'
print(tea.name)
print(Teacher.name)
del tea.name
print(tea.name)