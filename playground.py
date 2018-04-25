# -*- coding: utf-8 -*-
import time
n = 21971
e = 131
d = 17867

message = "feeding"
encrypted_message = ""
decrypted_message = ""

start = time.time()
##########шифрование##########
for x in message:
    numerize = ord(x)
    encrypt = pow(numerize, e, n)
    denumerize = unichr(encrypt)
    encrypted_message += denumerize

print encrypted_message

##########Дешифрование##########
for t in encrypted_message:
    numerize = ord(t)
    decrypt = pow(numerize, d, n)
    denumerize = chr(decrypt)
    decrypted_message += denumerize
    
print decrypted_message
end = time.time()

print(end - start)

encrypted_message2 = ""
decrypted_message2 = ""
LUT_encryption = dict()
LUT_decryption = dict()

start = time.time()
##########второе шифрование##########
for x in message:
    if x in LUT_encryption:
        encrypted_message2 += LUT_encryption[x]
    else:
        numerize = ord(x)
        encrypt = pow(numerize, e, n)
        denumerize = unichr(encrypt)
        encrypted_message2 += denumerize
        LUT_encryption[x] = denumerize
        
print encrypted_message

##########расшифровка версии два##########
for t in encrypted_message2:
    if t in LUT_decryption:
        decrypted_message2 += LUT_decryption[t]
    else:
        numerize = ord(t)
        decrypt = pow(numerize, d, n)
        denumerize = chr(decrypt)
        decrypted_message2 += denumerize
        LUT_decryption[t] = denumerize

print decrypted_message

end = time.time()