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
