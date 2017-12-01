# Написать класс Unary, реализующий единичную систему счисления. Палочное представление L числа N
#
#     создаётся из любой строки длиной N
#         представляется в виде строки из N символов "|"
#             имеет длину N
#                 можно пройти циклом (при этом N раз возвращается палочная единица)
#
#         можно дополнить другим палочным числом K с помощью L |= K (при этом длина L увеличивается на длину K)
#
#         можно поделить пополам нацело с помощью ~L (лишняя палка исчезает)
#
#         можно дополнить одной палкой с помощью +L
#
#         Во всех случаях изменения числа идентификатор объекта сохраняется. Унарныеоперации не только изменяют объект, но и возвращают его.
#         Input:
#
#         Toggle line numbers
#
#            1 a = Unary("||")
#               2 b = Unary("||||")
#                  3 print(a, b)
#        4 a |= b
#           5 print(a)
#        6 print(~a)
#        7 for c in a:
#           8     print("  ",c)
#              9     print(". ",+c)
#                10     print("..",+c)
#                  11 ~a
#                    12 ~a
#                      13 print("Error" if a else a is a)
#
#                      Output:
#
#                      || ||||
#                      ||||||
#                      |||
#                         |
#                         .  ||
#                         .. |||
#                            |
#                            .  ||
#                            .. |||
#                               |
#                               .  ||
#                               .. |||
#                               True

class Unary:
    def __init__(self, s):
        assert(type(s) is str)
        n = len(s)
        assert(n == s.count('|'))
        self.n = n

    def __str__(self):
        return "".join("|" for i in range(self.n))

    def __repr__(self):
        return "".join("|" for i in range(self.n))

    def __len__(self):
        return self.n

    def __iter__(self):
        return iter( Unary('|') for i in range(self.n) )

    def __ior__(self, other):
        self.n += other.n
        return self

    def __invert__(self):
        self.n //= 2
        return self

    def __pos__(self):
        self.n += 1
        return self
