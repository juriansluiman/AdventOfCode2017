"""
Live example at https://repl.it/@juriansluiman/2py
"""

import requests

data = requests.get('https://raw.githubusercontent.com/juriansluiman/AdventOfCode2017/master/2.txt')
rows = data.split("\n")

checksum = 0
for row in rows:
  values = list(map(int, row.split("\t")))
  diff   = max(values) - min(values)
  checksum += diff

print("Part 1:", checksum)

checksum = 0
for row in rows:
  values = list(map(int, row.split("\t")))
  values = sorted(values)
  
  stopped = False

  for i,v in enumerate(values):
    testing = values[i+1:]
    for c in testing:
      if (c%v == 0):
        checksum += int(c/v)
        break
  
print("Part 2:", checksum)
