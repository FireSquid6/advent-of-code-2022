currentTotal = 0
elves = []

with open("./day-1/input.txt", "r") as file:
  for line in file:
    line = line.strip("\n")
    
    if line.isdigit():
      currentTotal += int(line)
    
    if line == '':
      elves.append(currentTotal)
      currentTotal = 0

  
  elves.sort(reverse=True)
  print(elves)

  total = 0
  for i in range(3):
    total += elves[i]

  print(total)
  