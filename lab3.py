import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

googleTranslateUrl = "https://translate.google.com"
delayTime = 3

class TestTranslator(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def getSourceField(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.ID, "source")))

    def getResultField(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "translation")))

    def getTargetLanguageSelector(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "tlid-open-target-language-list")))

    def getSourceLanguageSelector(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "tlid-open-source-language-list")))

    def test_eng_to_rus(self):
        self.driver.get(googleTranslateUrl)
        sourceField = self.getSourceField()
        sourceField.send_keys("cat")
        resultField = self.getResultField()
        time.sleep(delayTime)
        assert "Кот" == resultField.text
        self.driver.close()

    def test_rus_to_eng(self):
        self.driver.get(googleTranslateUrl)
        sourceField = self.getSourceField()
        sourceField.send_keys("кот")
        targetLangSelector = self.getTargetLanguageSelector()
        targetLangSelector.click()
        engWrapper = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.CLASS_NAME, "language_list_item_wrapper-en")))
        self.driver.execute_script("arguments[0].click();", engWrapper)
        switchButton = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div")))
        switchButton.click()
        time.sleep(delayTime)
        resultField = self.getResultField()
        assert "cat" == resultField.text
        self.driver.close()

    def test_rus_to_rus(self):
        self.driver.get(googleTranslateUrl)
        sourceField = self.getSourceField()
        sourceField.send_keys("кот")
        resultField = self.getResultField()
        time.sleep(delayTime)
        assert "кот" == resultField.text
        self.driver.close()

    def test_input_digits(self):
        self.driver.get(googleTranslateUrl)
        sourceField = self.getSourceField()
        sourceField.send_keys("123")
        resultField = self.getResultField()
        time.sleep(delayTime)
        assert "123" == resultField.text
        self.driver.close()

    def test_rus_to_ger(self):
        self.driver.get(googleTranslateUrl)
        sourceField = self.getSourceField()
        sourceField.send_keys("кот")
        targetLangSelector = self.getTargetLanguageSelector()
        targetLangSelector.click()
        engWrapper = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.CLASS_NAME, "language_list_item_wrapper-de")))
        self.driver.execute_script("arguments[0].click();", engWrapper)
        switchButton = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div")))
        switchButton.click()
        time.sleep(delayTime)
        resultField = self.getResultField()
        assert "Der Kater" == resultField.text
        self.driver.close()

    def test_ger_to_rus(self):
        self.driver.get(googleTranslateUrl)
        sourceField = self.getSourceField()
        sourceField.send_keys("der kater")
        resultField = self.getResultField()
        time.sleep(delayTime)
        assert "Кот" == resultField.text
        self.driver.close()

    def test_rus_abb_to_eng(self):
        self.driver.get(googleTranslateUrl)
        sourceField = self.getSourceField()
        sourceField.send_keys("СССР")
        targetLangSelector = self.getTargetLanguageSelector()
        targetLangSelector.click()
        engWrapper = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.CLASS_NAME, "language_list_item_wrapper-en")))
        self.driver.execute_script("arguments[0].click();", engWrapper)
        switchButton = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div")))
        switchButton.click()
        time.sleep(delayTime)
        resultField = self.getResultField()
        assert "USSR" == resultField.text
        self.driver.close()
    
    def test_eng_abb_to_rus(self):
        self.driver.get(googleTranslateUrl)
        sourceField = self.getSourceField()
        sourceField.send_keys("USSR")
        resultField = self.getResultField()
        time.sleep(delayTime)
        assert "СССР" == resultField.text
        self.driver.close()

if __name__ == '__main__':
    unittest.main()