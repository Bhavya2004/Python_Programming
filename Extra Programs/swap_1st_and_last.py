#Write a program to swap first and last digit of a integer number.
import math

n=int(input("Enter your number:"))
temp=n
count=0
while(temp>0):
    temp=temp//10
    count=count+1

count=count-1
first_digit=n // math.pow(10,count)
last_digit=n % 10

new=(n//10)*10+first_digit #removing last digit and adding first digit
new=(new % pow(10,count))+(last_digit * pow(10,count)) #removing first digit and adding last digit

print(f"Reversed Number:{new}")


