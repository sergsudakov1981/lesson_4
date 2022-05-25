#### Регистрация аккаунта ####

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("http://practice.automationtesting.in/")
#
# my_account = driver.find_element(By.ID, 'menu-item-50')
# my_account.click()
#
# time.sleep(5)
#
# reg_email = driver.find_element(By.ID, 'reg_email')
# reg_email.send_keys('1A2B3C@mail.ru')
#
# reg_password = driver.find_element(By.ID, 'reg_password')
# reg_password.send_keys('GhTyUi9734R')
#
# register = driver.find_element(By.NAME, 'register')
# register.click()
#
# driver.quit()

#### Логин в систему ####

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("http://practice.automationtesting.in/")
#
# my_account = driver.find_element(By.ID, 'menu-item-50')
# my_account.click()
#
# username = driver.find_element(By.ID, 'username')
# username.send_keys('1A2B3C@mail.ru')
#
# password = driver.find_element(By.ID, 'password')
# password.send_keys('GhTyUi9734R')
#
# login = driver.find_element(By.NAME, 'login')
# login.click()
#
# logout = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'woocommerce-MyAccount-navigation-link--customer-logout')))
# logout_text = logout.text
# assert logout_text == 'Logout'
# print(logout_text, 'присутствует')
#
# driver.quit()





