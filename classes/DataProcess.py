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
        archive (str): absolute path to the image that will be uploaded.
        expected_time (int): Estimated time to send all messages.
        qt_contacts (int): Number of contacts to send messages.
        contacts (list): List of Contact objects.

    Example of use:
        data = DataProcess('files/table.xlsx', 'files/image.jpg')
        print(data.table_df)
        print(data.archive)
        print(data.expected_time)
        for contact in data.contacts:
            print(contact.name)
    """

    def __init__(self, table:str, archive:str):
        """ 
        Initialize DataProcess with table and image

        Args:
            table (str): path to table '.xslx'
            archive (str): path to a '.jpg' image
        """
        if self.__checkArgs(table, archive):
            self.table_df = pd.read_excel(table)
            self.archive = os.path.abspath(archive)
            self.expected_time = 0
            self.qt_contacts = 0
            self.contacts = self.__createContacts()
        else:
            self.table_df = 'none'
            self.archive = 'none'
            self.expected_time = 0
            self.qt_contacts = 0
            self.contacts = 0


    def __checkArgs(self, table:str, archive:str):
        """ Check the attached table and image file extension, in case of error returns False. """
        if table.find('.xlsx') == -1:
            print('Table file error')
            return False
        if archive.find('.jpg') == -1:
            print('archive file error')
            return False
        return True

    def __createContacts(self):
        """ Reads the table, saves and returns the contacts in a Contact vector. """
        contacts = []
        size = len(self.table_df)
        if size < 1:
            return False
        for i in range(size):
            name = self.table_df.loc[i, 'Nome']
            number_phone = str(self.table_df.loc[i, 'Numero'])
            if name != '' and len(number_phone) < 11:
                temp = ct.Contact(name, number_phone)
                contacts.append(temp)
                self.expected_time += temp.getTime()
                self.qt_contacts += 1
        return contacts
