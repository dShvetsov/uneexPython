#!/usr/bin/env python3

def GenTriseq(v):
    for i in v:
        less_than_i = filter(lambda x : i >= x, v)
        for j in less_than_i:
            yield j

v = eval(input())
n = eval(input())

new_seq = list(GenTriseq(v))
print(new_seq[n] if n < len(new_seq) else "NO")
