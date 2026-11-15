num=int(input("Enter a number: "))
original_num=num
n=len(str(num))
total_sum=0
while num>0:
    digit=num%10
    total_sum+=digit**n
    num=num//10
if total_sum==original_num:
    print(original_num,"is an Armstrong number")   
else:
    print(original_num,"is not an Armstrong number")