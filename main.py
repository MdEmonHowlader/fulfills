def solve_case(x, y):
    parts = y.split()
    if len(parts) != int(x):
        return -1
    values = map(int, parts)
    non_positive = filter(lambda v: v <= 0, values)
    return sum(map(lambda v: v ** 4, non_positive))


def read_case(_):
    x = input()
    y = input()
    return solve_case(x, y)


def main():
    n = int(input())
    results = list(map(read_case, range(n)))
    print("\n".join(map(str, results)))


if __name__ == "__main__":
    main()