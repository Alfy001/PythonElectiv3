mess = input("Enter the text you want: ")
key = int(input("Enter the key to be added: "))
newmess = ""  # Initialize encrypted message as an empty string

# Encryption
for ch in mess:
    if 'a' <= ch <= 'z':  # Handle lowercase letters
        c_ord = ord(ch)
        c_ord += key
        if c_ord > ord('z'):  # Wrap around if it goes beyond 'z'
            c_ord = ord('a') + (c_ord - ord('z') - 1)
        newch = chr(c_ord)
    elif 'A' <= ch <= 'Z':  # Handle uppercase letters
        c_ord = ord(ch)
        c_ord += key
        if c_ord > ord('Z'):  # Wrap around if it goes beyond 'Z'
            c_ord = ord('A') + (c_ord - ord('Z') - 1)
        newch = chr(c_ord)
    else:
        # Non-alphabetical characters remain unchanged
        newch = ch
    newmess += newch  # Append the new character to newmess

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
