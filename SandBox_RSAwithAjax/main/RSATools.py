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


def Get_Private_Key(p, q, n):
    totient = (p-1)*(q-1)
    for i in range(0, n):
        if ((i * totient)+1) % n == 0:
            print("Found private key ")
            print("on iteration ", i)
            return ((i * totient)+1)//n
        
def ModuloExponent(base, exponent, modulus):
    if modulus == 1:
        return 0
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent //= 2
        base = (base*base) % modulus
    return result

