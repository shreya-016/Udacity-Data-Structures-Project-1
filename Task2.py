"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

from collections import defaultdict

hashmap = defaultdict(int)
for call in calls:
    if call[0] not in hashmap:
        hashmap[call[0]] = int(call[3])
    elif call[0] in hashmap:
        hashmap[call[0]] += int(call[3])
    if call[1] not in hashmap:
        hashmap[call[1]] = int(call[3])
    elif call[1] in hashmap:
        hashmap[call[1]] += int(call[3])

maxPhoneNumber = max(hashmap, key = lambda x : hashmap[x])
maxCallDuration = hashmap[maxPhoneNumber]

print("{} spent the longest time, {} seconds, on the phone during september 2016".format(maxPhoneNumber, maxCallDuration))
    
"""
TIME COMPLEXCITY
Tc of this task is O(n) where n is total records in call file.

"""



