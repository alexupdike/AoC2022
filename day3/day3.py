import string
from itertools import islice

def part1():
    sum = 0
    alphaMap = {}

    def generateAlphaMap():
        for index, letter in enumerate(string.ascii_lowercase, 1):
            alphaMap[letter] = index
        for index, letter in enumerate(string.ascii_uppercase, 1):
            alphaMap[letter] = index + 26

    def findItem(code, breakPoint):
        for char in code:
                for index in range(breakPoint, len(code)):
                    if char == code[index]:
                        return char

    generateAlphaMap()

    with open("input.txt") as file:
        for line in file:
            current = line.rstrip()
            division = int(len(current)/2)
            item = findItem(current, division)
            sum = sum + alphaMap[item]
    return sum

print("Part 1 sum: ", part1())

def part2():
    sum, length, counter = 0, 0, 0
    alphaMap = {}

    def generateAlphaMap():
        for index, letter in enumerate(string.ascii_lowercase, 1):
            alphaMap[letter] = index
        for index, letter in enumerate(string.ascii_uppercase, 1):
            alphaMap[letter] = index + 26

    def findBadge(code):
        for first in code[0]:
                for second in code[1]:
                    if first == second:
                        for third in code[2]:
                            if first == third:
                                return first

    generateAlphaMap()

    with open("input.txt") as file:
        length = len(file.readlines())

    with open("input.txt") as file:
        while(counter < length):
            head = list(x.rstrip('\n') for x in islice(file, 3))
            badge = findBadge(head)
            sum = sum + alphaMap[badge]
            counter = counter + 3
    return sum

print("Part 2 sum: ", part2())