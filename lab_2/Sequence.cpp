#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>

/**
 * Generates a random binary sequence of length 128 bits
 * and saves it to the file "cpp_seq.txt".
 *
 * This program initializes the random number generator using the current time
 * and generates a sequence of 0 or 1.
 * The generated sequence is written to a text file named "cpp_seq.txt".
 *
 * @return int Returns 0 upon successful completion of the program.
 */
int main() {
    std::srand(static_cast<unsigned int>(std::time(0)));
    std::ofstream outFile("cpp_seq.txt");
    for (int i = 0; i < 128; i++)
        outFile << std::rand() % 2;
    outFile.close();
    return 0;
}
