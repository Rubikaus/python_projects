answer = 0
str = ''
#str = input("Введите выражение которое необходимо посчитать: ")
#if (str.find('+')):
#    str = str.replace(' ', '')
#    neindex = str.index('+')
#    a = str[:(neindex)]
#    b = str[(neindex + 1):]
#    answer = a + b
#elif (str.find('-')):
#    str = str.replace(' ', '')
#    neindex = str.index('-')
#    a = str[:(neindex)]
#    b = str[(neindex + 1):]
#    answer = a - b
str = input()
answer = int(str)
while(True):
    str = ''
    str = input()
    if (str.find('+')):
        str = str.replace('+', ' ')
        str = str.replace(' ', '')
        answer += int(str)
    elif (str.find('-')):
        str = str.replace(' ', '')
        str = str.replace('-', '')
        answer -= int(str)
    elif (str.find('*')):
        str = str.replace(' ', '')
        str = str.replace('*', '')
        answer *= int(str)
    elif (str.find('/')):
        str = str.replace(' ', '')
        str = str.replace('/', '')
        answer /= int(str)
    elif (str.find('**')):
        str = str.replace(' ', '')
        str = str.replace('**', '')
        answer **= int(str)
    elif(str.find('=')):
        print(answer)
        exit(0)
    print(str)
