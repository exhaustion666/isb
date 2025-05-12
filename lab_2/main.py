from constants import *
from nist import *


def main():
    results = []
    results.append(("Frequency Bitwise Test (C++)", freq_bitwise_test(CPP_SEQ)))
    results.append(("Same Bits Test (C++)", same_bits_test(CPP_SEQ)))
    results.append(("Longest Test (C++)", longest_test(CPP_SEQ)))
    results.append(("Frequency Bitwise Test (Java)", freq_bitwise_test(JAVA_SEQ)))
    results.append(("Same Bits Test (Java)", same_bits_test(JAVA_SEQ)))
    results.append(("Longest Test (Java)", longest_test(JAVA_SEQ)))
    write_results(results, RESULT_FILE)


if __name__ == "__main__":
    main()
