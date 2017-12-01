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
    
print(result)
