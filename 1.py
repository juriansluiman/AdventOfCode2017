import requests

data = requests.get('https://raw.githubusercontent.com/juriansluiman/AdventOfCode2017/master/1.txt')
data += data[0]

result = 0
size   = len(data)

for i,c in enumerate(data):
  if (i+1 != size and c == data[i+1]):
    result += int(c)
    
print(result)
