import csv

data = open("find_the_link.csv", encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)

i = 0
for line in data_lines:
    print(line[i], end='')
    i += 1
    
data.close()