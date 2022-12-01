import os
import heapq

def part1(inventories):
    return max(inventories)

def part2(inventories):
    return sum(heapq.nlargest(3, inventories))

if __name__ == "__main__":
    elves = []
    with open("day1/input.txt", "r") as file:
        elves = list(map(lambda x: sum(map(int, x.splitlines())), file.read().split(os.linesep + os.linesep)))
    
    print("Part 1:", part1(elves))
    print("Part 2:", part2(elves))
