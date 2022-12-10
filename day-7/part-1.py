root = []
stack = []


with open("./day-7/test-input.txt") as file:
    current_dir = root
    stack.append(current_dir)

    for line in file:
        line = line.strip()
        if line == "$ cd /":
            continue

        if "$" in line:
            if "cd" in line:
                if ".." in line:
                    stack.pop()
                    current_dir = stack[len(stack) - 1]
                else:
                    current_dir.append([])
                    current_dir = current_dir[len(current_dir) - 1]
                    stack.append(current_dir)
            elif "ls" in line:
                pass
        elif not "dir" in line:
            string = ""
            for char in line:
                if char.isdigit():
                    string += char
            
            current_dir.append(int(string))

print(root)


SMALL_FILES_SIZE = 0


def get_dir_size(dir: list) -> int:
    size = 0
    
    for item in dir:
        if isinstance(item, list):
            size += get_dir_size(item)
        else:
            size += item

    if size < 100000:
        SMALL_FILES_SIZE += size

    return size