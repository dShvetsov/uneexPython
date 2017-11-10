#!/usr/bin/env python3

# Ввести строку, содержащую произвольные символы (кроме символа «@»).
# Затем ввести строку-шаблон, которая может содержать символы @.
# Проверить, содержится ли в исходной строке подстрока, совпадающая со строкой-шаблоном везде, кроме символов @;
# на месте @ в исходной строке должен стоять ровно один произвольный символ.
# Вывести позицию в строке, с которой начинается эта подстрока или -1, если её там нет.
# Input:
#
# исходной строке подстрока, совпадающая со строкой
# ст@ок@
#
# Output:
#
# 9

not_found = -1
any_char = '@'

def check_word(subline, pattern):
    if len(subline) < len(pattern):
        return False
    for a, b in zip(subline, pattern):
        if a != b and b != any_char:
            return False
    return True

if __name__ == "__main__":
    line = input()
    pattern = input()

    subpat = pattern.split(any_char)
    first_pat = subpat[0]
    idx = 0
    while idx < len(line):
        idx = line.find(first_pat, idx)
        if idx == not_found:
            break
        elif check_word(line[idx::], pattern):
            break
        else:
            idx += 1
    else:
         idx = -1
    print(idx)

