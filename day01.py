import itertools


def read_input(filepath):
    with open(filepath) as f:
        return [int(line) for line in f]


def solve(input):
    for x, y in itertools.combinations(input, 2):
        if x + y == 2020:
            return x * y


def solve2(input):
    for x, y, z in itertools.combinations(input, 3):
        if x + y + z == 2020:
            return x * y * z


if __name__ == "__main__":
    input = read_input("day01.txt")
    print(f"Part1: {solve(input)}")
    print(f"Part2: {solve2(input)}")
