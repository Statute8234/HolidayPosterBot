# HolidayPosterBot

[![praw](https://img.shields.io/badge/praw-brightgreen)](https://pypi.org/project/praw/)
[![datetime](https://img.shields.io/badge/datetime-yellow)](https://pypi.org/project/DateTime/)
[![holidays](https://img.shields.io/badge/holidays-blue)](https://pypi.org/project/holidays/)
[![wikipedia](https://img.shields.io/badge/wikipedia-orange)](https://pypi.org/project/wikipedia/)
[![pycountry](https://img.shields.io/badge/pycountry-red)](https://pypi.org/project/pycountry/)
[![os](https://img.shields.io/badge/os-purple)](https://pypi.org/project/os-sys/)
[![logging](https://img.shields.io/badge/logging-pink)](https://pypi.org/project/logging/)

Holiday Poster is a Python script that finds and posts holiday details on Reddit, using Wikipedia and the holidays library to fetch holiday summaries.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## About

Holiday Poster is a Python script that finds and posts holiday details on Reddit, using Wikipedia for holiday summaries and the holidays library for holiday data.

## Features

- **Logging:** Detailed logging using Python's logging library, which includes rotating file handlers.
- **Holiday Lookup:** Uses the holidays library to find holidays in various countries.
- **Wikipedia Integration:** Fetches holiday summaries from Wikipedia.
- **Reddit Posting:** Posts holiday details to a specified subreddit.
- **Environment Variable Handling:** Securely handles secret tokens using environment variables.

## Installation

Prerequisites
- Python 3.6 or higher
- Reddit API credentials
- Wikipedia API library
- Holidays library
- Pycountry library

Dependencies

You can install the necessary dependencies using pip:

pip install praw wikipedia holidays pycountry

Configuration

Ensure you have your Reddit API credentials set up in environment variables or within your script securely. For example:

export SOME_SECRET='your_reddit_api_secret'

## Usage

Running the Script

To run the script, simply execute:

python your_script_name.py

## Contributing

Contributions are welcome! To contribute to Monster Maze, follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/YourFeature
   ```
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.