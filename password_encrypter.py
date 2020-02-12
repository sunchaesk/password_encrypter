import math

def encode(s):
    n = sum([ord(i) for i in s])
    avg = n / len(inp)
    icmt = 0
    l = []
    for i in range(12):
        icmt += avg
        l.append(chr(math.ceil(icmt)))
    r = ''.join(l)
    return r

def is_english(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

def decode():
    pass

if __name__ == '__main__':
    while True:
        try:
            inp = int(input('What do you want to do?: 1 or 2: '))
            if not 0 < inp < 3:
                print('Invalid num')
        except:
            print('Invalid type')
        else:
            break
    if inp == 1:
        print('==========================')
        print('Password has to be in English')
        print('No longer than 24 characters')
        print('==========================')
        while True:
            inp = input('Enter a string to encode: ')
            if 0 < len(inp) < 25:
                if is_english(inp) == True:
                    print(encode(inp))
                    break
                else:
                    print('Invalid Characters')
            else:
                print('Invalid length')
        input()
    elif inp == 2 :
        print('decode')
        input()