import Contact as ct
import Auto as aut

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import pandas as pd
import time
import os

contact_df = pd.read_excel('arquivos/contatos.xlsx')
archive = os.path.abspath("arquivos/urubu-do-pix.jpg")



for index in contact_df.index:
    nome = contact_df.loc[index, 'Nome']
    numero = contact_df.loc[index, 'Numero']
    send_mensage(nome, numero, arquivo)