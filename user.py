import json
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

    def _scraping_profile(self, user, id):
        self._driver.get('https://www.instagram.com/{}/?__a=1'.format(user))
        pre = self._driver.find_element_by_tag_name("pre").text
        user_data = json.loads(pre)['user']
        graphql_followers = ('https://www.instagram.com'
            '/graphql/query/?query_id={}'.format(id))
        all_profiles = []
        variables = {}
        variables['id'] = user_data['id']
        variables['first'] = 3000
        has_next_data = True
        while has_next_data:
            url = '{}&variables={}'.format(
                graphql_followers, str(json.dumps(variables))
                )
            self._driver.get(url)
            pre = self._driver.find_element_by_tag_name("pre").text
            data = json.loads(pre)['data']
            page_info = (data['user']['edge_followed_by']['page_info'])
            edges = data['user']['edge_followed_by']['edges']
            for user in edges:
                all_profiles.append(user['node']['username'])
            
            has_next_data = page_info['has_next_page']
            if has_next_data:
                variables['after'] = page_info['end_cursor']
        
        return all_profiles

        def scraping_followers_profile(self, user):
            self._scraping_profile(user, '17851374694183129')
        
        def scraping_followings_profile(self, user):
            self._scraping_profile(user, '17874545323001329')