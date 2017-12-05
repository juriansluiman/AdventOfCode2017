"""
Live example at https://repl.it/@juriansluiman/1py
"""

import requests

data = requests.get('https://raw.githubusercontent.com/juriansluiman/AdventOfCode2017/master/1.txt')
data += data[0] # To fix the last number will be checked too

result = 0
size   = len(data)

for i,c in enumerate(data):
  if (i+1 != size and c == data[i+1]):
    result += int(c)
    
    
print("Part 1:", result)

result = 0 # Reset
data = data[:-1] # Reset
size = len(data)
half = int(size/2)

for i,c in enumerate(data):
  pos = i+half
  if (pos >= size):
    pos = pos-size
    
  if (c == data[pos]):
    result += int(c)

print("Part 2:", result)
