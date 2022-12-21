# Print the following pattern:
# 5 5 5 5 5
# 5 4 4 4 5
# 5 4 3 4 5 
# 5 4 4 4 5
# 5 5 5 5 5


n=int(input("Enter the value of n: "))

for x in range(1,n+1):
    for y in range(1,n+1):
        if((y == 1 or y == n) or (x == 1 or x == n)):
            print(n,end="")
        elif(x==2 or x==n-1 or y==2 or y ==n-1):
            print(n-1,end="")
        else:
            print(n-2,end="")
        
    print()
    
        
