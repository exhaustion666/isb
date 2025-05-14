from constants import *
from scipy.special import gammaincc

import math

def freq_bitwise_test(seq) -> float:
    """
    Frequency bitwise test.

    args:
        seq (str): Source random sequence.

    return:
        p_value (float): P-value of sequence.
    """

    total = sum(1 if var == "1" else -1 for var in seq)
    total /= math.sqrt(len(seq))
    p_value = math.erfc(abs(total) / math.sqrt(2))
    return p_value


def same_bits_test(seq) -> float:
    """
    A test for identical consecutive bits.

    args:
        seq (str): Source random sequence.

    return:
        p_value (float): P-value of sequence.
    """

    count_ones = seq.count('1')
    frac = count_ones / len(seq)
    if abs(frac - 0.5) >= (2 / math.sqrt(len(seq))): return 0.0
    v_n = sum(1 if seq[i] != seq[i+1] else 0 for i in range(len(seq) - 1))
    nom = abs(v_n - 2 * len(seq) * frac * (1 - frac))
    den = 2 * math.sqrt(2 * len(seq)) * frac * (1 - frac)
    p_value = math.erfc(nom / den)
    return p_value


def longest_test(seq) -> float:
    """
    A test for the longest sequence of units in a block.
    
    args:
        seq (str): Source random sequence.

    return:
        p_value (float): P-value of sequence.
    """

    blocks = [seq[i:i + BLOCK_SIZE] for i in range(0, len(seq), BLOCK_SIZE)]
    v = [0, 0, 0, 0]

    for block in blocks:
        max_ones = 0
        cur_ones = 0
        for var in block:
            if var == '1':
                cur_ones += 1
                max_ones = max(max_ones, cur_ones)
            else:
                cur_ones = 0

        match max_ones:
            case 0 | 1: v[0] += 1
            case 2: v[1] += 1
            case 3: v[2] += 1
            case _: v[3] += 1

    hi_sq = sum((v[i] - 16 * EXPECT_PI[i]) ** 2 / (16 * EXPECT_PI[i]) for i in range(4))
    p_value = gammaincc(3 / 2, hi_sq / 2)
    return p_value
