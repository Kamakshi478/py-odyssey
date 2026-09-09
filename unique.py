original_list=["apple", "banana", "cherry", "apple", "cherry", "date"]
clean_list=list(dict.fromkeys(original_list))
print(clean_list)