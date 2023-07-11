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


import tkinter as tk

def printAlgo():
    print("ola mundo")

def create_buttons(window):
    buttons = {
        'bt_table': None,
        'bt_browser': None,
        'bt_login': None,
        'bt_send': None
        }

    buttons['bt_table'] = tk.Button(window, text="Definir", command=printAlgo)
    buttons['bt_browser'] = tk.Button(window, text="Inicializar", command=printAlgo)
    buttons['bt_login'] = tk.Button(window, text="Logar", command=printAlgo)
    buttons['bt_send'] = tk.Button(window, text="Enviar Tudo", command=printAlgo)
    return buttons

window = tk.Tk()

buttons = create_buttons(window)

title = tk.Label(window, text="Titulo")
title.grid(row=0, column=0, padx=10, pady=10)
bt_table = tk.Button(window, text="click aqui", command=printAlgo)
bt_init_browser = tk.Button(window, text="click aqui", command=printAlgo)
bt_login = tk.Button(window, text="click aqui", command=printAlgo)
buttom.grid(row=1, column=0, padx=10, pady=10)

window.mainloop()