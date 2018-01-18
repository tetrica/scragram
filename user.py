import random
import time
from selenium import webdriver
from selenium.common import exceptions as error

class User:
    """\tRepresents a instagram user 
    
        This class represents a instagram user and can following or send 
        messages to outhers users

        Attributes:
            username: Name, cell phone number or e-mail used to login
                      on instagram
            password: password of instagram account
    """
    def __init__(self, username, password):
        """\tConstructor

            Args:
                username: Name, cell phone number or e-mail used to login
                      on instagram
                password: password of instagram account
        """
        self._username = username
        self._password = password
        self._driver = None

    def login(self):
        """\tLogin a user account"""
        driver = webdriver.Chrome()
        INSTAGRAM_URL = "https://www.instagram.com/accounts/login/"

        try:
            driver.get(INSTAGRAM_URL)
            driver.find_element_by_name("username").clear()
            driver.find_element_by_name("username").send_keys(self._username)
            driver.find_element_by_name("password").clear()
            driver.find_element_by_name("password").send_keys(self._password)
            driver.find_element_by_class_name('_qv64e').click()
            time.sleep(random.randint(1, 5))
        except error.WebDriverException:
            print("Erro ao realizar login!")
        
        self._driver = driver

    def follow(self, pathfile):
        with open(pathfile, 'r') as urls_followers:
            for i, url_follower in enumerate(urls_followers):
                print(str(i), '-', url_follower)
                self._driver.get(url_follower)
                time.sleep(7)
                self._driver.find_element_by_class_name('_qv64e').click()
                time.sleep(7)