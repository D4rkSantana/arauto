import pandas as pd
import os
import Contact as ct

class DataProcess:
    def checkArgs(self, table:str, archive:str):
        if table.find('.xlsx') == -1:
            print('Table file error')
            return True
        if archive.find('.jpg') == -1:
            print('archive file error')
            return True
        return False

    def createContacts(self):
        contacts = []
        size = self.table_df.len()
        if size < 1:
            return False
        for i in range(size):
            name = self.table_df.loc['Nome', i]
            number = self.table_df.loc['Numero', i]
            if name != '' and number.len() < 11:
                temp = ct.Contact(nome, numero)
                contacts.append(temp)
                self.expected_time += temp.getTime()
                self.qt_contacts++
        return contacts

    def __init__(self, table:str, archive:str):
        if checkArgs(table, archive):
            return False
        self.table_df = pd.read_excel(table)
        self.archive = os.path.abspath(archive)
        self.expected_time = 0
        self.qt_contacts = 0
        self.contacts = self.createContacts()
        return True

    configTable(self)

# gera os dados sobre a planilia
# inicializa os contatos
#def ()

#Leitura da planilha
contacts_df = pd.read_excel('arquivos/contatos.xlsx')
#archive = os.path.abspath("arquivos/urubu-do-pix.jpg")