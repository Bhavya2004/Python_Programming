# Print the following pattern:
# # # # #
#       #
#       #
#       #
# # # # #       
n=int(input("Enter the value of n: "))
for x in range(1,n+1):
    for y in range(1,n+1):
        if((y == 1 or y == n) or (x == 1 or x == n)):
            print("#",end="")
        else:
            print(" ",end="")
    print()
        

