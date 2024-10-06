import tkinter as tk
from tkinter import messagebox

# Función para agregar una nueva tarea
def add_task(event=None):
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No se puede añadir una tarea vacía.")

# Función para marcar una tarea como completada
def complete_task(event=None):
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_task_index)
        listbox_tasks.delete(selected_task_index)
        listbox_tasks.insert(tk.END, task + " (Completada)")
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea.")

# Función para eliminar una tarea
def delete_task(event=None):
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea.")

# Función para cerrar la aplicación
def close_app(event=None):
    root.quit()

# Crear ventana principal
root = tk.Tk()
root.title("Gestión de Tareas")

# Crear campo de entrada para nuevas tareas
entry_task = tk.Entry(root, width=30)
entry_task.grid(row=0, column=0, padx=10, pady=10)

# Botones
button_add_task = tk.Button(root, text="Añadir Tarea", command=add_task)
button_add_task.grid(row=0, column=1, padx=10)

button_complete_task = tk.Button(root, text="Completar Tarea", command=complete_task)
button_complete_task.grid(row=1, column=0, pady=10)

button_delete_task = tk.Button(root, text="Eliminar Tarea", command=delete_task)
button_delete_task.grid(row=1, column=1, pady=10)

# Lista para mostrar las tareas
listbox_tasks = tk.Listbox(root, width=50, height=10)
listbox_tasks.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Atajos de teclado
root.bind("<Return>", add_task)  # Añadir tarea con "Enter"
root.bind("<c>", complete_task)  # Marcar tarea como completada con "C"
root.bind("<Delete>", delete_task)  # Eliminar tarea con "Delete"
root.bind("<Escape>", close_app)  # Cerrar aplicación con "Escape"

# Ejecutar la ventana principal
root.mainloop()