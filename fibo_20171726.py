
import time

def iterfibo(num):
    try :
        fib = [0,1]
        for i in range(2,num + 1):
            fib.append(fib[i-1] + fib[i - 2])
        return fib[num]
    except:
        return num
def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    start = time.time()
    fibonumber = iterfibo(nbr)
    start = time.time() - start
    print("iterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, start))