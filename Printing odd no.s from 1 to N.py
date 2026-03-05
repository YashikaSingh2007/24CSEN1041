N = int(input("Enter the number:"))

first = True

for i in range(1, N+1):
    if i%2!=0:
        if first:
            print(i, end="")
            first = False
        else:
            print(",",i,sep="",end="")



OUTPUT:
Enter the number:11
1,3,5,7,9,11

Enter the number:8
1,3,5,7

Enter the number:1
1

