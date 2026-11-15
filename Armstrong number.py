num=int(input("Enter a number: ")) 
original_num=num
n=len(str(num)) # finds the total digit 
total_sum=0
while num>0: # This tells Python to keep repeating the indented lines below as long as num is greater than 0. Once all digits are processed, num becomes 0 and the loop stops.
    digit=num%10 # The % (modulo) operator finds the remainder when dividing by 10, which always gives you the last digit.
    total_sum+=digit**n # The ** operator raises the digit to the power of n (which is 3), and += adds that result to total_sum.
    num=num//10 #The // (floor division) operator divides by 10 and drops the decimal, effectively removing the last digit.
if total_sum==original_num: # After the loop finishes, total_sum is 153. This checks if that calculated sum matches your saved copy (153). 
    print(original_num,"is an Armstrong number")  #  
else:
    print(original_num,"is not an Armstrong number")
