f = open('./IO Test File', 'r')
print(f.read())
f.close()


with open('./IO Test File', 'r') as f:
    print(f.read(10 * 1024))

with open('./IO Test File', 'r') as f:
    for line in f.readlines():
        print(line.strip()) # 把末尾的'\n'删掉

with open('./IO Test File', 'r') as f:
    print(f.readlines())
