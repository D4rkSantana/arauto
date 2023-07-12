import tkinter as tk
from . import Auto as auto
from . import DataProcess as dp

class Interface:
    def __init__(self, auto, data):
        self.level = 0
        self.window = tk.Tk()
        self.browser = None
        self.browser_arg = tk.StringVar()
        self.path_table = None
        self.auto = auto
        self.data = data

        self.buttons = self.__crateButtons()
        self.labels_status = self.__createStatus()
        self.entry_table = tk.Entry(self.window)
        self.radio_browser = self.__createRadios()
        self.labels_infos = self.__createInfos()
    
    def __crateButtons(self):
        buttons = {
        'bt_table': None,
        'bt_browser': None,
        'bt_wpp': None,
        'bt_send': None
        }
        buttons['bt_table'] = tk.Button(self.window, text="Definir Tabela", command=self.__clickTable)
        buttons['bt_browser'] = tk.Button(self.window, text="Inicializar Navegador", command=self.__clickBrowser)
        buttons['bt_login'] = tk.Button(self.window, text="Iniciar Whatsapp", command=self.__clickLoginWpp)
        buttons['bt_send'] = tk.Button(self.window, text="Enviar Mensagens", command=self.__clickSend)
        return buttons
    
    def __createStatus(self):
        labels = {
        'status_table': None,
        'status_browser': None,
        'status_wpp': None,
        'status_send': None
        }
        labels['status_table'] = tk.Label(self.window, text="Status: Não Definido")
        labels['status_browser'] = tk.Label(self.window, text="Status: Navegado não Iniciado")
        labels['status_wpp'] = tk.Label(self.window, text="Status: Não Logado")
        labels['status_send'] = tk.Label(self.window, text="Status: Indefinido")
        return labels

    def __createRadios(self):
        radios = {
            'firefox': None,
            'chrome': None
        }
        radios['firefox'] = tk.Radiobutton(self.window, text='Firefox', variable=self.browser_arg, value='firefox', command=self.__getBrowser)
        radios['chrome'] = tk.Radiobutton(self.window, text='Chrome', variable=self.browser_arg, value='chrome', command=self.__getBrowser)
        return radios

    def __getBrowser(self):
        self.browser = self.browser_arg.get()
        temp_str = 'Navegador Definido: ' + self.browser
        self.labels_infos['browser_set'].config(text=temp_str)

    def __createInfos(self):
        labels = {
            'qt_contacts_table': None,
            'estimated_time_table': None,
            'path_table': None,
            'browser_set': None,
            'total_time_send': None,
            'time_left_send': None,
            'remaining_contacts_send': None,
            'contacts_send': None
        }
        labels['qt_contacts_tb'] = tk.Label(self.window, text="Quantidade Contatos: ---")
        labels['estimated_time_tb'] = tk.Label(self.window, text="Tempo Estimado: ------")
        labels['path_table'] = tk.Label(self.window, text="-------------")
        labels['browser_set'] = tk.Label(self.window, text="Navegador Definido: ------")
        labels['total_time_send'] = tk.Label(self.window, text="Tempo Total: -----")
        labels['time_left_send'] = tk.Label(self.window, text="Tempo Restante: -----")
        labels['remaining_contacts_send'] = tk.Label(self.window, text="Contatos Enviados: ---")
        labels['contacts_send'] = tk.Label(self.window, text="Contatos Restantes: ---")
        return labels

    def __clickTable(self):
        self.path_table = self.entry_table.get()
        if self.path_table != '':
            if self.data.initTable(self.path_table) == False:
                self.labels_infos['path_table'].config(text='Tabela invalida')
                self.level = 0
            self.labels_status['status_table'].config(text="Status: Definido")
            self.labels_infos['path_table'].config(text=self.path_table)
            temp_str = "Quantidade Contatos: " + str(self.data.qt_contacts)
            self.labels_infos['qt_contacts_tb'].config(text=temp_str)
            temp_str = "Tempo Estimado: " + str(self.data.expected_time) + 'seg'
            self.labels_infos['estimated_time_tb'].config(text=temp_str)
            self.level = 1

    def __clickBrowser(self):
        if self.level < 1:
            print("Nav Negado")
        if self.browser != None:
            self.auto.initXpath('arquivos/config_' + self.browser)
            self.auto.initBrowser(self.browser)
            temp_str = 'Status: Inicializado'
            self.labels_status['status_browser'].config(text=temp_str)
            self.level = 2

    def __clickLoginWpp(self):
        if self.level < 2:
            print("Login Negado")
            return
        self.auto.loginWhats()
        self.labels_status['status_wpp'].config(text="Status: Logado")
        self.level = 3

    def __clickSend(self):
        if self.level < 3:
            print("Send Negado")
        if self.data.contacts == None or self.data.text == None:
            return
        
        cont_send = 0
        cont_rest = self.data.qt_contacts
        time = self.data.expected_time
        temp_str = "Tempo Total: " + str(time) + 'seg'

        self.labels_status['status_send'].config(text="Status: Enviando")
        self.labels_infos['total_time_send'].config(text=temp_str)
        temp_str = 'Tempo Restante: ' + str(time) + 'seg'
        self.labels_infos['time_left_send'].config(text=temp_str)
        self.labels_infos['contacts_send'].config(text="Contatos Enviados: " + str(cont_send))
        self.labels_infos['remaining_contacts_send'].config(text="Contatos Restantes: " + str(cont_rest))

        for cont in self.data.contacts:
            self.auto.sendMensage(cont, self.data.text, self.data.file)

            time -= cont.total_time
            temp_str = 'Tempo Restante: ' + str(time) + 'seg'
            self.labels_infos['time_left_send'].config(text=temp_str)

            cont_send += 1
            cont_rest -= 1
            self.labels_infos['contacts_send'].config(text="Contatos Enviados: " + str(cont_rest))
            self.labels_infos['remaining_contacts_send'].config(text="Contatos Restantes: " + str(cont_send))

        self.labels_status['status_send'].config(text="Status: Finalizado")

    def buildWidgets(self):
        #Area Tabela
        self.buttons['bt_table'].grid(row=1, column=0, sticky="NSEW", padx=10, pady=10)
        self.labels_status['status_table'].grid(row=2, column=0, sticky="NSEW", padx=10, pady=10)
        self.entry_table.grid(row=1, column=1, sticky="NSEW", columnspan=2, padx=10, pady=10)
        self.labels_infos['qt_contacts_tb'].grid(row=2, column=1, sticky="NSEW", columnspan=2, padx=10, pady=10)
        self.labels_infos['path_table'].grid(row=3, column=0, sticky="NSEW", padx=10, pady=10)
        self.labels_infos['estimated_time_tb'].grid(row=3, column=1, sticky="NSEW", columnspan=2, padx=10, pady=10)

        #Area Navegador
        self.buttons['bt_browser'].grid(row=5, column=0, sticky="NSEW", padx=10, pady=10)
        self.radio_browser['firefox'].grid(row=5, column=2, sticky="NSEW", padx=10, pady=10)
        self.radio_browser['chrome'].grid(row=5, column=1, sticky="NSEW", padx=10, pady=10)
        self.labels_status['status_browser'].grid(row=6, column=0, sticky="NSEW", padx=10, pady=10)
        self.labels_infos['browser_set'].grid(row=6, column=1, sticky="NSEW", columnspan=2, padx=10, pady=10)

        #Area Login
        self.buttons['bt_login'].grid(row=8, column=0, sticky="NSEW", padx=10, pady=10)
        self.labels_status['status_wpp'].grid(row=8, column=1, sticky="NSEW", columnspan=2, padx=10, pady=10)
        
        #Area Envios
        self.buttons['bt_send'].grid(row=10, column=0, sticky="NSEW", padx=10, pady=10)
        self.labels_status['status_send'].grid(row=10, column=1, sticky="NSEW", columnspan=2, padx=10, pady=10)

        self.labels_infos['total_time_send'].grid(row=11, column=0, sticky="NSEW", padx=10, pady=10)
        self.labels_infos['time_left_send'].grid(row=12, column=0, sticky="NSEW", padx=10, pady=10)
        self.labels_infos['remaining_contacts_send'].grid(row=11, column=1, sticky="NSEW", columnspan=2, padx=10, pady=10)
        self.labels_infos['contacts_send'].grid(row=12, column=1, sticky="NSEW", columnspan=2, padx=10, pady=10)