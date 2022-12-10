# not the best solution, but I'm going for speed tbh
def get_crosshair(start_x, start_y) -> list:
    crosshair = [[], [], [], []]
    
    xx = 0
    yy = 0
    i = 0
    while xx < len(grid[start_y]):
        if xx == start_x:
            i += 1
            xx += 1
            continue

        crosshair[i].append(grid[start_y][xx])
        xx += 1
    
    i += 1

    while yy < len(grid):
        if yy == start_y:
            i += 1
            yy += 1
            continue

        crosshair[i].append(grid[yy][start_x])
        yy += 1

    crosshair[0].reverse()
    crosshair[2].reverse()
    return crosshair


grid = []

with open("./input.txt") as file:
    for line in file:
        line = line.strip()
        trees = []
        for char in line:
            trees.append(int(char))
        
        grid.append(trees)


visible = 0
visible_coords = []
scenic_scores = []
for y in range(len(grid)):
    for x in range(len(grid[y])):
        
        height = grid[y][x]
        
        crosshair = get_crosshair(x, y) 
        visibility_amounts = []

        if x == 3 and y == 3:
            print("pain")

        for line in crosshair:
            visibility = 0

            
            for tree in line:
                visibility += 1
                if tree >= grid[y][x]:
                    break
                
            
            visibility_amounts.append(visibility)

        scenic_score = 1
        for visibility in visibility_amounts:
            scenic_score = scenic_score * visibility
                
        print(f"Tree at x:{x}, y:{y}, h: {grid[y][x]} has a scenic score of {scenic_score}")
        scenic_scores.append(scenic_score)


print(max(scenic_scores))