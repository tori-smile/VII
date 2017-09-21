import getpass
import os

def print_menu():
    print "What do you want to do? (Print number)"
    print "1. To encrypt a file"
    print "2. To decrypt a file"
    print "3. Exit \n"

def read_answer():
    try:
        return int(raw_input())
    except ValueError as e:
        return 0

def correct_filepath(height = 0):
    if height == 0:
        print "Print file path: "
    else:
        print "\nWrong file path. Please try again."
    path = raw_input()
    if os.path.isfile(path):
        return (True, path)
    else:
        ans, path = correct_filepath(height + 1)
        if height < 2 and ans:
            return (True, path)
        else:
            return (False, path)

def CaesarCipher(shift):
    unicode_lenght = 65536;
    new_file = ''
    answer, path = correct_filepath()
    if answer:
        print "\nEncrypting something ...\n"
        with open(path, 'rb') as f:
            old = f.read(1)
            num = 0
            while old:
                new_file = new_file + chr((ord(old) + shift) % unicode_lenght)
                old = f.read(1)
        print new_file
        with open(path+'1', 'wb') as f:
            f.write(new_file)
    else:
        print "\nCan't find file you want to encrypt. =(\n"

def encrypting(indicator):
    shift = read_shift()
    # print type(shift), type(indicator)
    CaesarCipher(shift * indicator)

def read_shift():
    print "Print shift, please"
    ans = read_answer()
    while ans == 0:
        print "Enter correct shift, please"
        ans = read_answer()
    return ans

if __name__=='__main__':
    password = '123'
    keyword = 'FalseAlarm'
    print "Hello, I'm cifer helper.\n"
    print_menu()
    ans = read_answer()
    while ans != 3:
        if ans == 1:
            encrypting(1)
        elif ans == 2:
            encrypting(-1)
        else:
            print "Something went wrong. Please try again.\n"
        print_menu()
        ans = read_answer()
