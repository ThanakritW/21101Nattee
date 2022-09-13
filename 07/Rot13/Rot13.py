while(True):
    s = input()
    if(s == 'end'):
        break
    for e in s:
        if(e.isalpha()):
            if(e.isupper()):
                print(chr((ord(e)+13-ord('A')) % 26+ord('A')), end='')
            else:
                print(chr((ord(e)+13-ord('a')) % 26+ord('a')), end='')

        else:
            print(e, end='')
    print('')
