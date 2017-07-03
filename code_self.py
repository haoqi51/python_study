
# -*- coding: UTF-8 -*-

import functools
import study_module

#生成器yield

def fib():
    n, a, b = 0, 0, 1
    while True:
        yield(b)
        a, b = b, a+b
    return 'done'

L = fib()
L = [next(L) for i in range(15)]
print(L)

print('\n')

def yanghui():
    L = [1]
    while True:
        yield(L)
        L.append(0)
        L = [L[i-1]+L[i] for i in range(len(L))]

n = 0
for t in yanghui():
    print(t)
    n = n+1
    if n == 10:
        break
print('\n')

#function map map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def normalize(name):
    return name[0].upper() + name[1:].lower()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

print('\n')

#reduce 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
#function map and reduce

def char2int(c):
    return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[c]

def qiuji(x, y):
    return x * 10 + y

def str2int(s):
    return functools.reduce(qiuji, map(char2int,s))

print(str2int('123321'))

def str2float(s):
    p = s.index('.')
    return functools.reduce(qiuji, map(char2int,s[:p])) + functools.reduce(qiuji, map(char2int,s[p+1:]))/10**(len(s)-1-p)

print(str2float('1233.21'))

#filter函数，根据筛选器返回True还是False决定保留还是丢弃该元素
#从3开始的奇数序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

#lambda x: x % n > 0 为匿名函数
def _not_divisible(n):
    return lambda x: x % n > 0
'''
def _not_divisible(n,x):
    return x % n > 0
'''

#素数生成器
def primes():
    yield 2
    it = _odd_iter() #定义it是一个从3开始的奇数序列
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

for n in primes():
    if n <20:
        print(n)
    else:
        break

#回数 
def is_palindrom(n):
    return str(n) == str(n)[::-1]

output = filter(is_palindrom, range(1, 100))
print(list(output))

#sorted 排序，
#参数key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序
#参数reverse=True，反向排序
L = [36, 5, -12, 9, -21]

L2 = sorted(L)
print(L2)

L2 = sorted(L, key = abs)
print(L2)

L2 = sorted(L, key = abs, reverse=True)
print(L2)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]

def by_score(t):
    return t[1]

L2 = sorted(L, key=by_name)
print(L2)

L2 = sorted(L, key=by_score, reverse=True)
print(L2)

#获取函数名
print(sorted.__name__)

#返回函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 3, 5, 7, 9) #此时f为sum函数
print(f)
sum = f()
print(sum)

#闭包
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1==f2)

# 返回闭包时牢记的一点就是：
# 返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

# 如果一定要引用循环变量怎么办？
# 方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

# 装饰器
'''
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
'''

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2016-3-20')
now()
print(now.__name__)

# 带参数的装饰器
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('excute')
def now1():
    print('2017-5-23')
now1()
print(now1.__name__)

study_module.test()
