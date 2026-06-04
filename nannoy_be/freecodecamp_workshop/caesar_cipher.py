def caesar(text , shift, encrypt=True): 
    if not isinstance(text , str) or not isinstance(shift,int):
        return "error"
    if shift < 1 or shift > 25 : 
        return "Error, shift must be an integer between 1-25" 

    if not encrypt :
        shift = -shift     

    encrypted_text = ""    

    for i in text : 
        if i.isalpha(): 
            if i.isupper():
              base = ord('A')
            else :  
                base = ord('a')      
            #formula such that it convert to 0–25 range

            position = ord(i) - base
            shifted_text = (position + shift)%26   #if z = 26 and shift = 6 , the output should be f .
            encrypted_text += chr(shifted_text + base) 
        else : 
            encrypted_text += i     
    return encrypted_text

"""testing Github"""    

def encrypt(text,shift):
    return caesar(text, shift)

def decrypt(text,shift) :      
    return caesar(text,shift,encrypt =False)

encrypted_text = input("Enter your message : ")
decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)