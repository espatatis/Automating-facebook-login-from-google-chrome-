from selenium import webdriver

udriver = webdriver.Chrome()
udriver.get('https://www.facebook.com/')
user_id = udriver.find_element_by_id('email')
user_id.send_keys('rohans.mike')
pasword = udriver.find_element_by_id('pass')
pasword.send_keys('nautankisala3')
pasword.submit()
print(udriver.current_url)