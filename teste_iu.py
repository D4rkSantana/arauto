import tkinter as tk

def printAlgo():
    print("ola mundo")

janela = tk.Tk()

title = tk.Label(janela, text="Titulo")
buttom = tk.Button(janela, text="click aqui", command=printAlgo)
title.pack()
buttom.pack()

janela.mainloop()