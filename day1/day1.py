def part1():
    max, counter, current = 0, 0, 0

    with open("input.txt") as file:
        for line in file:
            current = line.rstrip()
            if not current:
                if counter > max: max = counter
                counter = 0
            else:
                counter = counter + int(current)
        
    return max

print("Part 1 max: ", part1())

def part2():
    counter, current = 0, 0
    stack = []

    with open("input.txt") as file:
        for line in file:
            current = line.rstrip()
            if not current:
                stack.append(counter)
                counter = 0
            else:
                counter = counter + int(current)

    stack.sort(reverse=True)

    return sum(stack[0:3])

print("Part 2 total: ", part2())