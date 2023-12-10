#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#include "utility.h"

std::vector<int> getNumbers(const std::string& line)
{
    if (line.empty())
        return {};

    const std::vector<std::string> valStrings = splitString(line, " ", false);

    if (valStrings.empty())
        return {};

    std::vector<int> numbers;
    numbers.reserve(valStrings.size());

    for (const std::string& valString : valStrings)
    {
        int num = std::stoi(valString);
        numbers.push_back(num);
    }

    return numbers;
}

int getPoints(const std::string& line)
{
    if (line.empty())
        return 0;

    std::vector<std::string> hand = splitString(line, ":", false);

    if (hand.size() < 2)
        return 0;

    hand = splitString(hand[1], "|", false);

    if (hand.size() != 2)
        return 0;

    const std::vector<int> card = getNumbers(hand[0]);
    const std::vector<int> numbers = getNumbers(hand[1]);

    int points = 0;

    for (const int num : numbers)
    {
        if (std::ranges::find(card, num) != card.end())
        {
            if (points == 0)
                points = 1;
            else
                points *= 2;
        }
    }

    return points;
}

int main()
{
    std::string   input;
    std::ifstream file;

    do
    {
        std::cout << "Enter input path: " << '\n';
        std::getline(std::cin, input);

        file.open(input);

        if (!file.is_open())
            std::cerr << "Invalid file path..." << '\n';
    }
    while (!file.is_open());

    int sum = 0;

    while (std::getline(file, input))
        sum += getPoints(input);

    std::cout << "\nSum: " << sum << '\n';

    return 0;
}
