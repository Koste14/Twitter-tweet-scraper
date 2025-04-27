import undetected_chromedriver as uc

EMAIL = 'your_email@example.com'
USERNAME = 'your_username_or_phone'
PASSWORD = 'your_password'
TWITTER_URL = 'https://x.com/i/flow/login'
CELEBRITY_NAME = 'Luka Doncic'
AMOUNT_OF_TWEETS = 200
FILE_LOCATION = 'PATH/twitter_tweets.xlsx'

def setup_driver():
    options = uc.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36')
    return uc.Chrome(options=options)