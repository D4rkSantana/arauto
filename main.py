from classes import Auto as aut
from classes import DataProcess as dp
from classes import Interface as inter


auto = aut.Auto()
data = dp.DataProcess()
interface = inter.Interface(auto, data)
interface.buildWidgets()
interface.window.mainloop()

#arquivos/contatos.xlsx