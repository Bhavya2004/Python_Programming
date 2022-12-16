# Print the following pattern:
# 5 5 5 5 5
# 5 4 4 4 5
# 5 4 3 4 5 
# 5 4 4 4 5
# 5 5 5 5 5

# [google's logic]:
# n=int(input("Enter the value of n: "))
# for x in range(1-n,n):
#     for y in range(1-n,n):
#         if abs(x)>abs(y):
#             print("{:2d}".format(abs(x)+1),end="")
#         else:
#             print("{:2d}".format(abs(y)+1),end="")
#     print()
        
