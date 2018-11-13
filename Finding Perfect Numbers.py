#Owing to their form, 2^(p−1)((2^p) − 1), every even perfect number is represented in binary as p ones followed by p − 1  zeros

#so

numberofperfectnumbers = int(input("To what arbitrary degree do you want to search to?"))

#Prime Number Calculator
from math import sqrt

limit = numberofperfectnumbers ** 2
print(limit)

def findprimes(limit):
    while True:
        primes = [2]
        for num in range(3, limit, 2):
            isprime = True
            for x in primes:
                if (num / x) % 1 == 0:
                    isprime = False
                    break
                if x >= (int(sqrt(num) // 1) + 1):
                    break
            if isprime:
                primes.append(num)
        break
    return primes

primes = findprimes(limit)

print("Primes =", primes)
#Binary representation convert


#LucasLehmer test - for Mersenne numbers

def LucasLehmer(prime):
    LL = 4
    Mp = (2**prime) - 1
    for x in range(prime - 2):
        LL = (((LL ** 2) - 2)% Mp)
    if LL == 0:
        print(Mp * (2**(prime - 1)), Mp, prime)
    return LL==0

binary = [6] #Lucas-Lehmer does not work for prime = 2

print("\nPerfect Number, Mersenne Prime, Prime Power")
print(6, 3, 2)
for x in primes:
    if LucasLehmer(x):
        binary.append(((2**x) - 1)*(2**(x - 1)))
