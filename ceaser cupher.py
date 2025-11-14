"""ord(char) gives the unicode of the specific zharacter
65 is unicode for A
97 is unicode for a
chr(123) gives the character corresponding to the unicode 123"""


    
def encrypt_messages(text,step):
    encrypt_messages=""
    for char in text:
        if char.isupper():
            encrypt_messages+=chr((ord(char)+step-65)%26+65)
        elif char.islower():
            encrypt_messages+=chr((ord(char)+step-97)%26+97)
        else:
            encrypt_messages+=char
    return encrypt_messages
    

    
def decrypt_messages(text,step):
    decrypt_messages=""
    for char in text:
        if char.isupper():
            decrypt_messages+=chr((ord(char)-step-65)%26+65)
        elif char.islower():
            decrypt_messages+=chr((ord(char)-step-97)%26+97)
        else:
             decrypt_messages+=char
    return decrypt_messages

def ceaser_cypher():
    choose=input("Enter 'Encrypt' to encrypt and 'Decrypt' to decrypt: \n")
    text=input("enter the message: \n")
    step=int(input("enter the step: \n"))
    if choose=="Encrypt":
        print(f"Encrypted Message: \n{encrypt_messages(text,step)}")
    elif choose=="Decrypt":
        print(f"Decrypted Message: \n{decrypt_messages(text,step)}")
    else:
         print("INVALID INPUT")

ceaser_cypher()