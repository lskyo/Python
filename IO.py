from io import StringIO
from io import BytesIO

f = open('./IO Test File', 'r')
print(f.read())
f.close()


with open('./IO Test File', 'r') as f:
    print(f.read(10 * 1024))

with open('./Write Test', 'w') as f:
    f.write('Hello world!')

with open('./Write Test', 'r') as f:
    for line in f.readlines():
        print(line.strip()) # 把末尾的'\n'删掉

with open('./Write Test', 'a') as f:
    f.write('Hello world!')

with open('./Write Test', 'r', encoding='utf-8') as f:
    print(f.readlines())


f = StringIO()
print(f.write('Hello'))
print(f.write(' World!'))
print(f.getvalue())

f = StringIO('Hello!\nI am lskyo!\nGoodbye!')
s = f.readline()
while s:
    print(s)
    s = f.readline()

f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
print(f.getvalue().decode('utf-8'))