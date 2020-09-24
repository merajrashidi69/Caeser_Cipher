
#caeser-cipher decryptor

lower_letters = 'abcdefghijklmnopqrstuvwxyz'
upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            #1                       #25

def encrypt(word,key):
    result = ''
    key=int(key)
    for i in word:
        if i.isupper(): #uppercase letters
            index = upper_letters.index(i)
            index -= key
            result += upper_letters[index]

        elif i.islower(): #lowercase letters
            index = lower_letters.index(i)
            index -= key
            result += lower_letters[index]


        if i == ' ':
            result += i


    return result #return final result


while True:
    caeser_cipher = input('Enter the password: ')
    key = input('Enter the key: ')
    result = encrypt(caeser_cipher,key)
    print(result)
