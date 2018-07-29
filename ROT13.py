import sys
string = input('> ')
chr_list = list(string)
for character in chr_list:
    if 65 <= ord(character) <= 77 or 97 <= ord(character) <= 109:
        sys.stdout.write(chr(ord(character) + 13))
    elif 78 <= ord(character) <= 90 or 110 <= ord(character) <= 122:
        sys.stdout.write(chr(ord(character) - 13))
    else:
        sys.stdout.write(character)
