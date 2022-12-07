

# iterate through file
with open("day-4/input.txt", "r") as file:
    overlaps = 0
    
    for line in file:
        assignments = []

        # parse input
        for assignment in line.strip().split(","):
            assignments.append(assignment.split("-"))
        for i in range(len(assignments)):
            for j in range(len(assignments[i])):
                assignments[i][j] = int(assignments[i][j])

        if ((assignments[0][0] <= assignments[1][0] and assignments[0][1] >= assignments[1][1]) or 
            (assignments[1][0] <= assignments[0][0] and assignments[1][1] >= assignments[0][1])):
            print(assignments)
            overlaps += 1
    
    print(f'Number of overlaps: {overlaps}')