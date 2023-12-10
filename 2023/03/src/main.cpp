#include <fstream>
#include <iostream>
#include <string>
#include <vector>

int getNum(const std::string& str, const size_t index, const int defaultVal = 0)
{
    if (str.empty() || str.size() <= index || !isdigit(str[index]))
        return defaultVal;

    int num = str[index] - '0';

    size_t offset = 1;
    int    multiplier = 1;
    bool   hasPrev = index >= offset && isdigit(str[index - offset]);
    bool   hasNext = index + offset < str.size() && isdigit(str[index + offset]);

    do
    {
        const size_t prevIdx = index - offset;
        const size_t nextIdx = index + offset;
        ++offset;

        if (hasPrev)
        {
            multiplier *= 10;
            num += (str[prevIdx] - '0') * multiplier;
            hasPrev = index >= offset && isdigit(str[index - offset]);
        }

        if (hasNext)
        {
            num *= 10;
            multiplier *= 10;
            num += str[nextIdx] - '0';
            hasNext = index + offset < str.size() && isdigit(str[index + offset]);
        }
    }
    while (hasPrev || hasNext);

    return num;
}

int getSumV1(const std::vector<std::string>& grid)
{
    if (grid.empty())
        return 0;

    int sum = 0;

    for (size_t row = 0; row < grid.size(); ++row)
    {
        const std::string& line = grid[row];

        if (line.empty())
            continue;

        for (size_t col = 0; col < line.size(); ++col)
        {
            const char c = line[col];

            if (isdigit(c) || isalpha(c) || c == '.')
                continue;

            // Check the previous line
            if (row > 0)
            {
                const std::string& prevLine = grid[row - 1];

                if (isdigit(prevLine[col]))
                {
                    sum += getNum(prevLine, col);
                }
                else
                {
                    if (col > 0)
                        sum += getNum(prevLine, col - 1);

                    if (col < prevLine.size() - 1)
                        sum += getNum(prevLine, col + 1);
                }
            }

            // Check the next line
            if (row < grid.size() - 1)
            {
                const std::string& nextLine = grid[row + 1];

                if (isdigit(nextLine[col]))
                {
                    sum += getNum(nextLine, col);
                }
                else
                {
                    if (col > 0)
                        sum += getNum(nextLine, col - 1);

                    if (col < nextLine.size() - 1)
                        sum += getNum(nextLine, col + 1);
                }
            }

            // Check the current line
            if (col > 0)
                sum += getNum(line, col - 1);

            if (col < line.size() - 1)
                sum += getNum(line, col + 1);
        }
    }

    return sum;
}

int getSumV2(const std::vector<std::string>& grid)
{
    if (grid.empty())
        return 0;

    int sum = 0;

    for (size_t row = 0; row < grid.size(); ++row)
    {
        const std::string& line = grid[row];

        if (line.empty())
            continue;

        for (size_t col = 0; col < line.size(); ++col)
        {
            const char c = line[col];

            if (isdigit(c) || isalpha(c) || c == '.')
                continue;

            int gearRatio = 1;
            int adjacentCount = 0;

            // Check the previous line
            if (row > 0)
            {
                const std::string& prevLine = grid[row - 1];

                if (isdigit(prevLine[col]))
                {
                    const int num = getNum(prevLine, col, -1);

                    if (num != -1)
                    {
                        gearRatio *= num;
                        ++adjacentCount;
                    }
                }
                else
                {
                    if (col > 0)
                    {
                        const int num = getNum(prevLine, col - 1, -1);

                        if (num != -1)
                        {
                            gearRatio *= num;
                            ++adjacentCount;
                        }
                    }

                    if (col < prevLine.size() - 1)
                    {
                        const int num = getNum(prevLine, col + 1, -1);

                        if (num != -1)
                        {
                            gearRatio *= num;
                            ++adjacentCount;
                        }
                    }
                }
            }

            // Check the next line
            if (row < grid.size() - 1)
            {
                const std::string& nextLine = grid[row + 1];

                if (isdigit(nextLine[col]))
                {
                    const int num = getNum(nextLine, col, -1);

                    if (num != -1)
                    {
                        gearRatio *= num;
                        ++adjacentCount;
                    }
                }
                else
                {
                    if (col > 0)
                    {
                        const int num = getNum(nextLine, col - 1, -1);

                        if (num != -1)
                        {
                            gearRatio *= num;
                            ++adjacentCount;
                        }
                    }

                    if (col < nextLine.size() - 1)
                    {
                        const int num = getNum(nextLine, col + 1, -1);

                        if (num != -1)
                        {
                            gearRatio *= num;
                            ++adjacentCount;
                        }
                    }
                }
            }

            // Check the current line
            if (col > 0)
            {
                const int num = getNum(line, col - 1, -1);

                if (num != -1)
                {
                    gearRatio *= num;
                    ++adjacentCount;
                }
            }

            if (col < line.size() - 1)
            {
                const int num = getNum(line, col + 1, -1);

                if (num != -1)
                {
                    gearRatio *= num;
                    ++adjacentCount;
                }
            }

            if (adjacentCount == 2)
                sum += gearRatio;
        }
    }

    return sum;
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

    std::vector<std::string> grid;

    while (std::getline(file, input))
        grid.emplace_back(input);

    std::cout << "\nSum (v1): " << getSumV1(grid) << "\nSum (v2): " << getSumV2(grid) << '\n';

    return 0;
}
