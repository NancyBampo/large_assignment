import string
def alphabet_position(letter):
    
    upper_case = string.ascii_uppercase
    lower_case = string.ascii_lowercase
    if letter in upper_case:
        position = upper_case.find(letter)
        #return position
    elif letter in lower_case:
        position = lower_case.find(letter)
    return position
#print(alphabet_position('L'))
def rotate_character(char, rot):
    upper_case = string.ascii_uppercase
    lower_case = string.ascii_lowercase
    if char in upper_case:
        rotation_position = (alphabet_position(char) + rot) % 26 
        #return chr(rotation_position + 65)
        return upper_case[rotation_position]
    elif char in lower_case:
        rotation_position = (alphabet_position(char) + rot) % 26 
        return lower_case[rotation_position]
    else:
        return char  