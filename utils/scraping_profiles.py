import json
import time

def _scraping_profile(driver, user, _id):
    driver.get('https://www.instagram.com/{}/?__a=1'.format(user))
    pre = driver.find_element_by_tag_name("pre").text
    user_data = json.loads(pre)['user']
    graphql_followers = ('https://www.instagram.com'
        '/graphql/query/?query_id={}'.format(_id))

    variables = {}
    variables['id'] = user_data['id']
    variables['first'] = 3000
    has_next_data = True

    while has_next_data:
        url = '{}&variables={}'.format(
            graphql_followers, str(json.dumps(variables))
            )

        driver.get(url)
        pre = driver.find_element_by_tag_name("pre").text
        data = json.loads(pre)['data']
        page_info = (data['user']['edge_followed_by']['page_info'])
        edges = data['user']['edge_followed_by']['edges']
        all_profiles = [user['node']['username'] for user in edges]

        has_next_data = page_info['has_next_page']
        if has_next_data: 
            variables['after'] = page_info['end_cursor']
    
    return all_profiles

    def scraping_followers_profile(driver, user):
        return _scraping_profile(driver, user, '17851374694183129')
    
    def scraping_followings_profile(driver, user):
        return _scraping_profile(driver, user, '17874545323001329')