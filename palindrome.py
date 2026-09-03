value= input("Enter a number or a string: ")
reverse=value[::-1]
if value==reverse:
    print("The given value is a palindrome")
else:
    print("The given value is not a palindrome")