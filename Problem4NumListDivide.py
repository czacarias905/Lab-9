#Cecilia Zacarias
#3/12/2020

#This problem is a while loop that intiallize a counter at 0 and will run until the counter reaches 50. It will check if the counter is divisible by 10 append to list, tens.

x = 0
ten = []

while x <= 50:
    print(x)
    if x% 10 == 0:
        ten.append(x)
    x += 1

print(ten)
