import csv

data = open("example.csv", encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)

for line in data_lines[:5]:
    print(line)
    
print(data_lines[10][3])

all_emails = []
for line in data_lines[1:15]:
    all_emails.append(line[3])
    
print(all_emails)

full_names = []

for line in data_lines[1:]:
        full_names.append(line[1]+' '+line[2])
        
file_to_output = open("to_save_file.csv", mode='w', newline='')
csv_writer = csv.writer(file_to_output,delimiter=',')

csv_writer.writerow(['a', 'b', 'c'])
csv_writer.writerow([['1', '2', '3'], ['4', '5', '6']])

file_to_output.close()
data.close()