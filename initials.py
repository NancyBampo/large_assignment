def get_initials(fullname):
    full_name = fullname
    name_list = full_name.split()
    initials = ""
    for name in name_list:
        initials += name[0].upper()

    return 'The initials of ' + full_name + ' is ' + initials

def main():    #return ''
    name = input('Please Enter your full name?: ')
    print(get_initials(name))


if __name__ == '__main__':
    main()
