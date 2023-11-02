from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# global variables
driver = webdriver.Edge()
driver.get('http://127.0.0.1:443/') #change the url to your own url

# def for login
def login():
    element_username = driver.find_element(By.NAME, 'username')
    element_username.send_keys('admin')
    time.sleep(2)
    element_password = driver.find_element(By.NAME, 'password')
    element_password.send_keys('password')
    time.sleep(2)
    element_submit = driver.find_element(By.NAME, 'Login')
    time.sleep(2)
    element_submit.click()
    time.sleep(5)

# def for normal browsing activity
# user will just click stuff, nothing else
def click_urls(name_index):
    # so each url is enclosed in <a> tag with href attribute
    # we need to do something equivalent to window.location.href = 'url'
    # we just need to change the input url of the browser to the name params
    names = ['', 'instructions.php', 'setup.php', 'vulnerabilities/brute/', 'vulnerabilities/exec/', 'vulnerabilities/csrf', 'vulnerabilities/fi/?page=include.php', 'vulnerabilities/upload/', 'vulnerabilities/captcha' , 'vulnerabilities/sqli', 'vulnerabilities/sqli_blind', 'vulnerabilities/xss_r', 'vulnerabilities/xss_s', 'security.php', 'phpinfo.php', 'about.php']
    driver.get('http://127.0.0.1:443/' + names[name_index])
    time.sleep(5)




# element = driver.find_element(By.ID, 'sb_form_q')
# element.send_keys('WebDriver')
# element.submit()

# so now i want to login into damm vulnerable web applications
# it has 2 inputs with name username and password
# and a submit button with name submit
# element_username = driver.find_element(By.NAME, 'username')
# element_username.send_keys('admin')
# time.sleep(2)
# element_password = driver.find_element(By.NAME, 'password')
# element_password.send_keys('password')
# time.sleep(2)
# element_submit = driver.find_element(By.NAME, 'Login')
# time.sleep(2)
# element_submit.click()

# first login
# login()
# then clicking
for i in range(0, 16):
    if i == 0:
        login()

    else:
        click_urls(i)


time.sleep(5)
driver.quit()