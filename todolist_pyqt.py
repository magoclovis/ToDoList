import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QLineEdit, QPushButton, QMessageBox, QInputDialog

# Definição da classe do aplicativo de lista de tarefas
class ToDoListApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicativo Lista de Tarefas")
        self.tasks = []  # Lista para armazenar as tarefas

        layout = QVBoxLayout()  # Criação do layout principal vertical

        # Lista para exibir as tarefas
        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        # Caixa de entrada para adicionar ou editar tarefas
        self.input_entry = QLineEdit()
        layout.addWidget(self.input_entry)

        button_layout = QHBoxLayout()  # Layout horizontal para os botões

        # Botão para adicionar tarefa
        add_button = QPushButton("Adicionar Tarefa")
        add_button.clicked.connect(self.add_task)  # Conecta o botão à função add_task()
        button_layout.addWidget(add_button)

        # Botão para remover tarefa
        delete_button = QPushButton("Remover Tarefa")
        delete_button.clicked.connect(self.delete_task)  # Conecta o botão à função delete_task()
        button_layout.addWidget(delete_button)

        # Botão para editar tarefa
        edit_button = QPushButton("Editar Tarefa")
        edit_button.clicked.connect(self.edit_task)  # Conecta o botão à função edit_task()
        button_layout.addWidget(edit_button)

        # Botão para limpar todas as tarefas
        clear_button = QPushButton("Limpar Tarefas")
        clear_button.clicked.connect(self.clear_tasks)  # Conecta o botão à função clear_tasks()
        button_layout.addWidget(clear_button)

        # Botão para salvar as tarefas em um arquivo
        save_button = QPushButton("Salvar Tarefas")
        save_button.clicked.connect(self.save_tasks)  # Conecta o botão à função save_tasks()
        button_layout.addWidget(save_button)

        layout.addLayout(button_layout)  # Adiciona o layout dos botões ao layout principal
        self.setLayout(layout)  # Define o layout principal para a janela do aplicativo

    # Função para adicionar uma tarefa à lista de tarefas
    def add_task(self):
        task = self.input_entry.text()
        if task:
            self.tasks.append(task)
            self.list_widget.addItem(task)
            self.input_entry.clear()
        else:
            self.show_warning("Atenção", "Por favor, insira uma tarefa.")

    # Função para remover uma tarefa selecionada da lista de tarefas
    def delete_task(self):
        selected_item = self.list_widget.currentItem()
        if selected_item:
            self.list_widget.takeItem(self.list_widget.row(selected_item))
        else:
            self.show_warning("Atenção", "Por favor, selecione uma tarefa para remover.")

    # Função para limpar todas as tarefas da lista
    def clear_tasks(self):
        self.list_widget.clear()
        self.tasks.clear()

    # Função para salvar as tarefas da lista em um arquivo "tarefas.txt"
    def save_tasks(self):
        with open("tarefas.txt", "w") as file:
            file.write("\n".join(self.tasks))

    # Função para editar a tarefa selecionada na lista
    def edit_task(self):
        selected_item = self.list_widget.currentItem()
        if selected_item:
            index = self.list_widget.row(selected_item)
            new_task, ok_pressed = QInputDialog.getText(self, "Editar Tarefa", "Digite a nova tarefa:", QLineEdit.Normal, selected_item.text())
            if ok_pressed and new_task:
                self.tasks[index] = new_task
                selected_item.setText(new_task)
        else:
            self.show_warning("Atenção", "Por favor, selecione uma tarefa para editar.")

    # Função para mostrar uma caixa de mensagem de aviso
    def show_warning(self, title, message):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.exec_()

# Inicialização do aplicativo
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoListApp()
    window.show()
    sys.exit(app.exec_())
