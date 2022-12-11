correct_answer = "##..##..##..##..##..##..##..##..##..##..###...###...###...###...###...###...###.####....####....####....####....####....#####.....#####.....#####.....#####.....######......######......######......###########.......#######.......#######....."

class CPU:
    cycles = 0
    register = 1
    strengths = []
    crt = [""]
    crt_row = 0
    draw_index = 0

    def cycle(self, amount):
        # START OF CYCLE
        self.cycles += 1

        # DURING CYCLE
        pixel = "."
        if self.draw_index >= self.register - 1 and self.draw_index <= self.register + 1:
            pixel = "#"

        self.crt[self.crt_row] += pixel
        if len(self.crt[self.crt_row]) == 40:
            self.crt_row += 1
            self.crt.append("")
            self.draw_index = -1

        
        self.draw_index += 1
        
        # END OF CYCLE
        self.register += amount
        


with open("./input.txt") as file:
    cpu = CPU()

    for i, line in enumerate(file):
        line = line.strip()
        cpu.cycle(0)
        
        if "addx" in line:
            number = int(line.split(" ")[1])
            cpu.cycle(number)

    print(cpu.cycles)
    merged = ""
    for crt_row in cpu.crt:
        print(crt_row)
        merged += crt_row
    
    print(merged)