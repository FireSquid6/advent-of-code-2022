

def cycle(amount):
    pass


with open("./test-input.txt") as file:
    cycle = 0
    cooldown = 20
    register = 1
    total_strength = 0
    
    for i, line in enumerate(file):
        line = line.strip()

        if "noop" in line:
            cycle += 1
        elif "addx" in line:
            cycle += 2
            number = int(line.split(" ")[1])
            register += number
            
            print(number)
        
        if cooldown == 0:

            cooldown = 40

        cooldown -= 1
