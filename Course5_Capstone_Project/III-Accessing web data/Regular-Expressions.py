import re
filename = input("Enter the filename: ")
file = open(filename, "r")
content = file.read()
number_strings = re.findall(r'[0-9]+', content)
total=0
for num in number_strings:
    total += int(num)
count = len(number_strings)

print(total)

