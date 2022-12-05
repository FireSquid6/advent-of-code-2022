from math import floor
filepath = "./day-3/input.txt"


# get priority dictionary
priority_str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priority = {}
for i in range(len(priority_str)):
    priority[priority_str[i]] = i + 1


# iterate through file
total = 0
with open(filepath) as file:
    bags = []

    for line in file:
        bags.append(line)

        if len(bags) == 3:
            for key in priority.keys():
                if (key in bags[0]) and (key in bags[1]) and (key in bags[2]):
                    total += priority[key]
            bags = []

print(priority)
print(total)