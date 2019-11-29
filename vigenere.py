import string
from helpers import alphabet_position, rotate_character
def encrypt(text, key):
    #get the key and get position fo each letter in key
    #modulus length of key
    upper_case = string.ascii_uppercase
    lower_case = string.ascii_lowercase
    key_list = []
    num = 0
    encrypted_list = ''
    for char in key:
        key_list.append(alphabet_position(char))
    for item in text:
        if item in upper_case:
            rotation_char = rotate_character(item, key_list[num])
            num = (num + 1) % len(key)
            encrypted_list += rotation_char
        elif item in lower_case:
            rotation_char = rotate_character(item, key_list[num])
            num = (num + 1) % len(key)
            encrypted_list += rotation_char
        else:
            encrypted_list += item
    return encrypted_list
def main():
    text = input("Please type a secret message: ")
    key = (input("Encryption key: "))

    print(encrypt(text, key))
if __name__ == "__main__":
    main()

    

