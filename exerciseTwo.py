import heapq

import random

# initializing list
myList = []
# creates (random) amount of values in the list
listLength = random.randint(1,20)

for x in range(listLength):
    #for every value in the list, it will now generate a random value from 1 to 100 until list is complete
    myList.append(random.randint(1,101));

print(myList)

# using heapify to CONVERT LIST INTO HEAP
# Transforms list into a heap, in-place, in linear time
heapq.heapify(myList)

print (list(myList))

# printing modified heap

def heapSort(myList):
	n = len(myList)

	# Build a maxheap.
	for i in range(n, -1, -1):
		heapq.heapify(myList)

	# One by one extract elements
	for i in range(n-1, 0, -1):
		myList[i], myList[0] = myList[0], myList[i] # swap
		heapq.heapify(myList)

# code to test above list
heapSort(myList)
n = len(myList)
print ("Binary Heap Tree results: ")
for i in range(n):
	print ("%d" %myList[i]),
	

