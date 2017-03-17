#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#=======生成器==========

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

