#### Отображение страницы товара ####

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
# username = driver.find_element(By.ID, 'username')
# username.send_keys('1A2B3C@mail.ru')
#
# password = driver.find_element(By.ID, 'password')
# password.send_keys('GhTyUi9734R')
#
# login = driver.find_element(By.NAME, 'login')
# login.click()
#
# shop = driver.find_element(By.ID, 'menu-item-40')
# shop.click()
#
# html_5_forms = driver.find_element(By.CSS_SELECTOR, '[alt="Mastering HTML5 Forms"]')
# html_5_forms.click()
#
# title = driver.find_element(By.CLASS_NAME,'product_title')
# title_text = title.text
# assert title_text == 'HTML5 Forms'
#
# driver.quit()

#### Количество товаров в категории ####

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
# username = driver.find_element(By.ID, 'username')
# username.send_keys('1A2B3C@mail.ru')
#
# password = driver.find_element(By.ID, 'password')
# password.send_keys('GhTyUi9734R')
#
# login = driver.find_element(By.NAME, 'login')
# login.click()
#
# shop = driver.find_element(By.ID, 'menu-item-40')
# shop.click()
#
# html_btn = driver.find_element(By.CSS_SELECTOR,'.cat-item-19 a')
# html_btn.click()
#
# product = driver.find_elements(By.CLASS_NAME, 'woocommerce-LoopProduct-link')
# if len(product) == 3:
#     print('В категории HTML 3 товара')
# else:
#     print('Ошибка. В категории HTML товаров:', str(len(product)))
#
# driver.quit()

#### Сортировка товаров ####

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.by import By
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
# shop = driver.find_element(By.ID, 'menu-item-40')
# shop.click()
#
# element = driver.find_element(By.CSS_SELECTOR, '.orderby [selected="selected"]')
# element_selected = element.get_attribute('value')
# assert element_selected == 'menu_order'
#
# element = driver.find_element(By.CLASS_NAME, 'orderby')
# select = Select(element)
# select.select_by_value('price-desc')
#
# element = driver.find_element(By.CSS_SELECTOR, '.orderby [selected="selected"]')
# element_selected = element.get_attribute('value')
# assert element_selected == 'price-desc'
#
# driver.quit()

#### Отображение, скидка товара ####

# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
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
# shop = driver.find_element(By.ID, 'menu-item-40')
# shop.click()
#
# android_qs = driver.find_element(By.CLASS_NAME, 'woocommerce-LoopProduct-link')
# android_qs.click()
#
# price_old = driver.find_element(By.CSS_SELECTOR, '.price>del>span')
# price_old_text = price_old.text
# assert price_old_text == '₹600.00'
#
# price_new = driver.find_element(By.CSS_SELECTOR, '.price>ins>span')
# price_new_text = price_new.text
# assert price_new_text == '₹450.00'
#
# book_img = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'images')))
# book_img.click()
#
# book_close = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'pp_close')))
# book_close.click()
#
# driver.quit()

#### Проверка цены в корзине ####

# import time
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
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
# shop = driver.find_element(By.ID, 'menu-item-40')
# shop.click()
#
# add_to_basket = driver.find_element(By.CSS_SELECTOR, '[data-product_id="182"]')
# add_to_basket.click()
#
# time.sleep(3)
#
# item = driver.find_element(By.CLASS_NAME, 'cartcontents')
# item_text = item.text
# imount = driver.find_element(By.CSS_SELECTOR,'.wpmenucart-contents .amount')
# imount_text = imount.text
# assert item_text == '1 Item'
# assert imount_text == '₹180.00'
#
# cart = driver.find_element(By.ID, 'wpmenucartli')
# cart.click()
#
# subtotal = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.cart-subtotal>td>span')))
# subtotal_text = subtotal.text
# assert subtotal_text == '₹180.00'
#
# total = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.order-total>td>strong')))
# total_text = total.text
# assert total_text == '₹189.00'
#
# driver.quit()

