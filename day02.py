

def read_input(filepath):
    with open(filepath) as f:
        res = []
        for line in f:
            l = line.strip().split(" ")
            m, mm = l[0].split("-")
            res.append([int(m), int(mm), l[1][0], l[2]])
    return res


def solve(input):
    return sum(
        a <= password.count(letter) <= b
        for a, b, letter, password in input
    )


def solve2(input):
    return sum(
        (password[a - 1] == letter) != (password[b - 1] == letter)
        for a, b, letter, password in input
    )


if __name__ == "__main__":
    input = read_input("day02.txt")
    print(f"Part1: {solve(input)}")
    print(f"Part2: {solve2(input)}")
