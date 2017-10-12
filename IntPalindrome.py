n = eval(input())
work = n
reverse_n = 0

while(work != 0):
    reverse_n *= 10
    reverse_n += work % 10
    work //= 10

print ("YES" if reverse_n == n else "NO")
