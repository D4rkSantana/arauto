from classes import Contact as ct
from classes import Auto as aut
from classes import DataProcess as dp
import tkinter as tk

window = tk.Tk()

def send_all():
    time_consumed = 0
    for i in range(data.qt_contacts):
        machine.sendMensage(data.contacts[i], text, data.archive)
        time_consumed += data.contacts[i].total_time
        print('tempo restante: ', data.expected_time - time_consumed)

data = dp.DataProcess('arquivos/contatos.xlsx', 'arquivos/urubu-do-pix.jpg')
machine = aut.Auto('firefox', 'arquivos/config')
text = 'ola {name}, tudo bem?'
machine.loginWhats()
#send_all()

window.mainloop()
