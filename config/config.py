import undetected_chromedriver as uc

EMAIL = 'your_email@example.com'
USERNAME = 'your_username'
PASSWORD = 'your_password'
TWITTER_URL = 'https://x.com/i/flow/login'

def setup_driver():
    options = uc.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36')
    return uc.Chrome(options=options)