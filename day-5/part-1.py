with open("./day-5/input.txt") as file:
    instruction_lines = []
    crate_lines = []

    # parse input
    for line in file:
        if "move" in line:
            instruction_lines.append(line.strip())
        elif "["  in line:
            crate_lines.append(line.strip("\n").replace("[", " ").replace("]", " "))
    
    # create crate array
    crate_array = []
    for i in range(len(crate_lines[len(crate_lines) - 1].replace(" ", ""))):
        crate_array.append([])
    
    for layer in reversed(crate_lines):
        i = 1
        for j in range(len(crate_array)):
            if layer[i] != " ":
                crate_array[j].append(layer[i])
            i += 4

    # perform instructions
    for instruction in instruction_lines:
        # parse instruction
        parsed_instruction: list = instruction.replace("move ", "").replace("from ", "").replace("to ", "").split(" ")
        for i in range(len(parsed_instruction)):
            parsed_instruction[i] = int(parsed_instruction[i])
        
        amount = parsed_instruction[0]
        from_stack = parsed_instruction[1] - 1
        to_stack = parsed_instruction[2] - 1

        forklift = []
        for i in range(amount):
            box = crate_array[from_stack].pop()
            forklift.append(box)
        
        for box in reversed(forklift):
            crate_array[to_stack].append(box)

        print(parsed_instruction)

    # get finalized output
    crate_string = ""
    
    for stack in crate_array:
        crate_string += stack.pop()
    
    print(crate_string)