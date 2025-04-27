import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import pandas as pd
import config.config as config

# Setting up Chrome options and passing them to uc

def login_to_twitter(driver):

    driver.get(config.TWITTER_URL) # twitter login url

    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/button/span/span')))

    # Finding enail box to enter text and entering email
    email_box = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
    email_box.send_keys(config.EMAIL)
    time.sleep(1)
    email_box.send_keys(Keys.ENTER)
    time.sleep(2)

# Checking if additional check pops up that required to confirm username/phone
    try:
        phone_username_confirm = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        phone_username_confirm.send_keys(config.USERNAME)
        time.sleep(1)
        phone_username_confirm.send_keys(Keys.ENTER)
    except:
        pass

    # Waiting for password box to show up and entering password
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')))
    password = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    password.send_keys(config.PASSWORD)
    time.sleep(1)
    password.send_keys(Keys.ENTER)
    time.sleep(3)
    # Declining optional cookies
    cookie_reject = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div[2]/div/div/div/div[2]/button[2]')
    time.sleep(1)
    cookie_reject.click()

def retry_button(driver):
    try:
        driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div[3]/button').click()
    except NoSuchElementException:
        pass

def searching_celebrity(driver, celebrity_name):

    # Finding search box element in twitter page and entering string into the field
    search_box = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/div/div[2]/div/input')
    search_box.send_keys(celebrity_name)
    time.sleep(1)
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)

    # Clicking on the "People" tab in the search tab
    driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[3]').click()
    time.sleep(2)
    # Clicking the 1st option of the search
    driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/section/div/div/div[1]').click()
    time.sleep(2)

    # clicking retry button in case it appears
    retry_button(driver)

def getting_tweets(driver, tweet_limit):
    # Setting empty set and list to find and store unique strings
    uniqueTweets = set()
    rows = []

    while True:
        # Getting current page content and finding posts that will return tweet text
        soup = BeautifulSoup(driver.page_source, 'lxml')
        posts = soup.find_all('div', class_ = 'css-146c3p1 r-8akbws r-krxsd3 r-dnmrzs r-1udh08x r-1udbk01 r-bcqeeo r-1ttztb7 r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-16dba41 r-bnwqim')
        
        # Going through each tweet on current page source and getting tweets, then checking if it's not empty and is not in uniqueTweets, if not adding it to rows and uniqueTweets
        for tweets in posts:
            try:
                tweet = tweets.text
                if tweet and tweet not in uniqueTweets:
                    rows.append({'Twitter posts':tweet})
                    uniqueTweets.add(tweet)
            except:
                pass
        # Scrolling logic, to always scroll to document height
        driver.execute_script('window.scrollTo (0, document.body.scrollHeight)')
        time.sleep(2)
        
        # stopping once reaching tweet limit
        if len(uniqueTweets) > tweet_limit:
            break
    return rows

def saving_to_excel(rows, path):
    table = pd.DataFrame(rows)
    table.to_excel(path, index=False)
    print(f"Saved {len(table)} tweets to {path}")


def main():
    driver = config.setup_driver()
    try:
        login_to_twitter(driver)
        searching_celebrity(driver, config.CELEBRITY_NAME)
        tweets = getting_tweets(driver, config.AMOUNT_OF_TWEETS)
        saving_to_excel(tweets, config.FILE_LOCATION)
    finally:
        driver.quit()
        del driver

if __name__ == "__main__":
    main()
        
