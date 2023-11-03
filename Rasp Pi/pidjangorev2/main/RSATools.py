import random #Needed for RSA cryptography

def Eulers_GCD(a, b):
    r = a % b
    q = a//b
    while r != 0:
        a = b
        b = r
        q = a//b
        r = a - b*q
    return b

def miller_rabin(n, k):

    if n == 2 or n == 3:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def nextprime(n):
    while miller_rabin(n, 40) == False:
        n += 1
    return n

