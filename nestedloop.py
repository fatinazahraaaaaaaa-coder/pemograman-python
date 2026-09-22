max = int(input("jumlah bintng: "))

for i in range(max):
    for j in range(0, max - i):
        print("*", end=" ")
    print()