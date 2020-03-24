from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

delayTime = 2
driver = webdriver.Chrome()

sourceFile = open("sourceFile.txt", "r").read().splitlines()
imageSites = []
myImageUrl = sourceFile[0]

for i in range(1, len(sourceFile), 1):
    driver.get(sourceFile[i])

    time.sleep(delayTime)

    images = driver.find_elements_by_tag_name("a")
    for image in images:
        if (myImageUrl in image.get_attribute("style")):
            imageSites.append(driver.title + ": " + sourceFile[i] + "\n")

if (len(imageSites) != 0):
    open("imageSites.txt", 'w+', encoding="UTF-8-sig").writelines(imageSites)
    print("Заголовки и URL-ссылки сайтов, содержащих указанную в sourceFile.txt картинку, сохранены в файл imageSites.txt")
else:
    print("Не найдено ни одного сайта, содержащего указанную в sourceFile.txt картинку!")
driver.close()