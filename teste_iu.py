import tkinter as tk

janela = tk.Tk()

escolha = tk.StringVar()

def selecionar_opcao():
    opcao_selecionada = escolha.get()
    print("Opção selecionada:", opcao_selecionada)

# Cria os botões de opção
opcao1 = tk.Radiobutton(janela, text="Firefox", variable=escolha, value="firefox", command=selecionar_opcao)
opcao2 = tk.Radiobutton(janela, text="Chrome", variable=escolha, value="chrome", command=selecionar_opcao)

# Posiciona os botões de opção na janela
opcao1.pack()
opcao2.pack()


janela.mainloop()
