import re
name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_42.txt"
handle = open(name)
book = handle.read()

sums = 0
#to find all numbers in file called book
num = re.findall('[0-9]+ ', book)

numbers = []

#to loop through a list called num
for total in num:
    numbers.append(int(total))
#to sum up the list numbers
print(sum(numbers))
