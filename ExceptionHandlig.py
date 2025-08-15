# print("hello world" -> this is a syntax error


# a = 12
# if a == 12:
# print("ok")  # This will raise an indentation error



# try keyword is used to handle exceptions in Python
# try:  

number = int(input("Enter a number: "))

try:
    print(10/number)

except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("No exceptions occurred, the division was successful.")


# finally:
finally:
    print("This block always executes, regardless of exceptions. mera gunda Raaj ha ma hamesha chalo ga ")


#raise Exception("This is a custom exception message")  # This will raise an exception
age = int(input("Enter your age: "))
if age < 18:
    raise Exception("You must be at least 18 years old to proceed.")  # Custom exception for age validation
else:
    print("You are old enough to proceed.")

print('This is the end of the ExceptionHandling.py script.')
