# Реализовать с помощью дескрипторов абстракцию «простой семафор», используемую при разделении некроторого ресурса.
# При обращении к семафору либо происходит захват ресурса (семафор взводится),
# либо возвращается объект, который этот ресурс захватил.
# Взведённый семафор может сбросить только объект, который его захватил.
# Input:
#
# Toggle line numbers
#
#    1 a, b = Sem("A"), Sem("B")
#    2 print("Locked:",a.lock) # A взводит опущенный семафор
#    3 print("Locked:",a.lock) # Семафор взведён A
#    4 print("Locked:",b.lock) # Семафор взведён A
#    5 del(b.lock)             # B пытается сбросить семафор
#    6 print("Locked:",b.lock) # Семафор взведён A
#    7 print("Locked:",a.lock) # Семафор взведён A
#    8 del(a.lock)             # А сбрасывает семафор
#    9 print("Locked:",b.lock) # B взводит опущенный семафор
#   10 print("Locked:",a.lock) # Семафор взведён B
#
# Output:
#
# Locked: None
# Locked: <A>
# Locked: <A>
# Locked: <A>
# Locked: <A>
# Locked: None
# Locked: <B>

class semaphore:
#owner = None
    def __init__(self):
        self.owner = None

    def __get__(self, obj, cls):
        if self.owner is not None :
            return "<{}>".format(self.owner.name)
        self.owner = obj

    def __delete__(self, obj):
        if obj is self.owner:
            self.owner = None

class Sem:
    lock = semaphore()

    def __init__(self, name):
        self.name = name
