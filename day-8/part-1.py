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

    return crosshair


grid = []

with open("./test-input.txt") as file:
    for line in file:
        line = line.strip()
        trees = []
        for char in line:
            trees.append(int(char))
        
        grid.append(trees)


visible = 0
visible_coords = []
for y in range(len(grid)):
    for x in range(len(grid[y])):
        visible_lines = 4
        crosshair = get_crosshair(x, y)
        for line in crosshair:
            for tree in line:
                if tree >= grid[y][x]:
                    visible_lines -= 1
                    break
        
        if visible_lines > 0:
            visible += 1
            visible_coords.append([y, x])
                
                
        print(crosshair)


print(visible)