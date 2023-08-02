import tkinter as tk
from tkinter import messagebox

# Função para adicionar uma tarefa à lista de tarefas
def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Atenção", "Por favor, insira uma tarefa.")

# Função para remover uma tarefa selecionada da lista de tarefas
def delete_task():
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
    except IndexError:
        messagebox.showwarning("Atenção", "Por favor, selecione uma tarefa para remover.")

# Função para limpar todas as tarefas da lista
def clear_tasks():
    listbox_tasks.delete(0, tk.END)

# Função para salvar as tarefas da lista em um arquivo "tarefas.txt"
def save_tasks():
    with open("tarefas.txt", "w") as file:
        tasks = listbox_tasks.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")

# Função para editar a tarefa selecionada na lista
def edit_task():
    try:
        index = listbox_tasks.curselection()[0]
        old_task = listbox_tasks.get(index)
        new_task = entry_task.get()
        if new_task:
            listbox_tasks.delete(index)
            listbox_tasks.insert(index, new_task)
            entry_task.delete(0, tk.END)
            messagebox.showinfo("Sucesso", f"Tarefa '{old_task}' foi editada para '{new_task}'.")
        else:
            messagebox.showwarning("Atenção", "Por favor, insira um valor para editar a tarefa.")
    except IndexError:
        messagebox.showwarning("Atenção", "Por favor, selecione uma tarefa para editar.")

# Criação da janela principal
root = tk.Tk()
root.title("Aplicativo Lista de Tarefas")

# Criação do quadro (frame) para conter os widgets
frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10)

# Criação da lista de tarefas com barra de rolagem
# bg = cor de fundo da lista
listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50, bg="lightyellow")
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

# Caixa de entrada para adicionar ou editar tarefas
entry_task = tk.Entry(root, width=50)
entry_task.pack(pady=10)

# Botões para executar as ações
button_add_task = tk.Button(root, text="Adicionar Tarefa", command=add_task)
button_add_task.pack(side=tk.LEFT, padx=5)

button_delete_task = tk.Button(root, text="Remover Tarefa", command=delete_task)
button_delete_task.pack(side=tk.LEFT, padx=5)

button_edit_task = tk.Button(root, text="Editar Tarefa", command=edit_task)
button_edit_task.pack(side=tk.LEFT, padx=5)

button_clear_tasks = tk.Button(root, text="Limpar Tarefas", command=clear_tasks)
button_clear_tasks.pack(side=tk.LEFT, padx=5)

button_save_tasks = tk.Button(root, text="Salvar Tarefas", command=save_tasks)
button_save_tasks.pack(side=tk.LEFT, padx=5)

# Inicia a interface gráfica
root.mainloop()
