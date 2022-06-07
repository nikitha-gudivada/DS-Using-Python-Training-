n = int(input("Enter a number"))
for i in range(1, n + 1):
    for j in range(1, 11):
        print(str(i) + "*" + str(j) + "=" + str(i * j))
    print("----------")

