from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import random

data: dict[str, str] = {
}
form_url: str

option = webdriver.ChromeOptions()
option.add_argument('-incognito')
browser = webdriver.Chrome(service=Service('chromedriver.exe'), options=option)
while True:
    browser.get(form_url)

    for question_element in browser.find_elements(by=By.XPATH, value=f"//div[@role='listitem']"):
        question_text: str = question_element.find_element(by=By.XPATH, value=f"./div/div/div/div/div").text
        if question_text in data:
            question_element.find_element(by=By.XPATH, value=f"./div/div[2]/div/div/span/div/div[label/div/div[2]/div/span/text()='{data[question_text]}']").click()
        else:
            options = question_element.find_elements(by=By.XPATH, value=f"./div/div/div[2]/div/div/span/div/div")
            print(options)
            random.choice(options).click()

    browser.find_element(by=By.XPATH, value=f"//div[@role='button' and span/span/text()='Submit']").click()
