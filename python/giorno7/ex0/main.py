import csv

#Parte 1
with open("data.csv", encoding='utf-8') as fd:
    reader = csv.reader(fd)
    saved_data = []
    for line in reader:
        print(line)
        saved_data.append(line)

header = saved_data[0]
data = saved_data[1:]

def surname(line):
    return line[1]

#Parte 2
sorted_data = list(sorted(data, key=surname))

#Parte 3
i = 1
for line in sorted_data:
    print([i] + line)
    i+=1

with open("data2.csv", mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    for line in sorted_data:
        writer.writerow(line)


#BONUS
def name(line):
    return line[0]

bonus_data = list(sorted(sorted_data, key=name))