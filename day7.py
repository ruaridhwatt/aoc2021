import numpy as np


def day7a():
    with open('day7.input') as f:
        crabs_positions = np.array([int(n) for n in f.readline().strip().split(',')])
    positions = np.array([p for p in range(np.min(crabs_positions), np.max(crabs_positions))])
    crabs_positions = np.tile(crabs_positions, (positions.shape[0], 1))
    fuel_per_crab = np.abs((crabs_positions.transpose() - positions).transpose())
    fuel = np.sum(fuel_per_crab, 1)
    return np.min(fuel)


def get_fuel_per_crab(crab_positions, target_position):
    distances = np.abs(crab_positions - target_position)
    return (distances * (distances + 1)) // 2


def day7b():
    with open('day7.input') as f:
        crabs_positions = np.array([int(n) for n in f.readline().strip().split(',')])
    positions = np.array([p for p in range(np.min(crabs_positions), np.max(crabs_positions))])
    crabs_positions = np.tile(crabs_positions, (positions.shape[0], 1))
    fuel_per_crab = np.array([get_fuel_per_crab(v, p) for p, v in enumerate(crabs_positions)])
    fuel = np.sum(fuel_per_crab, 1)
    return np.min(fuel)


if __name__ == '__main__':
    print(day7a())
    print(day7b())
