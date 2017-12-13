# Задать три класса — A, B и C, свойства которых неизвестны, но для которых верен пример.
# Input:
#
# Toggle line numbers
#
#    1 a, b, c, d = A(2), B(3), C(4), C("Op")
#    2 print(a,b,c, a+b+c, a*b*c, a*b*d)
#    3 print(*(o+p for o in (a,b,c) for p in (a,b,c) if not o==b==p))
#    4 print(*(o*p for o in (a,b,c,d) for p in (a,b,c,d) if not o==a==p and not o==d==p))
#    5 print(*(isinstance(e,T) for e in (a,b,c) for T in (A,B,C)))
#    6 print(*(a in T.__dict__.keys() for a in ('__add__','__mul__','__str__') for T in (A,B,C)))
#
# Output:
#
# /2/ |3| |4| /9/ |24| |OpOpOpOpOpOp|
# /4/ /5/ /6/ /5/ |7| |6| |7| |8|
# |6| |8| |OpOp| |6| |9| |12| |OpOpOp| |8| |12| |16| |OpOpOpOp| |OpOp| |OpOpOp| |OpOpOpOp|
# True False False False True False True True True
# True False False False True False True True False

class A:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return type(self)(self.value + other.value)

    __radd__ = __add__

    def __str__(self):
        return "/{}/".format(self.value)

class B:
    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        return type(self)(self.value * other.value)

    __rmul__ = __mul__

    def __str__(self):
        return "|{}|".format(self.value)

class C(B, A):
    pass
