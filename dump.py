import pickle
import json

d = dict(name='Bob', age=20, score=90)
dumps = pickle.dumps(d)
print(dumps)
loads = pickle.loads(dumps)
print(loads)

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('dump.txt', 'rb')
print(f.read())
f.seek(0)
load = pickle.load(f)
print(load)
f.close()


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


s = Student('lskyo', 22, 90)
print(json.dumps(s, default=student2dict))
print(json.dumps(s, default=lambda obj: obj.__dict__))
json_str = '{"name": "lskyo", "age": 22, "score": 90}'
print(json.loads(json_str, object_hook=dict2student))

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False)
print(s)