# list comprehension is: [ expression for item in list if conditional ]
#print [(x, y) for x in range(4) for y in range(2)] The second for runs the length of the first 4. so it looks like:
#for x in range(4):
#	for y in range(2):
#		print (x, y)

"""
#The fastest is the map, the second fastest is the list comprehension and the for loop is about twice as slow as the list comprehension.
#From slowest to fastest:
import time
t1 = time.clock()

#f = []
#for i in range(10000000):
#	f.append(i)

#f = [i for i in range(10000000)]

#f = []
#map(f.append, range(10000000))

print time.clock() - t1
"""

l = ['fred', 'sam', 'joe', 'willy']

#The first statement is what is appended to the list (i... would be appended. Here is the below in english:
#append i to the list if i[0] == "s" else, append 'no' to the list. Do this for all the items in the list, i = the item in the list.
#*note* if you are doing anything but appending to the list that is being built, like appending to another list, it doesn't seem to like having that other statement anywhere but as the first item in the list like:
#l = []
#[l.append(k) for k in range(5) if k == 2]

#a = [(i if i[0] == "f" else 'no') for i in l]

#b = [(i if i[0] == "f" else ('yes' if i[1] == "a" else 'no')) for i in l]
#print b

j = ['fred', 'joe', 'sam']

d = {'joe': 5, 'sam': 2}
d2 = {'sam': 99}

[d2.update({k: d[k]}) for k in d]

#print d2
