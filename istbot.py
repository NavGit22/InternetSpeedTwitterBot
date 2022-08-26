from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

PROMISED_DOWN = 25
PROMISED_UP = 3

class InternetSpeedTwitterBot:
    def __init__(self):
        self.download = 0
        self.upload = 0
        chrome_driver_path = "C:\\chromedriver.exe"
        ser = Service(chrome_driver_path)
        op = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=ser, options=op)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(30)
        go_button = self.driver.find_element(By.CSS_SELECTOR,
                                        "#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.start-button > a > span.start-text")
        go_button.click()
        time.sleep(60)
        down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        self.download = float(down)
        self.upload = float(up)
        print(self.download)
        print(self.upload)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(2)
        email = self.driver.find_element(By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        password = self.driver.find_element(By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
        email.send_keys('*****@*****.****')
        password.send_keys('********')
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        tweet_compose = self.driver.find_element(By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet = f"Hey Internet Provider, why is my internet speed {self.download}down/{self.upload}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)
        tweet_button = self.driver.find_element(By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()
        time.sleep(2)
        self.driver.quit()
