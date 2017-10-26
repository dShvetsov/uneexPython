#!/usr/bin/env python3

def GenTriseq(v):
    for i in v:
        less_than_i = filter(lambda x : i >= x, v)
        for j in less_than_i:
            yield j

v = eval(input())
n = eval(input())

for i,elem in enumerate(GenTriseq(v)):
    if i == n:
        print (elem)
        break
else:
    print("NO")
