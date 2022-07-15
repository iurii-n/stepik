from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

 
try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()   
    browser.get(link)
    
    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )
    print('\n','price = ',price)
    
    #Нажать на кнопку "book" 
    browser.find_element(By.ID, "book").click()
    
    #Посчитать математическую функцию от x
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text #получить текст
    y = calc(x)
    print('\n','x = ',y)
    
    #Ввести ответ в текстовое поле.
    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(y)
    
    #проскролить на 100 пикселей вниз
    browser.execute_script("window.scrollBy(0, 100);")
    
    #Нажать на кнопку Submit. 
    browser.find_element(By.ID, "solve").click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    browser.quit()