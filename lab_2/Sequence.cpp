#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>

int main() {
    std::srand(static_cast<unsigned int>(std::time(0)));
    std::ofstream outFile("cpp_seq.txt");
    for (int i = 0; i < 128; i++)
        outFile << std::rand() % 2;
    outFile.close();
    return 0;
}
