# there are two types of loops in Python: for and while

print("asalam u alikum aj hum loop prhy ga or bi boht kuch ")

# for loop

# a = range(1 , 20 , 1)
# for i in a:
#     print(i)


# agar is ma humay reverse ma jana pry to steps ko -1 krny pry ga 

# print a table of 8 
# for i in range(8 , 81 , 8):
#     print(i)

# string in for loop 
a = "Tiger"

for i in range(5):
    print(a[i])


b= "Python Tiger ha "

for i in range(len(b)):
    print(b[i])
               
for i in b:
    print(i)

# for loop and break statement
for i in range(1 , 20):
    if i == 16:
        break
    else:
        print(i)

# for loop and conitnue statement
for i in range(1 , 21):
    if i == 17:
        continue
    print(i)





# else work krta ha break ka sath 





# loop question-1

# num = int(input("enter a number: "))

# for i in range(1 , num+1):
#     print("hello world")


# question - 2
# num = int(input("please enter a number : "))
# for i in range(num , 0 , -1):
#     print(i)


# question - 3 
# num = int(input("please enter a number : "))
# for i in range(1 , 11):
#     print(f"{num} x {i} = {num*i}")


# quesion -  4
# num = int(input("please enter a number:"))

# for i in range(num -1, 0 , -1):
#     print(i)
#     num *= i
# print(num)

# question- 5
# num = int(input("please enter your number"))
# even = 0
# odd = 0

# for i in range(1 , num+1):
#     if i %2 ==0 :
#         even += i

#     else:
#         odd += i
        
# print("this is odd : " , odd)
# print("this is even : " , even)



# question - 6
# num = int(input("please enter a number"))
# factorsSum = 0 

# for i in range(1 , num):
#     if num % i == 0:
     
#         factorsSum += i
# if( factorsSum == num):
            
#             print(f"{num} is a prefect number")
# else:
#             print(f"{num} is not a perfect number")     
        


 # question - 7

# num = int(input("please enter a number : "))
# count = 0

# for i in range(1 , num+1):
#     if num % i == 0 :
#         count += 1 
         
# if count == 2 : 
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")





# Reverse a string
# a = "tiger"
# print(a[::-1])


# reverse a string using loop
# a = str(input("enter a string:"))
# reversed_string = ""
# for i in range(len(a)- 1 , -1 , -1):
#     reversed_string += a[i]
# if reversed_string == a:
#     print("string is a palindrome")
# else:
#     print("string is not a palindrome")
# palindrome wo hota ha agar string ko reverse krne pr wo same hi aaye



# check alphabet or digit in string
# a = "tiger123##"
# alpha = 0
# digit = 0
# spec = 0
# for i in a :
#     if i.isalpha():
#       alpha +=1
      
#     elif i.isdigit():
#         digit += 1
        
#     else:
#         spec += 1


# print(f"{alpha} is alphabet , {digit} is digit , {spec} is special character")




# while loop

# a = 1 
# while a <= 30:
#     print(a)
#     a += 1



# a = int(input("please enter a number : "))
# newa = a
# rev = 0

# while a > 0 :
#     rev =  rev * 10  + a % 10
#     a //=10


# if rev == newa:
#     print("number is palindrome")
# else:
#     print("number is not palindrome")


# guess the number game
import random
num = random.randint(1 , 10)
print(num)
tries = 0

while True:
    guessNum = int(input("please enter a number between 1 to 10: "))

    if guessNum == num:
        print("you win")
        tries += 1
        break
    elif guessNum < num:
        print("you are too low")
        tries += 1
    elif guessNum > num:
        print("you are too high")
        tries += 1
    else:
        print("you lose")
        tries += 1

print(f"you took {tries} tries to guess the number")









