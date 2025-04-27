# Twitter celebrity tweet scraper

This python tool automates the process of logging into Twitter (X), then searching for specific person's tweets, which are then saved to the Excel file for easy analysis and viewing.


## Features

- Automated login to Twitter using Selenium & undetected-chromebrowser
- Searches for any celebrity or user by name and selects 1st option on People's tab
- Scrapes unique tweets up to a specified amount
- Saves data to an Excel file ('xlsx')
- Handles dynamic elements, like retry buttons in case of failing to load and optional pop ups

## Requirements

- Python 3.8+
- Google Chrome installed

Python libraries that are needed:
- `undetected-chromedriver`
- `selenium`
- `pandas`
- `beautifulsoup4`
- `lxml`
- `openpyxl`

To install all dependencies use:
```bash
pip install -r requirements.txt
```


## Setup and configuration

1. Clone the repository:

```git clone https://github.com/Koste14/Twitter-tweet-scraper.git```

```cd Twitter-tweet-scraper```


2. Install required dependencies:

```pip install -r requirements.txt```

3. Configure your credentials, file location and other settings in configure.py file:

```EMAIL = 'your_email@example.com'
USERNAME = 'your_username_or_phone'
PASSWORD = 'your_password'
CELEBRITY_NAME = 'Luka Doncic'
TWEET_LIMIT = 200
FILE_LOCATION = 'PATH/twitter_tweets.xlsx'
```

## Usage
Run the script with:
```python src/twitter_scraping.py```
