from classes import Contact as ct
from classes import Auto as aut
from classes import DataProcess as dp

contact = ct.Contact('Emerson', '5511962676520')
print(contact.getName(), contact.getName(), contact.time, contact.total_time)

data = dp.DataProcess('arquvios/contatos.xlsx', 'arquivos/urubu-do-pix.jpg')
data = dp.DataProcess()
