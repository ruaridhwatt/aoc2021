def step_point(point, target):
    result = []
    for a, b in zip(point, target):
        if a < b:
            result.append(a + 1)
        elif a > b:
            result.append(a - 1)
        else:
            result.append(a)
    return tuple(result)


def points_between(p1, p2):
    p = p1
    while p != p2:
        yield p
        p = step_point(p, p2)
    yield p


def day5a():
    with open('day5.input') as f:
        point_counts = dict()
        for line in f:
            p1, p2 = line.split(' -> ')
            p1 = tuple(int(coord) for coord in p1.split(','))
            p2 = tuple(int(coord) for coord in p2.split(','))
            if p1[0] == p2[0] or p1[1] == p2[1]:
                for p in points_between(p1, p2):
                    if p in point_counts.keys():
                        point_counts[p] += 1
                    else:
                        point_counts[p] = 1
        nr_overlaps = 0
        for point, count in point_counts.items():
            if count > 1:
                nr_overlaps += 1
        return nr_overlaps


def day5b():
    with open('day5.input') as f:
        point_counts = dict()
        for line in f:
            p1, p2 = line.split(' -> ')
            p1 = tuple(int(coord) for coord in p1.split(','))
            p2 = tuple(int(coord) for coord in p2.split(','))
            for p in points_between(p1, p2):
                if p in point_counts.keys():
                    point_counts[p] += 1
                else:
                    point_counts[p] = 1
        nr_overlaps = 0
        for point, count in point_counts.items():
            if count > 1:
                nr_overlaps += 1
        return nr_overlaps


if __name__ == '__main__':
    print(day5a())
    print(day5b())
