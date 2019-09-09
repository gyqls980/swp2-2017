def Factorial(n):
    if (n<1 or n == 0 ):
        return 1
    else:
        return n*Factorial(n-1)

hyobin = int(input("팩토리얼 수를 입력하세요 : "))



while True :
	try :

		if hyobin <= -1 :
			break
		else :

			print(str(hyobin)+'! = ' + str(Factorial(hyobin)))
			hyobin = input("팩토리얼 수를 입력하세요 : ")

	except:
		print('invaild value')
		break