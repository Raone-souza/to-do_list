# Importa a biblioteca CustomTkinter e a biblioteca Tkinter
from customtkinter import *
import tkinter as tk

# Cria a janela principal do aplicativo com uma cor de fundo especificada
window = CTk(fg_color="#2B2B2B")  # Define o fundo da janela como cinza escuro
window.title("To-Do List")         # Define o título da janela
window.geometry("500x600")          # Define o tamanho da janela para 500x600 pixels

# Cria o título da aplicação
title = CTkLabel(
    window,                        # Define a janela principal como pai do rótulo
    text="to-do list",             # Define o texto do título
    font=CTkFont("Helvetica", 30, "bold"),  # Define a fonte, tamanho e estilo
    text_color="#c4e7d0"           # Define a cor do texto do título
)
title.place(
    relx=0.5,                      # Posição horizontal centralizada
    rely=0.1,                      # Posição vertical a 10% da altura da janela
    anchor=CENTER                  # Centraliza o texto no ponto especificado
)

# Cria um frame para conter a lista de tarefas
frame = CTkFrame(window, width=480, height=400)  # Define largura e altura do frame
frame.place(
    relx=0.5,                      # Posição horizontal centralizada
    rely=0.50,                     # Posição vertical no centro da janela
    anchor=CENTER,                 # Centraliza o frame no ponto especificado
    relwidth=0.96,                 # Ocupa 96% da largura da janela
    relheight=0.67                 # Ocupa 67% da altura da janela
)

# Cria a lista de tarefas (Listbox) dentro do frame
listbox = tk.Listbox(frame, bg="#2B2B2B", fg="#ffffff", highlightthickness=0, font=('Helvetica', 14, 'bold'))
listbox.pack(
    fill="both",                   # Preenche o espaço disponível dentro do frame
    expand=True                    # Permite que a lista expanda para o tamanho do frame
)

# Cria um campo de entrada de texto para adicionar novas tarefas
entry = CTkEntry(window, width=250, height=35)
entry.place(
    relx=0.5,                      # Posição horizontal centralizada
    rely=0.85,                     # Posição vertical a 85% da altura da janela
    anchor=CENTER                  # Centraliza o campo de entrada no ponto especificado
)

# Função para adicionar uma tarefa à lista
def add_task():
    task = entry.get()             # Obtém o texto digitado no campo de entrada
    listbox.insert(tk.END, task)   # Adiciona a nova tarefa ao final da listbox
    entry.delete(0, tk.END)        # Limpa o campo de entrada após adicionar a tarefa

# Função para deletar a tarefa selecionada da lista
def delete_task():
    try:
        task_index = listbox.curselection()[0]  # Obtém o índice da tarefa selecionada
        listbox.delete(task_index)              # Deleta a tarefa com o índice especificado
    except:
        pass                                    # Ignora qualquer erro (ex.: nenhuma tarefa selecionada)

# Cria um frame para os botões "Adicionar" e "Deletar"
button_frame = CTkFrame(window, width=250, height=40, corner_radius=10)
button_frame.place(
    relx=0.5,                      # Posição horizontal centralizada
    rely=0.92,                     # Posição vertical a 92% da altura da janela
    anchor=CENTER                  # Centraliza o frame de botões no ponto especificado
)

# Cria o botão "Adicionar", que chama a função add_task ao ser clicado
add_button = CTkButton(button_frame, text="Adicionar", command=add_task, width=100, height=35, corner_radius=10)
add_button.pack(
    side=tk.LEFT,                  # Posiciona o botão à esquerda dentro do frame
    padx=10,                       # Espaçamento horizontal ao redor do botão
    pady=5                         # Espaçamento vertical ao redor do botão
)

# Cria o botão "Deletar", que chama a função delete_task ao ser clicado
delete_button = CTkButton(button_frame, text="Deletar", command=delete_task, width=100, height=35, corner_radius=10)
delete_button.pack(
    side=tk.LEFT,                  # Posiciona o botão à esquerda do botão "Adicionar"
    padx=10,                       # Espaçamento horizontal ao redor do botão
    pady=5                         # Espaçamento vertical ao redor do botão
)

# Inicia o loop principal da aplicação, que mantém a janela aberta
window.mainloop()
