import math

def primeNumberDetector(n):
    if n < 2:
        return False
    elif n < 4:
        # 2 and 3 are prime
        return True
    elif (n % 6) in (0,2,3,4):
        # must be divisible by 2 or 3
        return False
    else:
        limit = int(math.sqrt(n))+1
        for i in range(5,limit,6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

def primeNumberPrinter(text):
    # collect candidate numbers
    nums = []
    # walk along the original string
    for start in range(len(text)):
        # extend possible string one char at a time
        for end in range(start + 1, len(text) + 1):
            if text[start:end].isdigit():
                # if it's a valid number
                a = int(text[start:end])
                # see if it's a prime: if so, remember it
                if primeNumberDetector(a): 
                    nums.append(a)
            else:
                # short circuit as soon as end gets to end of string 
                # or it's no longer a digit
                break

    # return the list of primes
    return nums
print(primeNumberDetector(17))
print(primeNumberPrinter("17989"))


output:
True
[17, 1789, 7, 89]
