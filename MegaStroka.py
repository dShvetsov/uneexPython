#!/usr/bin/env bash

# Написать класс Stroka, унаследованииый от str, экземпляр которого s дополнительно поддерживает следующие операции:
#
#     объект типа Stroka, содержащий символы s в обратном порядке: -s
#
#     объект типа Stroka, содержащий все пары символов из объектов s и t в порядке следования — s*t (t может быть просто строкой)
#
#     объект типа Stroka, равный s*s*…(n-1 раз)…*s — s**n (s**0 — пустая Stroka)
#
# Input:
#
# Toggle line numbers
#
#    1 a, b, c, d = Stroka("wer"), Stroka("ASDF"), Stroka("12"), Stroka(":,")
#    2 print(a+b)
#    3 print(c*4)
#    4 print(b[2:])
#    5 print(a*b)
#    6 print(c**3)
#    7 print(a*c*d)
#
# Output:
#
# werASDF
# 12121212
# DF
# wAwSwDwFeAeSeDeFrArSrDrF
# 11121112111221222122111221222122
# w:w,1:1,w:w,2:2,e:e,1:1,e:e,2:2,r:r,1:1,r:r,2:2,

class Stroka( str ):
    def __neg__(self):
        return type(self)(self[::-1])

    def __mul__(self, other):
        if isinstance(other, str):
            return type(self)("".join((i+j) for i in self for j in other))
        else:
            return str.__mul__(self, other)

    def __pow__(self, n):
        res = type(self)("")
        for i in range(n):
            res = res * self if res != '' else  self
        return res

