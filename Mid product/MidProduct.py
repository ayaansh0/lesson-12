#take two input from user 
lower = int(input("Enter a upper range :"))
upper = int(input("Enter a lower range "))


print("prime numbers between ", lower , "and", upper, "are")
#iterate loop from lower limit to upper limit
for num in range(lower,upper + 1 ):
    #all prime numbers are greater than 1 
    if num > 1 :
        for i in range(2, num):
            if (num % i) == 0:
                break 
        else:
            print(num)
