# Print the following pattern:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
n=int(input("Enter the value of n: "))
for x in range(1,n+1):
    for y in range(1,x+1):
        print(x,end=" ")
    print()

