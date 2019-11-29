from helpers import alphabet_position, rotate_character
#print(rotate_character(" ", 13)) 
def encrypt(text, rot):
    encrypted_text = ""
    for char in text:
        encrypted_text += rotate_character(char,rot)
    return encrypted_text

def main():
    text = input("Please type a message: ")
    rot = int(input("Rotate by: "))

    print(encrypt(text, rot))
if __name__ == "__main__":
    main()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    