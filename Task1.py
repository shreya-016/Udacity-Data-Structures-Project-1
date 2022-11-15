"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
answer = 570
"""

different_tel_num = set()

for num in texts:
    different_tel_num.add(num[0])
    different_tel_num.add(num[1])
for num in calls:
    different_tel_num.add(num[0])
    different_tel_num.add(num[1])
print("There are {} different telephone numbers in the records.".format(len(different_tel_num)))

"""
TIME COMPLEXCITY
Tc of this task is O(n) + O(m) == max(O(n,m)) where n is total records in call file, and m is total records in text file. 

"""
