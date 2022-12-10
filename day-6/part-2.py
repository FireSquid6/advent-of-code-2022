with open("./input.txt") as file:
    for line in file:
        last_index = 0
        line = line.strip()
        queue = []

        for i, char in enumerate(line):
            queue.insert(0, char)

            if len(queue) >= 14:
                no_duplicates = True
                for item in queue:
                    if queue.count(item) > 1:
                        no_duplicates = False
                    

                if no_duplicates:
                    last_index = i
                    break
                popped = queue.pop()
            

        print(line)
        print(queue)
        print(last_index + 1)