

# iterate through file
with open("day-4/input.txt", "r") as file:
    overlaps = 0
    
    for line in file:
        assignments = []

        for assignment in line.strip().split(","):
            assignments.append(assignment.split("-"))
        for i in range(len(assignments)):
            for j in range(len(assignments[i])):
                assignments[i][j] = int(assignments[i][j])

        arrays = []
        for assignment in assignments:
            array = []
            for i in range(assignment[0], assignment[1] + 1):
                array.append(i)
            arrays.append(array)
        
        print(arrays)

        for i in range(len(arrays[0])):
            if arrays[0][i] in arrays[1]:
                overlaps += 1
                break

    
    print(f'Number of overlaps: {overlaps}')