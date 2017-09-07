def func_fac(fac):
    fac = 1
    for i in range(1, n + 1):
        fac = fac * i
    return fac

n = 0
while (n > -1):
    n = int(input("Enter a number: "))
    if (n == -1):
        break


    print(func_fac(n))