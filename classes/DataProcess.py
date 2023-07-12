""" Module containing the DataProcess class. """

from . import Contact as ct
import pandas as pd
import os

class DataProcess:
    """
    A class that processes program data, Receives the path of a '.xlsx' table and a '.jpg' image.

    This class receives, verifies and processes an exel spreadsheet and image that will be used in the program

    Attributes:
        table_df (DataFrame): DataFrame of the spreadsheet sent.
        file (str): absolute path to the image that will be uploaded.
        expected_time (int): Estimated time to send all messages.
        qt_contacts (int): Number of contacts to send messages.
        contacts (list): List of Contact objects.

    Example of use:
        data = DataProcess()
        data.initTable('table.xlsx')
    """

    def __init__(self):
            self.table_df = None
            self.text = 'Boa tarde, poderia me mandar um pix de R$200? estamos tentando contratar o neymar para jogar no vasco mas esta faltando 200 pratas para pagar o contrato dele'
            self.file = None
            self.expected_time = 0
            self.qt_contacts = 0
            self.contacts = None

    def initTable(self, path:str):
        if path.find('.xlsx') != -1:
            self.table_df = None
            self.file = None
            self.expected_time = 0
            self.qt_contacts = 0
            self.contacts = None
            self.table_df = pd.read_excel(path)
            if len(self.table_df) < 1:
                    self.table_df = None
                    return False
            self.contacts = self.__createContacts()
            return True
        else:
            return False

    def initFile(self, file:str):
        if file.find('.jpg') != -1:
            self.file = os.path.abspath(file)
            return True
        return False

    def __createContacts(self):
        """ Reads the table, saves and returns the contacts in a Contact vector. """
        contacts = []
        if len(self.table_df) < 1:
            return None
        size = len(self.table_df)
        if size < 1:
            return None
        for i in range(size):
            name = self.table_df.loc[i, 'Nome']
            number_phone = str(self.table_df.loc[i, 'Numero'])
            if name != '' and len(number_phone) > 10:
                temp = ct.Contact(name, number_phone)
                contacts.append(temp)
                self.expected_time += temp.total_time
                self.qt_contacts += 1
        return contacts
