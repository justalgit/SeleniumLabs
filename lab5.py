from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys
import time

delayTime = 5
driver = webdriver.Chrome()


#Необходимо ввести логин и пароль от тестируемого аккаунта Вконтакте в значения переменных login и password
userLogin = ""
userPassword = ""


driver.get("https://vk.com/")
emailInput = driver.find_element_by_xpath("//*[@id=\"index_email\"]")
passwordInput = driver.find_element_by_xpath("//*[@id=\"index_pass\"]")
loginButton = driver.find_element_by_xpath("//*[@id=\"index_login_button\"]")

emailInput.send_keys(userLogin)
passwordInput.send_keys(userPassword)
loginButton.click()

if ((len(userLogin) != 0) & (len(userPassword) != 0)):
    audioLink = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
        (By.XPATH, '//li[@id="l_aud"]/a')))
    driver.get(audioLink.get_attribute('href'))
    audioList = driver.find_elements_by_xpath('//div[@class="audio_row_content _audio_row_content"]')
    requiredCount = 10
    if(len(audioList) < requiredCount):
        requiredCount = len(audioList)
    for index in range(0, requiredCount):
        audio = audioList[index]
        artist = audio.find_element_by_xpath('./div[@class="audio_row__inner"]/div/div/a[@class="artist_link"]').text
        title = audio.find_element_by_xpath('./div[@class="audio_row__inner"]/div/div/span[@class="audio_row__title_inner _audio_row__title_inner"]').text
        print("Трек №"+ str(index+1) + ":\t" + artist +" - " + title + "\n")
    time.sleep(delayTime)
    driver.get(driver.find_element_by_id("top_logout_link").get_attribute('href'))

else:
    print("Ошибка - заполните переменные login и password корректными для входа значениями в файле lab5.py")

driver.close()