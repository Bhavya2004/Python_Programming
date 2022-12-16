# Print the following pattern:
#        1
#      1  2
#     1  2  3
#   1  2  3  4
#  1  2  3  4  5
n=int(input("Enter the value of n: "))
for x in range(1,n+1):
    for y in range(n,x,-1):
        print(" ",end="")
    for z in range(1,x+1):
        print(str(z)+" ",end="")
    print()

 