from functions import *

sizeOfBlocks = 1
specialDividerCharacter = chr(1100)
shiftedAscii = 100
# ------------------------------------- encrypt -------------------------------------
def encryption(e, N):

    inputText = ''
    cipherText = ''
    lastCharacterLength = []

    print('\n----------------------------------------------------------------\n')
    print('Encryption)')

    # read input file [like: '123abc']
    with open('input.txt', encoding='utf-8') as input:

        while True:
            message = input.read(sizeOfBlocks)
            if not message:
                break
            # foreach character in file
            plainText = ''
            for word in message:
                # calculate ascii code of character
                asciiCode = str(ord(word)+shiftedAscii)
                plainText += asciiCode
                # add ascii code into message as a string
                inputText += word
                # save the length of ascii code
                # Calculate cipher [like: '495051979899']

            print('Ascii code of the line:\n', plainText)
            C = str(fastExponentiation(int(plainText), e, N))
            print('After exponentation:\n', C)
            # convert to character, 2-by-2 [like: '23124512564']

            lastCharacterLength.append(len(C)%3)
            cipherText += asciiToChar(C) + specialDividerCharacter
            print('Converting to cipherText:\n', asciiToChar(C))
            # store result [like: '@$as^&5']

    with open('encrypt.txt', 'w', encoding='utf-8') as Cipher:
        Cipher.write(cipherText)

    print('\nPlainText:\n{}'.format(inputText))
    print('PlainText to ASCII:\n{}'.format(cipherText))
    print('\n----------------------------------------------------------------\n')

    return lastCharacterLength

# ------------------------------------- decrypt -------------------------------------
def decryption(lastCharacterLength, d, N):

    print('\nDecryption)')
    # convert to ascii [like: '@$as^&5']

    with open('encrypt.txt', encoding='utf-8') as Cipher:
        c = Cipher.read()


    plainText = ''
    text = ''
    index = 0
    i = 0
    while index < len(c):
        # taking valid block of ciphertext
        if c[index] != specialDividerCharacter:
            text += c[index]

        # block is ready to compute
        else:
            print('Read cipherText:\n', text)
            asciiCode = charToAscii(text, lastCharacterLength[i])
            print('Convert to ascii:\n', asciiCode)
            plain = str(fastExponentiation(asciiCode, d, N))
            print('After exponentation:\n', plain)
            startIndex = 0
            # foreach character [like: '495051979899']
            for characters in range(len(plain)//3):
                # calculate ascii code of character - add character to plaintext
                temp = plain[startIndex:startIndex+3]
                if int(temp)>0:
                    plainText += chr(int(temp) - shiftedAscii)
                else:
                    plainText += chr(int(temp))

                # startIndex updates for new character
                startIndex += 3

            # make container empty
            text = ''
            i += 1
        # end of while
        index += 1


    print('\nPlainText:\n{}'.format(plainText))
    # store result [like: '123abc']
    with open('decrypt.txt', 'w', encoding='utf-8') as Message:
        Message.write(plainText)

    return

# ------------------------------------- Convert Ascii To Character -------------------------------------
def asciiToChar(C):

    # input [like: '23124512564']
    cipherText = ''
    # foreach character
    for i in range(0, len(C), 3):
        if i+3 >= len(C):
            cipherText += chr(int(C[i:]))
            break
        else:
            # calculate ascii code of character - add character to ciphertext
            cipherText += chr(int(C[i:i+3]))

    # output [like: '@$as^&5']
    return cipherText

# ------------------------------------- Convert Character To Ascii -------------------------------------
def charToAscii(C, length):

    # avoid adding extra '0' to odd strings [like: '@$as^&5']
    lastCharacter = ord(C[len(C)-1])
    # if it has 3 digits
    if length == 0:
        if lastCharacter < 10:
            lastCharacter = '00' + str(lastCharacter)
        elif lastCharacter >= 10 and lastCharacter < 100:
            lastCharacter = '0' + str(lastCharacter)
        else:
            lastCharacter = str(lastCharacter)
    # if it has 2 digits
    elif length == 2 and lastCharacter < 10:
        lastCharacter = '0' + str(lastCharacter)
    else:
        lastCharacter = str(lastCharacter)

    # remove last character
    C = C[:len(C)-1]

    asciiCode = ''
    # foreach character
    for word in C:
        # calculate ascii code of character
        ascii = ord(word)
        if ascii < 10:
            asciiCode += '00' + str(ascii)
        elif ascii >= 10 and ascii < 100:
            asciiCode += '0' + str(ascii)
        else:
            asciiCode += str(ascii)

    # output [like: 23124512564]
    asciiCode += lastCharacter
    return int(asciiCode)
