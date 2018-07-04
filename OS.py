import os
import shutil
print(os.name)
for k in os.environ:
    print(k, ':', os.environ[k])

abspath = os.path.abspath('.')
print(abspath)
mydir = os.path.join("G:\\", 'mydir')
print(mydir)
# os.mkdir(mydir)
# os.rmdir(mydir)

print(os.path.split(abspath))
print(os.path.splitext('/path/to/file.txt'))

# os.rename('test.txt', 'test.py')
# os.remove('test.py')

for x in os.listdir('.'):
    if os.path.isdir(x):
        print(x)

shutil.copyfile('./IO Test File', './abc')
with open('./abc', 'r') as f:
    print(f.read())

for x in os.listdir('.'):
    if os.path.isfile(x) and os.path.splitext(x)[1] == '.py':
        print(x)