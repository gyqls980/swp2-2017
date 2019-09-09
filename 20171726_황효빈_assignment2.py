

n = input('숫자를 입력하세요 : ')

while True:
    answer= 1
    count = 2
    mul = 1
    if str(n) == False:
        n = input('숫자를 입력하세요 : ')

    elif float(n) != int(float(n)):
        print('잘못 입력하셨습니다.')
        n = input('숫자를 입력하세요 : ')

    elif int(n) <= -1:
        break

    else:
        while count <= int(n):
            mul = mul + 1
            count = count + 1
            answer = answer * mul
        print(str(n) + '!=' + str(answer) + ' 입니다.')

        n = input("숫자를 입력하세요 : ")