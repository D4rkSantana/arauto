""" Module containing the Auto class. """

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from urllib.parse import quote

from . import Contact

class Xpath:
    """ 
    Opens and saves xpath settings.

    The class receives a 'config' file, reads it and saves the xpaths in the variables.

    Attributes:
        send_msg (str): xpath of send text message button.
        attach (str): xpath from the attachments button.
        input_doc (str): image input xpath.
        input_send (str): xpath of the image upload button.

    Example of use:
        xpath = Xpath('../arquivos/config')
        print(xpath.send_msg)
    """
    def __init__(self, archive_path:str):
        """
        Args:
            archive_path (str): path to xpath configure file
        """
        self.send_msg = ''
        self.attach = ''
        self.input_doc = ''
        self.input_send = ''
        self.__config(archive_path)

    def __config(self, archive_path:str):
        """ Reads the configuration file and saves it in the variables. """
        file = open(archive_path, 'r')
        line = file.readline()
        self.send_msg = line[line.index('=') + 1:]
        line = file.readline()
        self.attach = line[line.index('=') + 1:]
        line = file.readline()
        self.input_doc = line[line.index('=') + 1:]
        line = file.readline()
        self.input_send = line[line.index('=') + 1:]
        file.close()

# Classe auto recebe qual o browser e o arquivo com os xpaths
# Essa classe opera todas as questões com o broser
class Auto:
    """ 
    This class operates automations with the browser.

    The auto class does operations like initializing the browser and sending messages.

    Attributes:
        browser (str): browser name.

    Methods:
        initXpath(path_config:str): inicializa o Xpath
        initBrowser(browser_name:str): inicializa o browser
        loginWhats(): incializa o whatsapp e aguarda a confirmação do login
        sendMensage(contact:Contact, mensage:str, file:str): envia uma mensagem para o contato
        
    """
    def __init__(self, ):
        self.xpath = None
        self.browser = None

    def initXpath(self, config_file:str):
        self.xpath = Xpath(config_file)

    def initBrowser(self, browser:str):
        if browser == "firefox":
            self.browser = webdriver.Firefox()
        elif browser == "chrome":
            self.browser = webdriver.Chrome()

    def __waitLoad(self):
        """ Wait for whatsapp to load the message screen. """
        if self.browser == None:
            return
        while len(self.browser.find_elements("id", "side")) < 1:
            time.sleep(1)
        time.sleep(4)

    def loginWhats(self):
        """ launches whatsapp to be logged in and waits to load the message screen """
        if self.browser == None:
            return
        self.browser.get('https://web.whatsapp.com/')
        self.__waitLoad()

    def sendMensage(self, contact:Contact, text:str, file:str='none'):
        '''
        Send a message to a contact.
        
        Sends a text to a contact and optionally an image.

        Args:
            contact (Contact): Contact object.
            text (str): The text of the message, meets the following configuration.
                '{name}' will be replaced by contact.getName().
            file(str): Absolute path to the image.

        Example of use:
            auto.sendMensage(contact, 'ola {nome}, tudo bem?', 'C:\\Users\\imagem.jpg').
        '''
        if self.browser == None or self.xpath == None:
            return
        parse_text = text
        parse_text = parse_text.replace("{name}", contact.getName())
        parse_text = quote(parse_text)
        link = f"http://web.whatsapp.com/send?phone={contact.getNumber()}&text={parse_text}"
        self.browser.get(link)
        self.__waitLoad()
        self.browser.find_element(By.XPATH, self.xpath.send_msg).click()
        time.sleep(contact.times['send_msg'])
        if file != 'none':
            self.browser.find_element(By.XPATH, self.xpath.attach).click()
            time.sleep(contact.times['attach'])
            self.browser.find_element(By.XPATH, self.xpath.input_doc).send_keys(file)
            time.sleep(contact.times['input_doc'])
            self.browser.find_element(By.XPATH, self.xpath.input_send).click()
            time.sleep(contact.times['input_send'])
        time.sleep(contact.times['next'])
