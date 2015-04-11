
fib = [0, 1]

def countDig(n):
    num = 0
    if n == 0:
        return 1
    while n > 0:
        n /= 10
        num += 1
    return num

def sumDigit(x):
    sum = 0
    while x:
        sum, x = sum + x % 10, x / 10
    return sum

def fibListCheck(n):
    i = 0
    while countDig(i) < n:
        fib.append(fib[-1] + fib[-2])
        i = fib[-1]
    return sumDigit(i)

print fibListCheck(500000)

