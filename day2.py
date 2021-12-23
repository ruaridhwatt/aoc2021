
def day2a():
    y = 0
    z = 0
    with open('day2.input') as input:
        for line in input:
            match line.split(' '):
                case 'up', dist:
                    y -= int(dist)
                case 'down', dist:
                    y += int(dist)
                case 'forward', dist:
                    z += int(dist)
    return z * y


def day2b():
    y = 0
    z = 0
    aim = 0
    with open('day2.input') as input:
        for line in input:
            match line.split(' '):
                case 'up', dist:
                    aim -= int(dist)
                case 'down', dist:
                    aim += int(dist)
                case 'forward', dist:
                    z += int(dist)
                    y += aim * int(dist)
    return z * y


if __name__ == '__main__':
    print(day2a())
    print(day2b())
