num=12345
reverse=0 # create a variable to build our reversed number, to store the reversed number

while num>0: # We need to repeat te same process for each digit in the number, so we will use a while loop to repeat the process until the number is 0
    digit=num%10 # This is used because we need to get the last digit of the number, and we can do that by using the modulus operator, which gives us the remainder of a division. In this case, we are dividing by 10, so we will get the last digit of the number.
    reverse=reverse*10+digit   # Ths is used to build the reversed number. We multiply the current reversed number by 10 and add the last digit we just got from the original number. This effectively shifts the digits of the reversed number to the left and adds the new digit to the right.
    num=num//10 # to remove the last digit from the original number, we can use integer division by 10. This will effectively shift the digits of the original number to the right, removing the last digit.

print(reverse)