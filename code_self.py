#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import functools

#================

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

#function map

def normalize(name):
    return name[0].upper() + name[1:].lower()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

print('\n')

#function map and reduce

def char2int(c):
    return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[c]

def qiuji(x, y):
    return x * 10 + y;

def str2int(s):
    return functools.reduce(qiuji, map(char2int,s))

print(str2int('123321'))

def str2float(s):
    p = s.index('.')
    return functools.reduce(qiuji, map(char2int,s[:p])) + functools.reduce(qiuji, map(char2int,s[p+1:]))/10**(len(s)-1-p)

print(str2float('1233.21'))

#=====filter==============

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0  # x?

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

for n in primes():
    if n <100:
        print(n)
    else:
        break

def is_palindrom(n):
    return str(n) == str(n)[::-1]

output = filter(is_palindrom, range(1, 1000))
print(list(output))

#====sorted=====

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

