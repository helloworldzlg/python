#!/usr/bin/env python

# init list
print("\n"+'list init:')
workmates_0 = ['aaa', 'bbb', 'ccc']
print(workmates_0)

# append
print("\n"+'list append:')
workmates_1 = []
workmates_1.append('aaa')
print(workmates_1)
workmates_1.append('bbb')
print(workmates_1)
workmates_1.append('ccc')
print(workmates_1)

# delete
print("\n"+'list delete:')
workmates_2 = ['aaa', 'bbb', 'ccc']
print(workmates_2)
del workmates_2[0]
print(workmates_2)
del workmates_2[0]
print(workmates_2)

# modify
print("\n"+'list modify:')
workmates_3 = ['aaa', 'bbb', 'ccc']
print(workmates_3)
workmates_3[0] = 'ddd'
print(workmates_3)

# pop delete
print("\n"+'list pop delete:')
workmates_4 = ['aaa', 'bbb', 'ccc']
print(workmates_4)
mate = workmates_4.pop()
print(mate)
print(workmates_4)
mate = workmates_4.pop(1)
print(mate)
print(workmates_4)

# list remove
print("\n"+'list remove:')
workmates_5 = ['aaa', 'bbb', 'ccc', 'ddd']
print(workmates_5)
mate = workmates_5.remove('ddd')
print(mate)
print(workmates_5)

# list sort
print("\n"+'list sort:')
mates = ['aaa', 'ddd', 'ccc', 'bbb']
print(mates)
mates.sort()
print(mates)
mates.sort(reverse=True)
print(mates)

# list temp sort
print("\n"+'list temp sort:')
mates = ['aaa', 'ddd', 'bbb', 'ccc']
print(mates)
temp = sorted(mates)
print(temp)
print(mates)