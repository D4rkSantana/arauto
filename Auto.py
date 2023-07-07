from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from urllib.parse import quote
import Contact

class Xpath:
    def __init__(self):
        self.send_msg = '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]'
        self.attach = '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div'
        self.input_doc = '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[1]/button/input'
        self.input_send = '/html/body/div[1]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div'

class Auto:
    def __init__(self, browser:str):
        self.xpath = Xpath()
        if browser == "firefox":
            self.browser = webdriver.Firefox()
        elif browser == "chrome":
            self.browser = webdriver.Chrome()

    def waitLoad(self):
        while len(self.browser.find_elements("id", "side")) < 1:
            time.sleep(1)
        time.sleep(4)

    def loginWhats(self):
        self.browser.get('https://web.whatsapp.com/')
        self.waitLoad()

    def sendMensage(self, contact, file, text):
        parse_text = text;
        parse_text = parse_text.replace("{name}", contact.getName())
        parse_text = quote(parse_text)
        print(parse_text)
        link = f"http://web.whatsapp.com/send?phone={contact.getNumber()}&text={parse_text}"
        self.browser.get(link)
        self.waitLoad()
        self.browser.find_element(By.XPATH, self.xpath.send_msg).click()
        time.sleep(1)
        if file != 'none':
            self.browser.find_element(By.XPATH, self.xpath.attach).click()
            time.sleep(1)
            self.browser.find_element(By.XPATH, self.xpath.input_doc).send_keys(arquivo)
            time.sleep(5)
            self.browser.find_element(By.XPATH, self.xpath.input_send).click()
            time.sleep(2)
        time.sleep(10)
