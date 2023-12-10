#include <fstream>
#include <iostream>
#include <string>

int getCalibrationValueV1(const std::string& line)
{
    if (line.empty())
        return 0;

    int calibrationValue = 0;
    bool hasFirst = false, hasLast = false;
    const size_t lineSize = line.size();

    for (size_t i = 0; (!hasFirst || !hasLast) && i < lineSize; ++i)
    {
        if (!hasFirst && isdigit(line[i]))
        {
            hasFirst = true;
            calibrationValue += (line[i] - '0') * 10;
        }

        if (!hasLast && isdigit(line[lineSize - i - 1]))
        {
            hasLast = true;
            calibrationValue += line[lineSize - i - 1] - '0';
        }
    }

    return calibrationValue;
}

int getDigit(const std::string& str)
{
    if (str.empty())
        return -1;

    if (isdigit(str[0]))
        return str[0] - '0';

    static const char* digits[] = { "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };

    for (int8_t i = 0; i < 10; ++i)
    {
        const char* digit = digits[i];
        const size_t len = strlen(digit);

        if (len > str.size())
            continue;

        bool isEqual = true;

        for (size_t j = 0; j < len; ++j)
        {
            if (digit[j] != str[j])
            {
                isEqual = false;
                break;
            }
        }

        if (isEqual)
            return i;
    }

    return -1;
}

int getCalibrationValueV2(const std::string& line)
{
    if (line.empty())
        return 0;

    int calibrationValue = 0;
    bool hasFirst = false, hasLast = false;
    const size_t lineSize = line.size();

    for (size_t i = 0; (!hasFirst || !hasLast) && i < lineSize; ++i)
    {
        if (!hasFirst)
        {
            const int digit = getDigit(line.substr(i));

            if (digit >= 0)
            {
                hasFirst = true;
                calibrationValue += digit * 10;
            }
        }

        if (!hasLast)
        {
            const int digit = getDigit(line.substr(lineSize - 1 - i));

            if (digit >= 0)
            {
                hasLast = true;
                calibrationValue += digit;
            }
        }
    }

    return calibrationValue;
}

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

    while (std::getline(file, input))
    {
        // const int val = getCalibrationValueV1(input);
        const int val = getCalibrationValueV2(input);
        std::cout << '[' << val << ']';
        sum += val;
    }

    std::cout << "\nSum: " << sum << std::endl;

    return 0;
}
