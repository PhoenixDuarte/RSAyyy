message= ""
e=0
n=0
d=0        

encrypted_message= ""
decrypted_message= ""
endictcryption  = dict()
dictcryption = dict()

def encrypt(e, n):
    encrypted_message= ""
    e= int(input('Please enter a value in for e:'))
    print("e =", e)
    n= int(input('Please enter a value for n:'))
    print("n =", n)
    message= input("Please enter the message you would like to encrypt:")
    for x in message:
      if x in endictcryption:
       encrypted_message += endictcryption[x]
      else:
        numerize= ord(x)
        encrypt = pow(numerize, e, n)
        denumerize = chr(encrypt) 
        encrypted_message += denumerize 
        endictcryption[x] = denumerize
    print ("Your encrypted message is:", encrypted_message)

def decrypt(d, n):
    decrypted_message= ""
    d= int(input('Please enter a value in for d:'))
    print("d =", d)
    n= int(input('Please enter a value for n:'))
    print("n =", n)
    encrypted_message= input("Please enter the message you would like to decrypt:")
    for t in encrypted_message:
      if t in dictcryption:
        decrypted_message += dictcryption[t]
      else:
        numerize = ord(t)
        decrypt = pow(numerize, d, n)
        denumerize = chr(decrypt)
        decrypted_message += denumerize
        dictcryption[t] = denumerize
    print ("Your decrypted message is:", decrypted_message)

def start():
  whatdo = 0
  print("Welcome to the Cool™ Encryption and Decryption Program [With cool exit feature!]")
  command = input("Please select what you'd like to do: encrypt, decrypt, or exit.")
  while (whatdo != 1):
    if command == "encrypt" or command == "Encrypt":
      encrypt(e, n)
      command = input("Please select what you'd like to do: encrypt, decrypt, or exit.")
    elif command == "decrypt" or command == "Decrypt":
      decrypt(d, n)
      command = input("Please select what you'd like to do: encrypt, decrypt, or exit.")
    elif command == "exit" or command == "Exit":
      whatdo = 1
    else:
      print ("You dummmy. Please write in a proper answer.")
      command = input("Please select what you'd like to do: encrypt, decrypt, or exit.")
  print ("Thank you for using our program, have a great day!")
