from functions import *
from cryptography import *

# ----------------------------- Initialization -----------------------------
k = getKey()
p = k[0]
q = k[1]
N = p*q
phi = (p-1)*(q-1)
print('Initializations: \n\t p = {} \n\t q = {} \n\t N = {} \n\t Φ = {} \n'.format(p, q, N, phi))

# ----------------------------- generate e -----------------------------
e = eGenerator(phi)
print('Public Key: \n\t e = {} \n\t N = {} \n'.format(e, N))

# ----------------------------- generate d -----------------------------
d = inverseEuclid(phi, e)
print('Private Key:\n\t d = {} \n\t p = {} \n\t q = {} \n'.format(d, p, q))

# ----------------------------- Encryption -----------------------------
lastCharacterLength = encryption(e, N)

# ----------------------------- Decryption -----------------------------
decryption(lastCharacterLength, d, N)
