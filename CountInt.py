#!/usr/bin/end python3

obj = eval(input())

count = 0
for field in dir(obj):
    is_int = type(getattr(obj, field)) is int
    count += 1 if is_int else 0

print(count)
