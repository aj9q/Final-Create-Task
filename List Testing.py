import random

i = 0
Test01 = ['Thing1', 'Thing2', 'Thing3', 'Thing4']
match1 = (random.sample(Test01, 2))
print(Test01)
print(match1)
poplist = len(match1)
while i != poplist:
    Test01.remove(match1[i])
    i += 1
print(Test01)
