#pragma once
#include <string>

struct Config
{
    int m_redCount;
    int m_greenCount;
    int m_blueCount;

    void parse(const std::string& line);

    size_t getPower() const;
};

struct Game
{
    int m_id;
    Config m_config;

    explicit Game(const std::string& line);
};

inline bool isPossible(const Config config, const Config result)
{
    return config.m_redCount >= result.m_redCount
        && config.m_greenCount >= result.m_greenCount
        && config.m_blueCount >= result.m_blueCount;
}
