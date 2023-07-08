from classes import Auto as auto
from classes import Contact as cont
from classes import DataProcess as dp
import pandas as pd

print('===== Teste unitario classe Contact')
contact = cont.Contact("Emerson", "5511962676520")
print(contact.getName())
print(contact.getNumber())
print('total time: ', contact.total_time)
print(contact.times, '\n')

print('===== Teste unitario classe Xpath')
xpath = auto.Xpath('arquivos/config')
print(xpath.send_msg)
print(xpath.attach)
print(xpath.input_doc)
print(xpath.input_send, '\n')

print('===== Teste unitario classe DataProcess')
data = dp.DataProcess('arquivos/contatos.xlsx', 'arquivos/urubu-do-pix.jpg')
print(data.table_df)
print('qt contacts: ', data.qt_contacts)
print('expected time: ', data.expected_time)
print(data.archive)
print(data.contacts, '\n')

print('===== Teste unitario classe Auto')
machine = auto.Auto('firefox', 'arquivos/config')
machine.loginWhats()
machine.sendMensage(contact, 'Salve Salve {name} tudo na paz?')
