def prime(n):
    flag = True
    for i in range(2, n):
        if (n % i == 0):
            flag = False
    if (n != 1):
        if (flag):
            print(n, "is a Prime Number")
        else:
            print(n, "is Not a Prime Number")
    else:
        print("1 is neither prime nor composite")


def evenodd(n):
    if (n % 2 == 0):
        print(n, "is a Even number")
    else:
        print(n, "is a Odd number")


def divisibleby5(n):
    if (n % 5 == 0):
        print(n, "is Divisible by 5")
    else:
        print(n, "is Not divisible by 5")


n = int(input("Enter a number"))
prime(n)
evenodd(n)
divisibleby5(n)
print("Sum upto", n, "=", int((n * (n + 1)) / 2))
