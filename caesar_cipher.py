mess = input("Enter the text you want: ")
key = int(input("Enter the key to be added: "))
newmess = ""  

# Encryption
for ch in mess:
    if 'a' <= ch <= 'z': 
        c_ord = ord(ch)
        c_ord += key
        if c_ord > ord('z'):  
            c_ord = ord('a') + (c_ord - ord('z') - 1)
        newch = chr(c_ord)
    elif 'A' <= ch <= 'Z': 
        c_ord = ord(ch)
        c_ord += key
        if c_ord > ord('Z'): 
            c_ord = ord('A') + (c_ord - ord('Z') - 1)
        newch = chr(c_ord)
    else:
        
        newch = ch
    newmess += newch  

print("Encrypted text:", newmess)

# Decryption
newmess_dec = ""  

for ch in newmess:
    if 'a' <= ch <= 'z':  
        c_ord = ord(ch)
        c_ord -= key
        if c_ord < ord('a'):  
            c_ord = ord('z') - (ord('a') - c_ord - 1)
        newch = chr(c_ord)
    elif 'A' <= ch <= 'Z':  
        c_ord = ord(ch)
        c_ord -= key
        if c_ord < ord('A'):  
            c_ord = ord('Z') - (ord('A') - c_ord - 1)
        newch = chr(c_ord)
    newmess_dec +=newch

print("Decrypted text:", newmess_dec)
