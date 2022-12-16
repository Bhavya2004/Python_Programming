# Print the following pattern:
#     *
#    * *
#   * * * 
#  * * * * 
# * * * * *
n=int(input("Enter the value of n: "))
for x in range(1,n+1):
    for y in range(n,x,-1):
        print(" ",end="")
    for z in range(0,x):
        print("* ",end="")
    print()
    

