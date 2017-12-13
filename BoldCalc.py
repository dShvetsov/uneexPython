#!/usr/bin/env python3

# Написать программу — калькулятор с переменными и обработкой ошибок Команда, начинающаяся на '#' — комментарий
#
# Команда вида Переменная=выражение задаёт переменную
#
# Команда вида выражение выводит значение выражения.
# Если команда содержит знак "=", но не является присваиванием, выводится диагностика "invalid assignment" (см. пример)
# Если слева от "=" находится не идентификатор, выводится диагностика "invalid identifier (см. пример)"
# В случае любых других ошибок выводится текст ошибки.
#
# «Выражение» — это произвольное выражение Python3, в котором вдобавок можно использовать уже определённые переменные (и только их).
# Пробелов в командах нет. Пустая команда означает конец вычислений.
# Калькулятор вводит и исполняет команды по одной, тут же выводя диагностику,
# но в тестах это выглядит как ввод последовательности строк и вывод последовательности строк.
#     Input:
#
#     42
#     100500//33
#     "Qq!"*(6-2)
#     # Здесь ошибка
#     3,,5
#     10/(8-8)
#     "wer"[2]+"qwe"[1]
#     "wer"[7]+"qwe"[9]
#     1+(2+(3
#     a0=5
#     b0=7
#     # И здесь ошибка
#     12N=12
#     # И ещё где-то были
#     a0+b0*8
#     c=b0//2+a0
#     d==100
#     c+d
#     sorted(dir())
#
#     Output:
#
#     42
#     3045
#     Qq!Qq!Qq!Qq!
#     invalid syntax (<string>, line 1)
#     division by zero
#     rw
#     string index out of range
#     unexpected EOF while parsing (<string>, line 1)
#     invalid identifier '12N'
#     61
#     invalid assignment 'd==100'
#     name 'd' is not defined
#     ['__builtins__', 'a0', 'b0', 'c']
#
#

import sys

class InvalidAssigment(Exception) : pass
class InvalidIdentifier(Exception) : pass

def main():
    global line, expr, identifier, global_builtins
    __builtins__ = global_builtins
    for line in sys.stdin:
        line = line.strip()
        try:
            if not line.startswith('#') and len(line) > 0:
                expr = line.split('=')
                if len(expr) == 1 : print(eval(line))
                elif len(expr) == 2 :
                    identifier = expr[0].strip()
                    if not identifier.isidentifier() : raise InvalidIdentifier(identifier)
                    locals()[identifier] = eval(expr[1])
                else : raise InvalidAssigment(line)
        except InvalidIdentifier as ii:
            print ("invalid identifier '{}'".format(ii))
        except InvalidAssigment as ia:
            print ("invalid assignment '{}'".format(ia))
        except Exception as e:
            print (e)

global_builtins = __builtins__
if __name__ == '__main__':
    __name__='builtins'
    main()
