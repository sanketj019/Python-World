from selenium import webdriver
chrome_browser = webdriver.Chrome('E:/TY Classwork/python/chromedriver')
chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title

show_button=chrome_browser.find_element_by_class_name('btn-default')
#print(button_text.get_attribute('innerHTML'))

user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('I AM COOOL')
show_button.click()
output_message = chrome_browser.find_element_by_id('display')
print(output_message)