#### Работа в корзине ####

# import time
#
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
# username = driver.find_element(By.ID, 'username')
# username.send_keys('1A2B3C@mail.ru')
#
# password = driver.find_element(By.ID, 'password')
# password.send_keys('GhTyUi9734R')
#
# login = driver.find_element(By.NAME, 'login')
# login.click()
#
# shop = driver.find_element(By.ID, 'menu-item-40')
# shop.click()
#
# driver.execute_script('window.scrollBy(0,300);')
# book_html5 = driver.find_element(By.CSS_SELECTOR, '[data-product_id="182"]')
# book_html5.click()
# time.sleep(3)
# book_js = driver.find_element(By.CSS_SELECTOR, '[data-product_id="180"]')
# book_js.click()
#
# cart = driver.find_element(By.ID, 'wpmenucartli')
# cart.click()
# time.sleep(3)
#
# remove_html5 = driver.find_element(By.CSS_SELECTOR, '[data-product_id="182"]')
# remove_html5.click()
#
# undo = driver.find_element(By.CSS_SELECTOR, '.woocommerce-message>a')
# undo.click()
#
# number = driver.find_element(By.CSS_SELECTOR, 'tbody>tr:nth-child(2) .input-text')
# number.clear()
# number.send_keys('3')
# time.sleep(3)
#
# apply_coupon = driver.find_element(By.NAME, 'apply_coupon')
# apply_coupon.click()
#
# error = driver.find_element(By.CLASS_NAME, 'woocommerce-error')
# error_text = error.text
# assert error_text == 'Please enter a coupon code.'
#
# driver.quit()

#### Покупка товара ####

# import time
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("http://practice.automationtesting.in/")
#
# shop = driver.find_element(By.ID, 'menu-item-40')
# shop.click()
#
# driver.execute_script('window.scrollBy(0,300);')
# book_html5 = driver.find_element(By.CSS_SELECTOR, '[data-product_id="182"]')
# book_html5.click()
#
# cart = driver.find_element(By.CLASS_NAME, 'added_to_cart')
# cart.click()
#
# checkout_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'checkout-button')))
# checkout_btn.click()
#
# first_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'billing_first_name')))
# first_name.send_keys('Sergey')
# last_name = driver.find_element(By.NAME, 'billing_last_name')
# last_name.send_keys('Sudakov')
# email = driver.find_element(By.ID, 'billing_email')
# email.send_keys('qwerty@mail.ru')
# phone = driver.find_element(By.ID, 'billing_phone')
# phone.send_keys('12345678901')
#
# country = driver.find_element(By.ID, 's2id_billing_country')
# country.click()
# search = driver.find_element(By.ID, 's2id_autogen1_search')
# search.send_keys('Togo')
# result_country = driver.find_element(By.ID, 'select2-results-1')
# result_country.click()
#
# address = driver.find_element(By.ID, 'billing_address_1')
# address.send_keys('Weedghhfgg jjhggghjjjjhhh')
# billing_city = driver.find_element(By.ID, 'billing_city')
# billing_city.send_keys('WWWEEErrrr')
# billing_state = driver.find_element(By.ID, 'billing_state')
# billing_state.send_keys('Aaaaaaaaa')
# billing_postcode = driver.find_element(By.ID, 'billing_postcode')
# billing_postcode.send_keys('111111')
#
# driver.execute_script('window.scrollBy(0,600);')
# time.sleep(5)
#
# payment_method_cheque = driver.find_element(By.ID, 'payment_method_cheque')
# payment_method_cheque.click()
#
# place_order = driver.find_element(By.ID, 'place_order')
# place_order.click()
#
# thank_you = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'woocommerce-thankyou-order-received')))
# thank_you_text = thank_you.text
# assert thank_you_text == 'Thank you. Your order has been received.'
#
# method = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.method>strong')))
# method_text = method.text
# assert method_text == 'Check Payments'
#
# driver.quit()