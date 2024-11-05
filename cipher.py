# add your code here
def cipher(text, shift=5):
    encryption = ""
    
    for char in text:
        if char.isalpha():  
            offset = 65 if char.isupper() else 97
            encryption += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            encryption += char
    
    return encryption

text = input("Please enter a sentence to encrypt: ")

encryption = cipher(text)
print("Your encrypted sentence is:", encryption)

