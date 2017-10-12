from math import sqrt

def isAnyPower(n):
    sqrt_n = int(sqrt(n))
    for base in range(2, n):
        for exponent in range(2, sqrt_n):
            compared_value = base ** exponent
            if compared_value == n:
                return True
            elif compared_value > n:
                break
    return False

n = eval(input())

print ("YES" if isAnyPower(n) else "NO")
