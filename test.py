def f1(n):
    i = 3
    while True:
        i *= 2
        if i > n:
            return i


def f2(num):
    cnt = 0
    while True:
        num /= 2
        cnt += 1
        if num < 5:
            return cnt


print(f1(f2(20))*f2(f1(20)))
