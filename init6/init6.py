alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)



def caesar():
  
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    
    shift = int(input("Type the shift number:\n"))
    if shift >= 26:
      shift = shift % 26

    cipher_text = ""
    
    for letter in text:
      if letter in alphabet:
        
        if direction == "encode":
            index = (alphabet.index(letter)) + shift
            
        else:
            index = (alphabet.index(letter)) - shift
            
        cipher_text += alphabet[index]
        
      else:
        cipher_text += letter
              
        
        
    print(f"Here is your {direction}d result: {cipher_text.upper()}")
    
    
replay = True  

while replay:
  caesar()
  
  result = input("Would you like to restart the cipher program? 'yes' or 'no' ").lower()
  
  if result == "no":
    replay = False
    print("Goodbye")  

  
 