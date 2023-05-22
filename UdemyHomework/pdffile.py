import re

f = open("pdf.txt", 'r')

number = re.search(r'\d{3}.\d{3}.\d{4}', f.read())
if number:
    print(number.group())
f.close