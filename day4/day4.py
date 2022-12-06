def part1():
    area1, area2 = [], []
    counter = 0

    def doAreasOverlap(x, y):
        if int(x[0]) >= int(y[0]) and int(x[1]) <= int(y[1]):
            return True
        if int(x[0]) <= int(y[0]) and int(x[1]) >= int(y[1]):
            return True
        return False

    with open("input.txt") as file:
        for line in file:
            current = line.rstrip().split(",")
            area1, area2 = current[0].split("-"), current[1].split("-")
            if doAreasOverlap(area1, area2): counter += 1
    return counter

print("Part 1 sum: ", part1())

def part2():
    area1, area2 = [], []
    counter = 0

    def doAreasOverlap(x, y):
        if int(x[0]) >= int(y[0]) and int(x[1]) <= int(y[1]):
            return True
        if int(x[0]) <= int(y[0]) and int(x[1]) >= int(y[1]):
            return True
        if int(x[0]) >= int(y[0]) and int(x[0]) <= int(y[1]):
            return True
        if int(x[1]) >= int(y[0]) and int(x[1]) <= int(y[1]):
            return True
        return False

    with open("input.txt") as file:
        for line in file:
            current = line.rstrip().split(",")
            area1, area2 = current[0].split("-"), current[1].split("-")
            if doAreasOverlap(area1, area2): counter += 1
    return counter

print("Part 2 sum: ", part2())