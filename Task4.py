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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
TeleNum = set()
nonTeleNum = set()

for num in calls:
    TeleNum.add(num[0])
for num in calls:
    nonTeleNum.add(num[1])


for num in texts:
    nonTeleNum.add(num[0])
for num in texts:
    nonTeleNum.add(num[1])

result = sorted(TeleNum - nonTeleNum)
print("These numbers could be TeleNums:")
for r in result:
    print(r)

"""
TIME COMPLEXCITY

It has a time complexcity of O(nlogn) as the each for loops used here are taking O(n) time which add up to O(4n) and the sorted function
takes O(nlogn). So the total time complexcity will be O(4n + nlogn) which is equal to O(nlogn).

"""









    





    
