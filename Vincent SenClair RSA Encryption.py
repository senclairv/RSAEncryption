#Vincent SenClair
#RSA Encryption and Decryption

import random
import math

def egcd(a, b):
    
    if a == 0:
        return (b, 0, 1)
    
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    
    g, x, y = egcd(a, m)
    return x % m

def candidates(n):

    a = []
    for i in range(100):
        p = random.randint(n, 10*n)
        if p%2 is not 0 and p%3 is not 0 and p%5 is not 0 and p%7 is not 0 and p%11 is not 0:
            a.append(p)

    return a

def checkPrime(p):

    check = True
    
    for i in range(100):
        x = random.randint(1, math.ceil(pow(p, 0.5)))
        if(pow(x, p-1, p) != 1):
            check =  False

    if(check):
        return True

    else:
        return False

def candi(n):

    candi = candidates(n)

    for num in candi:
        if(checkPrime(num) is False):
            candi.remove(num)

    return candi

def createPublicKey(P, Q):

    n = P * Q
    fn = (P - 1) * (Q - 1)

    e = random.randint(1, fn)
    while(math.gcd(e, fn) is not 1):
        e = random.randint(1, fn)

    return e, n, fn

def createPrivateKey(E, FN):

    d = modinv(E, FN)
    return d

def encryptMessage(plaintext, E, N):
    
    cipher = [(ord(char) ** E) % N for char in plaintext]
    return cipher

def decryptMessage(ciphertext, D, N):
    
    plain = [chr((char ** D) % N) for char in ciphertext]
    return ''.join(plain)
    
def main():

    candidateList = candi(100)
    
    while(len(candidateList) < 2):
        candidateList = candi()

    P = random.choice(candidateList)
    candidateList.remove(P)
    Q = random.choice(candidateList)

    E, N, FN = createPublicKey(P, Q)

    D = createPrivateKey(E, FN)

    message = input("Enter a message: ")
    
    encryptedMessage = encryptMessage(message, E, N)

    print("Encrypted Message: ", encryptedMessage)
    
    decryptedMessage = decryptMessage(encryptedMessage, D, N)

    print("Re-Decrypted Message: ", decryptedMessage)
    

main()
