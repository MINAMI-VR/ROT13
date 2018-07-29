import sys

rot = int(input('ROT? > '))
string = input('String > ')
chr_list = list(string)
for character in chr_list:
    if 65 <= ord(character) <= 90 - rot or 97 <= ord(character) <= 122 - rot:
        sys.stdout.write(chr(ord(character) + 13))
    elif 90 - rot < ord(character) <= 90 or 122 - rot < ord(character) <= 122:
        sys.stdout.write(chr(ord(character) - 13))
    else:
        sys.stdout.write(character)
