import re

fh = open("Sample Data.txt")
count = 0
lst = []
for line in fh:
    line = line.rstrip()
    stuff = re.findall("[0-9]+", line)
    while len(stuff) > 0:
        num = float(stuff.pop(0))
        lst.append(num)
    
print(lst)
print(len(lst), int(sum(lst)))
