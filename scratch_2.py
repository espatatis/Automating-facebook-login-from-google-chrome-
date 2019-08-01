from selenium import webdriver

udriver = webdriver.Chrome()
udriver.get('https://www.facebook.com/')
user_id = udriver.find_element_by_id('email')
user_id.send_keys('your username')
pasword = udriver.find_element_by_id('pass')
pasword.send_keys('password')
pasword.submit
print(udriver.current_url)
