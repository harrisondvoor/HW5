import re

x = open("ActualData.txt")
num_lst = []

for line in x:
    line = line.rstrip()
    extract = re.findall("([0-9]+)", line)

    if len(extract) < 1 : continue

    for i in range(len(extract)):
        integer = int(extract[i])
        num_lst.append(integer)

print(sum(num_lst))

