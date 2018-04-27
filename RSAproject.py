message= ""
e=0
n=0
d=0        
decrypted_message= ""

#def start():
  #print("Welcome to the Cool™ Encryption and Decryption Program [With cool exit feature!]")
  #whatdo = input("Please select what you'd like to do: encrypt, decrypt, or exit.")
  #while whatdo != "exit"

def encrypt(e, n):
    encrypted_message= ""
    e= int(input('Please enter a value in for e:'))
    print("e =", e)
    n= int(input('Please enter a value for n:'))
    print("n =", n)
    message= input("Please enter the message you would like to encrypt:")
    for x in message:        
        numerize= ord(x)
        encrypt = pow(numerize, e, n)
        denumerize = chr(encrypt) 
        encrypted_message += denumerize   
    print ("Your encrypted message is:", encrypted_message)
    
def decrypt(d, n):
    decrypted_message= ""
    d= int(input('Please enter a value in for d:'))
    print("d =", d)
    n= int(input('Please enter a value for n:'))
    print("n =", n)
    encrypted_message= input("Please enter the message you would like to decrypt:")
    for t in encrypted_message:        
      numerize = ord(t)
      decrypt = pow(numerize, d, n)
      denumerize = chr(decrypt)
      decrypted_message += denumerize
    print ("Your decrypted message is:", decrypted_message)