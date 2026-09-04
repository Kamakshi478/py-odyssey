text= input("Enter a string:")
vowel_count = 0 

for char in text:
    if char.lower() in 'aeiou':
        vowel_count += 1
print(f"Number of vowels in the string: {vowel_count}")