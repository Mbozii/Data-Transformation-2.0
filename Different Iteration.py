
'''You’re given:
nums = [4, 9, 13, 18, 7, 2, 15, 20]
Your task:
If the number is divisible by 3, multiply it by 5
If it’s even but not divisible by 3, divide it by 2
If it’s odd and not divisible by 3, add 7
Store all results in a new list
From that new list, create another list with values that are between 10 and 50 (inclusive)
Print both lists'''

nums = [4, 9, 13, 18, 7, 2, 15, 20]
mod_nums = []
values = []


for num in nums:
    if num % 3 == 0:
        result = num * 5
        mod_nums.append(result)
    elif num % 2 == 0 and num % 3 != 0:
        result = num // 2
        mod_nums.append(result)  
    elif num % 2 == 1 and num % 3 != 0:
        result = num + 7
        mod_nums.append(result)   
        
#mod_nums.append(result)

for num in mod_nums:
    if 10 <= num <= 50:
        values.append(num)           
            

# Sorted lists
mod_nums.sort()
values.sort()

print(mod_nums)
print(values)           