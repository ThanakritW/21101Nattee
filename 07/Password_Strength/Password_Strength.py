checkLen = False
checkUpper = False
checkLower = False
checkNum = False
checkSym = False
checkRepetition = False
checkSeqNum = False
checkSeqAlpha = False
checkSeqKey = False
strNum = '01234567890'
strAlpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
strRow = '!@#$%^&*()_+/QWERTYUIOP/ASDFGHJKL/ZXCVBNM'

pwd = input().strip()

if(len(pwd) < 8):
    checkLen = True
for e in pwd:
    if 'a' <= e <= 'z':
        checkLower = True
    elif 'A' <= e <= 'Z':
        checkUpper = True
    elif '0' <= e <= '9':
        checkNum = True
    else:
        checkSym = True
for i in range(0, len(pwd)-3):
    if(pwd[i]*4 == pwd[i:i+4]):
        checkRepetition = True
    if((pwd[i:i+4] in strNum) or (pwd[i:i+4] in strNum[::-1])):
        checkSeqNum = True
    if((pwd[i:i+4].upper() in strAlpha) or (pwd[i:i+4].upper() in strAlpha[::-1])):
        checkSeqAlpha = True
    if((pwd[i:i+4].upper() in strRow) or (pwd[i:i+4].upper() in strRow[::-1])):
        checkSeqKey = True

if checkLen:
    print('Less than 8 characters')
if not checkLower:
    print('No lowercase letters')
if not checkUpper:
    print('No uppercase letters')
if not checkNum:
    print('No numbers')
if not checkSym:
    print('No symbols')
if checkRepetition:
    print('Character repetition')
if checkSeqNum:
    print('Number sequence')
if checkSeqAlpha:
    print('Letter sequence')
if checkSeqKey:
    print('Keyboard pattern')
if (not(checkLen or (not checkUpper) or (not checkLower) or (not checkNum) or (not checkSym) or checkRepetition or checkSeqNum or checkSeqAlpha or checkSeqKey)):
    print('OK')
