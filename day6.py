import math

import numpy as np


def day6a():
    with open('day6.input') as f:
        state = np.array([int(tts) for tts in f.readline().strip().split(',')])
    for d in range(80):
        state = state - 1
        spawned = state == -1
        nr_spawned = np.sum(spawned)
        state[spawned] = 6
        state = np.append(state, np.repeat(8, nr_spawned))
    return state.shape[0]


def nr_spawns(first_time_to_spawn, normal_time_to_spawn, nr_days, initial_time_to_spawn=None):
    if initial_time_to_spawn is None:
        initial_time_to_spawn = first_time_to_spawn
    result = 0
    if nr_days < initial_time_to_spawn:
        return result
    result += math.floor((nr_days + normal_time_to_spawn - initial_time_to_spawn) / normal_time_to_spawn)
    nr_days -= initial_time_to_spawn
    result += nr_spawns(first_time_to_spawn, normal_time_to_spawn, nr_days)
    nr_days -= normal_time_to_spawn
    while nr_days > 0:
        result += nr_spawns(first_time_to_spawn, normal_time_to_spawn, nr_days)
        nr_days -= normal_time_to_spawn
    return result


def nr_spawns_2(x, y, z, d):
    result = 0
    i = 0
    j = 0
    while True:
        while True:
            result += math.floor((d - x - i*y - j*z) / y)
            j += 1
            if (d - x - i*y - j*z) / y < 1:
                break
        i += 1
        if (d - x - i * y - j * z) / y < 1:
            break
    return result


def day6b():
    with open('day6.input') as f:
        state = np.array([int(n) for n in f.readline().strip().split(',')])
    nr_lanternfish = 0
    divisions = [0 for _ in range(257)]
    for day in state:
        nr_lanternfish += 1
        divisions[day + 1] += 1
    for day, nr_divisions in enumerate(divisions):
        nr_lanternfish += nr_divisions
        if day + 7 < 257:
            divisions[day + 7] += nr_divisions
        if day + 9 < 257:
            divisions[day + 9] += nr_divisions
    return nr_lanternfish


if __name__ == '__main__':
    print(day6a())
    print(day6b())
