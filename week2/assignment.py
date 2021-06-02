import re
name = input("Enter file:")

#To open and read the text file
if len(name) < 1 : name = "regex_sum_898395.txt"
handle = open(name)
book = handle.read()

#search for numbers in file called book
sums = 0
number = re.findall('[0-9]+', book)

numbers = []

#to loop through the list of found numbers
for total in number:
    numbers.append(int(total))
    
#to sum up a list called numbers
print(sum(numbers))
