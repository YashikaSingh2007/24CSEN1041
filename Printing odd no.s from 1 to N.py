N = int(input("Enter the number:"))

first = True

for i in range(1, N+1):
    if i%2!=0:
        if first:
            print(i, end="")
            first = False
        else:
            print(",",i,sep="",end="")
