import secrets
import math
import random
import os
clear = lambda: os.system('cls')

# ------------------------------------- Generate P & Q -------------------------------------
def getKey():
    print('Please enter type of key')
    print('1- Use default 32 bits to generate p & q')
    print('2- Choose length of byte to generate p & q')
    print('3- Manual insert p & q')
    typeOfKey = input()
    clear()

    if typeOfKey == '3':
        # if p&q recieved from user
        p = int(input('Insert p: '))
        q = int(input('Insert q: '))
        clear()
        return p,q

    elif typeOfKey == '2':
        # if spicific number of bytes recieved from user
        # guarantee a large number in range [(2**k)-1 , 2**k]
        byteLength = int(input('Insert length of bytes: '))
        numberOfBits = (byteLength*8)
        p = generateRandomPrime(numberOfBits)
        q = generateRandomPrime(numberOfBits)
        clear()
        return p,q

    else:
        # default case
        numberOfBits = 32
        p = generateRandomPrime(numberOfBits)
        q = generateRandomPrime(numberOfBits)
        clear()
        return p,q

# ------------------------------------- Generate a random prime P or Q -------------------------------------
def generateRandomPrime(numberOfBits):
    # find a random prime in spicified range
    while True:
        chosenValue = secrets.choice(range((2**(numberOfBits-1)), (2**numberOfBits)))
        if checkPrimality(chosenValue):
            return chosenValue

# ------------------------------------- Check Primality -------------------------------------
def checkPrimality(num):
    # check whether the input number is random or not
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            return False
    return True

# ------------------------------------- calculate Greatest Common Divisor -------------------------------------
def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a%b)

# ------------------------------------- generate e -------------------------------------
def eGenerator(phi):
    # for every possible value between [2, phi-1]
    maximumPeriod = 0
    primitiveRoots = []
    for num in range(2,phi-1):
        # if GCD == 1, then check primitiveRoot
        if GCD(phi, num) == 1:
            # calculate periodic range powers of num
            periodicVector = []
            pow = 1
            while True:
                # compute different powers of num
                currentValue = fastExponentiation(num, pow, phi)
                if currentValue not in periodicVector:
                    periodicVector.append(currentValue)
                    pow += 1

                else:
                    # if we found greater cycle length, we should replace it
                    if pow > maximumPeriod:
                        maximumPeriod = pow
                        primitiveRoots = [num]
                    # if it has same length cycle, we should save it
                    elif pow == maximumPeriod:
                        primitiveRoots.append(num)
                    # otherwise if it has shorter period length we ignore it
                    break

    # Here we have access to a range of possibleAnswers, that we have to choose random
    print('\nPossible Primitive Roots:\n{}'.format(primitiveRoots))
    print('\nMaximum Period of Primitive Roots:\n{}\n'.format(maximumPeriod-1))

    return random.choice(primitiveRoots)

# ------------------------------------- generate e -------------------------------------
def eGeneratorSimple(phi):
    while True:
        # choose random in range [3, phi) step by 2
        chosenValue = random.randrange(2,phi)
        if GCD(phi, chosenValue) == 1:
            return chosenValue

# ------------------------------------- inverse calculator -------------------------------------
def inverseEuclid(m, b):
    A = [1, 0, m]
    B = [0, 1, b]

    while True:
        if B[2] == 1:
            break

        Q = A[2] // B[2]
        T = [ A[0]-Q*B[0], A[1]-Q*B[1], A[2]-Q*B[2] ]
        A = [ B[0], B[1], B[2] ]
        B = [ T[0], T[1], T[2] ]

    # ensure positiveness
    if B[1] < 0:
        return B[1] + m
    else:
        return B[1]

# ------------------------------------- Fast Exponentiation -------------------------------------
def fastExponentiation(base, pow, modulus):
    result = 1
    base %= modulus
    while pow >= 1:
        if pow % 2 == 1:
            result *= base
        pow //= 2
        base *= base
        base %= modulus
        result %= modulus

    return result
