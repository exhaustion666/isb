from load_constants import *
from nist import *


def main():
    """
    Adds the NIST test results to an array and writes it to a file.
    """
   constants = load_constants('constants.json')
    CPP_SEQ = constants['CPP_SEQ']
    CPP_SEQ2 = constants['CPP_SEQ2']
    JAVA_SEQ = constants['JAVA_SEQ']
    JAVA_SEQ2 = constants['JAVA_SEQ2']
    BLOCK_SIZE = constants['BLOCK_SIZE']
    EXPECT_PI = constants['EXPECT_PI']
    RESULT_FILE = constants['RESULT_FILE']
    RESULT_FILE2 = constants['RESULT_FILE2']

    results = []
    results.append(("Frequency Bitwise Test (C++)", freq_bitwise_test(CPP_SEQ)))
    results.append(("Same Bits Test (C++)", same_bits_test(CPP_SEQ)))
    results.append(("Longest Test (C++)", longest_test(CPP_SEQ, BLOCK_SIZE, EXPECT_PI)))
    results.append(("Frequency Bitwise Test (Java)", freq_bitwise_test(JAVA_SEQ)))
    results.append(("Same Bits Test (Java)", same_bits_test(JAVA_SEQ)))
    results.append(("Longest Test (Java)", longest_test(JAVA_SEQ, BLOCK_SIZE, EXPECT_PI)))
    
    results2 = []
    results2.append(("Frequency Bitwise Test (C++)", freq_bitwise_test(CPP_SEQ2)))
    results2.append(("Same Bits Test (C++)", same_bits_test(CPP_SEQ2)))
    results2.append(("Longest Test (C++)", longest_test(CPP_SEQ2, BLOCK_SIZE, EXPECT_PI)))
    results2.append(("Frequency Bitwise Test (Java)", freq_bitwise_test(JAVA_SEQ2)))
    results2.append(("Same Bits Test (Java)", same_bits_test(JAVA_SEQ2)))
    results2.append(("Longest Test (Java)", longest_test(JAVA_SEQ2, BLOCK_SIZE, EXPECT_PI)))
    
    write_results(results, RESULT_FILE)
    write_results(results2, RESULT_FILE2)
    

if __name__ == "__main__":
    main()
