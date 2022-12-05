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
    for line in file:
        first_compartment = line[0:floor(len(line) * 0.5)]
        second_compartment = line[floor(len(line) * 0.5):len(line)]

        # add priority if an item is present in both compartments
        # make sure to remove duplicates!
        for char in list(dict.fromkeys(first_compartment)):
            if char in second_compartment:
                total += priority[char]

print(priority)
print(total)