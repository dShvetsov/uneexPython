#!/usr/bin/python3

sequance = eval(input())

result = sequance[::2][::-1] + sequance[1::2]

print(result)
