import numpy as np


def day3a():
    with open('day3.input') as f:
        digits = np.array([[c for c in n[:-1]] for n in f])
    zeros_hist = np.sum(digits == '0', 0)
    ones_hist = np.sum(digits == '1', 0)
    gamma_rate = int(''.join(['0' if zeros > ones else '1' for zeros, ones in zip(zeros_hist, ones_hist)]), 2)
    epsilon_rate = int(''.join(['0' if zeros < ones else '1' for zeros, ones in zip(zeros_hist, ones_hist)]), 2)
    return gamma_rate * epsilon_rate


def filter_candidates(candidates, mask_func, mask_length):
    zeros_hist = np.sum(candidates == '0', 0)
    ones_hist = np.sum(candidates == '1', 0)
    mask = np.copy(candidates[0, :mask_length])
    mask[-1] = mask_func(zeros_hist[mask_length - 1], ones_hist[mask_length - 1])
    candidates_comparable = candidates[:, :mask_length]
    return candidates[np.all(candidates_comparable == mask, 1)]


def day3b():
    with open('day3.input') as f:
        digits = np.array([[c for c in n[:-1]] for n in f])

    o2_rating_candidates = digits
    co2_scrubber_rating_candidates = digits

    for mask_length in range(1, digits.shape[1] + 1):
        if o2_rating_candidates.shape[0] > 1:
            o2_rating_candidates = filter_candidates(o2_rating_candidates,
                                                     lambda zeros, ones: '0' if zeros > ones else '1',
                                                     mask_length)
        if co2_scrubber_rating_candidates.shape[0] > 1:
            co2_scrubber_rating_candidates = filter_candidates(co2_scrubber_rating_candidates,
                                                               lambda zeros, ones: '0' if zeros <= ones else '1',
                                                               mask_length)
        if o2_rating_candidates.shape[0] == 1 and co2_scrubber_rating_candidates.shape[0] == 1:
            break
    o2_rating = int(''.join(o2_rating_candidates[0]), 2)
    co2_scrubber_rating = int(''.join(co2_scrubber_rating_candidates[0]), 2)
    return o2_rating * co2_scrubber_rating


if __name__ == '__main__':
    print(day3a())
    print(day3b())
