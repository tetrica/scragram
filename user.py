import random
import time
from selenium import webdriver
from selenium.common import exceptions as error

class User:
    def __init__(self, username, password):
        self._username = username
        self._password = password
        self._driver = None

    def login(self):
        driver = webdriver.Chrome()

        try:
            driver.get('https://www.instagram.com/accounts/login/')
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

                try:
                    if self._driver.find_element_by_class_name('_qv64e').text == 'Seguir':
                        time.sleep(random.randint(7, 10))
                        self._driver.find_element_by_class_name('_qv64e').click()
                        time.sleep(random.randint(7, 10))
                except error.WebDriverException:
                    print("<<<ERRO>>>", url_follower, "<<<ERRO>>>")
        
    def like(self, pathfile):
        total_likes = 0

        with open(pathfile, 'r') as __file:
            for url in __file:
                self._driver.get(url)
                self._driver.find_element_by_class_name('_mck9w').click()

                for i in range(50):
                    try:
                        time.sleep(1)
                        self._driver.find_element_by_xpath("//section/a/span").click()
                        time.sleep(1)
                        self._driver.find_element_by_class_name('_3a693').click()
                        total_likes += 1
                    except error.WebDriverException:
                        print("!Erro ao tentar curtir!")
                        time.sleep(5)
                        break

                time.sleep(60)

        print(str(total_likes), "foto(s) curtida(s)")