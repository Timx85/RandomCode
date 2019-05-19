"""

"""
import random

a = random.sample(range(100), 5)
b = random.sample(range(50), 5)
c= []

for item in a:
  if item in b and item not in c:
    c.append(item)

customList = [x*y for x in a for y in b if x*y%2 != 0]

print(a)
print(b)
print(c)
print(customList)