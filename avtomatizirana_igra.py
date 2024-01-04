from selenium import webdriver
import time
import selenium
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/experiments/cookie/")

a = 0
while a==0:
    cookie = driver.find_element(By.ID, 'cookie')
    money = int(driver.find_element(By.ID, 'money').text)

    cookie.click()
    cursor = driver.find_element(By.ID, 'buyCursor').find_element(By.TAG_NAME, 'b').text
    c = int(cursor.split()[2])
    if c>money:
        cursor1 = driver.find_element(By.ID, 'buyCursor')
        cursor1.click()
    else:
        cookie.click()


    grandma = driver.find_element(By.ID, 'buyGrandma').find_element(By.TAG_NAME, 'b').text
    g = int(grandma.split()[2])
    if money>g:
        grandma1 = driver.find_element(By.ID, 'buyGrandma')
        grandma1.click()
    elif money>c:
        cursor1 = driver.find_element(By.ID, 'buyCursor')
        cursor1.click()
    else:
        cookie.click()



    factory = driver.find_element(By.ID, 'buyFactory').find_element(By.TAG_NAME, 'b').text
    f =  int(factory.split()[2])
    if money>f:
        factory1 = driver.find_element(By.ID, 'buyFactory').
        factory1.click()
    elif money > c:
        cursor1 = driver.find_element(By.ID, 'buyCursor')
        cursor1.click()
    elif money>g:
        grandma1 = driver.find_element(By.ID, 'buyGrandma')
        grandma1.click()
    else:
        cookie.click()

    mine = driver.find_element(By.ID, 'buyMine').find_element(By.TAG_NAME, 'b').text
    m = int(factory.split()[2])
    if money>m:
        mine1 = driver.find_element(By.ID, 'buyMine')
        mine1.click()
    elif money>f:
        factory1 = driver.find_element(By.ID, 'buyFactory').
        factory1.click()
    elif money > c:
        cursor1 = driver.find_element(By.ID, 'buyCursor')
        cursor1.click()
    elif money>g:
        grandma1 = driver.find_element(By.ID, 'buyGrandma')
        grandma1.click()
    else:
        cookie.click()


    shipment = driver.find_element(By.ID, 'buyShipment').find_element(By.TAG_NAME, 'b').text
    s = int(shipment.split()[2])
    if money>s:
        shipment1 = driver.find_element(By.ID, 'buyShipment')
        shipment1.click()
    elif money>m:
        mine1 = driver.find_element(By.ID, 'buyMine')
        mine1.click()
    elif money>f:
        factory1 = driver.find_element(By.ID, 'buyFactory')
        factory1.click()
    elif money > c:
        cursor1 = driver.find_element(By.ID, 'buyCursor')
        cursor1.click()
    elif money>g:
        grandma1 = driver.find_element(By.ID, 'buyGrandma')
        grandma1.click()
    else:
        cookie.click()



    alchemy_lab = driver.find_element(By.ID, 'buyAlchemy lab').find_element(By.TAG_NAME, 'b').text
    a = int(alchemy_lab.split()[2])
    if money>a:
        alchemy_lab1 = driver.find_element(By.ID, 'buyAlchemy lab')
        alchemy_lab1.click()
    elif money>s:
        shipment1 = driver.find_element(By.ID, 'buyShipment')
        shipment1.click()
    elif money>m:
        mine1 = driver.find_element(By.ID, 'buyMine')
        mine1.click()
    elif money>f:
        factory1 = driver.find_element(By.ID, 'buyFactory')
        factory1.click()
    elif money > c:
        cursor1 = driver.find_element(By.ID, 'buyCursor')
        cursor1.click()
    elif money > g:
        grandma1 = driver.find_element(By.ID, 'buyGrandma')
        grandma1.click()
    else:
        cookie.click()







time.sleep(200)
