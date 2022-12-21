# COMMENTS = DEBUG

priorities = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for idx, val in enumerate(list(alphabet)):
	priorities[val] = idx+1
for idx, val in enumerate(list(alphabet.upper())):
	priorities[val] = idx+27

# print(priorities)

priorityItems = []

rucksacks = open('input.txt', 'r').readlines()
rucksacks = '#'.join(rucksacks)
rucksacks = rucksacks.replace('\n', '')
rucksacks = rucksacks.split('#')

for rucksack in rucksacks:
	rucksack = ''.join(rucksack)
	rck1 = list(rucksack)[:int((len(rucksack)/2))]
	rck2 = list(rucksack)[int(len(rucksack)/2):]
	for letter in rck2: 
		if letter in rck1:
			priorityItems.append(letter)
			break # This was my single point of failure.

total = 0

for x in priorityItems:
	total += priorities[x]

print(f'Part 1: {total}')

# print(((len('vJrwpWtwJgWrhcsFMMfFFhFp')/2)-1))
# rucksack = 'vJrwpWtwJgWrhcsFMMfFFhFp'
# rck1 = list(rucksack)[:int((len(rucksack)/2))]
# rck2 = list(rucksack)[int(len(rucksack)/2):]

# print(''.join(rck1))
# print(''.join(rck2))

# print(len(priorityItems))
# print(len(rucksacks))

# for item in rck2:
# 	if item in rck1:
# 		print(item)

group = []
groups = []
from itertools import count
for rucksack, n in zip(rucksacks, count(1)):
	if n % 3 == 0:
		group.append(rucksack)
		groups.append(group)
		group = []
		continue
	group.append(rucksack)

# print(len(groups)) # Outputs 100, we are on the right track. (300/3 = 100)
# print(groups[1])

priorityItems2 = []

# groups = [['vJrwpWtwJgWrhcsFMMfFFhFp','jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL','PmmdzqPrVvPwwTWBwg']]

for group in groups:
	for item in group[0]:
		if item in group[1] and item in group[2]:
			priorityItems2.append(item)
			break

# print(priorityItems2)

total2 = 0
for x in priorityItems2:
	total2 += priorities[x]

print(f'Part 2: {total2}')
