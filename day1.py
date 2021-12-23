def day1a():
    with open('day1.input') as f:
        depths = [int(d) for d in f]
    diffs = [depths[i + 1] - depths[i] for i in range(0, len(depths) - 1)]
    increases = [diff for diff in diffs if diff > 0]
    return len(increases)


def day1b():
    with open('day1.input') as f:
        depths = [int(d) for d in f]
    diffs = [sum(depths[i + 1:i + 4]) - sum(depths[i:i + 3]) for i in range(0, len(depths) - 3)]
    increases = [diff for diff in diffs if diff > 0]
    return len(increases)


if __name__ == '__main__':
    print(day1a())
    print(day1b())
