from secrets import SystemRandom
from algorithms import sqm

#  USED FOR SECURE NUMBER GENERATION
crypto_gen = SystemRandom()

#  PUBLIC PARAMETERS
p = crypto_gen.getrandbits(128)
alpha = crypto_gen.getrandbits(128)

#  MAKE SURE ALPHA IS A GENERATOR AND SMALLER THAN p
while alpha > p and sqm(alpha, int((p - 1) / 2), p) != 1:
    if not sqm(alpha, p - 1, p) == 1:
        alpha = crypto_gen.getrandbits(128)

#  PRIVATE KEY GENERATING
a = crypto_gen.randrange(2, p - 2)  # KEY a
b = crypto_gen.randrange(2, p - 2)  # KEY b

#  PUBLIC KEYS
K_pub_A = sqm(alpha, a, p)  # KEY A
K_pub_B = sqm(alpha, b, p)  # KEY B

#  SHARED KEY (SECRET)
K_ab = sqm(K_pub_B, a, p)

#  CHECK SHARED KEY
if not K_ab == sqm(K_pub_A, b, p):
    print("[FATAL ERROR] Shared key's are not matching")
else:
    print(f"[PUBLIC] p = ({hex(p)}), alpha = ({hex(alpha)})")
    print(f"[PRIVATE EXCHANGED] {hex(K_ab)}")
    print("\n[SECURE] key's are exchanged and match")
