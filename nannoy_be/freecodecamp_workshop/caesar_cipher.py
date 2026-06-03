def caesar(text , shift, mode): 
    if not ininstance(text , shift ,(str,int)):
        return "error"
    if shift < 1 or shift > 25 : 
        return "Error, shift must be an integer between 1-25" 
        
    for i in text : 
        if i.isalpha(): 
            if i.isupper():
                ascii_value = ord(i)   
            else :
                ascii_value = ord(i)    
            #formula such that it convert to 0–25 range

            position = ord(i) - ascii_value
            shifted_text = (position + shift)%26   #if z = 26 and shift = 6 , the output should be f .
            encrypted_text += chr(shifted_text + position) 
            return enrypted_text 
        else :
            pass()    