#include "config.h"

#include <sstream>

#include "utility.h"

void Config::parse(const std::string& line)
{
    m_redCount = 0;
    m_greenCount = 0;
    m_blueCount = 0;

    if (line.empty())
        return;

    const std::vector<std::string> tokens = splitString(line, ",", false);

    for (const auto& token : tokens)
    {
        std::vector<std::string> entry = splitString(token, " ", false);

        if (entry.size() != 2)
            continue;

        const int count = std::stoi(entry[0]);

        if (entry[1] == "red")
            m_redCount += count;
        else if (entry[1] == "green")
            m_greenCount += count;
        else if (entry[1] == "blue")
            m_blueCount += count;
    }
}

size_t Config::getPower() const
{
    return static_cast<size_t>(m_redCount) * m_greenCount * m_blueCount;
}

Game::Game(const std::string& line)
{
    m_id = 0;
    m_config = { 0, 0, 0 };

    if (line.empty())
        return;

    bool hasDigit = false;
    size_t offset = 0;

    for (; offset < line.length(); ++offset)
    {
        if (isdigit(line[offset]))
        {
            hasDigit = true;
            m_id = m_id * 10 + (line[offset] - '0');
        }
        else if (hasDigit)
        {
            break;
        }
    }

    const std::vector<std::string> entries = splitString(line.substr(offset + 1), ";", false);
    Config cfg;

    for (const auto& entry : entries)
    {
        cfg.parse(entry);

        m_config.m_redCount = std::max(cfg.m_redCount, m_config.m_redCount);
        m_config.m_greenCount = std::max(cfg.m_greenCount, m_config.m_greenCount);
        m_config.m_blueCount = std::max(cfg.m_blueCount, m_config.m_blueCount);
    }
}
