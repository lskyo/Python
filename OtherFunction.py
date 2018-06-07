import functools

a = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(a)


def now():
    print('2018-06-07')


f = now
f()
print(now.__name__)
print(f.__name__)


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2018-06-07')


now()


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s()' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log('excute')
def now():
    print('2018-06-07')


now()
print(now.__name__)

b = int('12345', base=8)
print(b)


def int2(x, base=2):
    return int(x, base)


print(int2('1000000'))
print(int2('1000000', 10))

int8 = functools.partial(int, base=8)
print(int8('1235'))

kw = { 'base': 2 }
print(int('10010', **kw))

args = (10,29,12,40)
print(max(*args))
