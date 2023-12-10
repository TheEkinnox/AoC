#include <fstream>
#include <iostream>
#include <string>

#include "config.h"

int main()
{
    std::string input;
    std::ifstream file;

    do
    {
        std::cout << "Enter input path: " << std::endl;
        std::getline(std::cin, input);

        file.open(input);

        if (!file.is_open())
            std::cerr << "Invalid file path..." << std::endl;
    }
    while (!file.is_open());

    int sum = 0;
    size_t powSum = 0;
    constexpr Config config = { 12, 13, 14 };

    while (std::getline(file, input))
    {
        const Game game(input);
        const size_t pow = game.m_config.getPower();
        std::cout << "{|" << pow << "|}";
        powSum += pow;

        if (!isPossible(config, game.m_config))
            continue;

        const int val = game.m_id;
        std::cout << '[' << val << ']';
        sum += val;
    }

    std::cout << "\nSum: " << sum << " | Powers sum: " << powSum << std::endl;

    return 0;
}
