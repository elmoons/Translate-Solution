import tkinter as tk
from tkinter import filedialog, messagebox

from process import process_excel


def open_file():
    input_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    if input_path:
        output_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
        if output_path:
            try:
                process_excel(input_path, output_path, selected_language.get(), direction.get())
                messagebox.showinfo("Успех", "Файл успешно обработан и сохранён.")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")


def closing_program():
    if messagebox.askyesno(title="Выйти", message="Вы действительно хотите выйти из программы?"):
        root.destroy()


def update_language_or_direction():
    # Обновляем текст метки
    label.config(text=f'Перевод слов язык: {selected_language.get()}')

    # Если направление перевода выбрано, показываем кнопку выбора файла
    if direction.get():
        btn_open.pack(pady=20)
    else:
        btn_open.pack_forget()


root = tk.Tk()
root.title("Переводчик")
root.geometry("500x400")

selected_language = tk.StringVar(value="Английский")
direction = tk.StringVar(value="на Русский")  # По умолчанию первый режим

label = tk.Label(root, text=f'Перевод слов язык: {selected_language.get()}')
label.pack(padx=20, pady=10)

instruction_text = (
    "1. Подготовьте файл Excel (.xlsx) с исходными словами.\n"
    "2. Перевод происходит из первой колонки во вторую (из A в B).\n"
    "3. Убедитесь, что выбран верный язык и направление перевода.\n"
    "4. Нажмите 'Выбрать файл' для начала процесса.\n"
    "5. Результат перевода сохраняется в файл, указанный вами."
)

info_label = tk.Label(root, text=instruction_text, fg="black", justify="left")
info_label.pack(padx=20, pady=10)

# Меню выбора языка
menubar = tk.Menu(root)
language_menu = tk.Menu(menubar, tearoff=0)
languages = ["Английский"]


def create_language_menu():
    for language in languages:
        language_menu.add_radiobutton(label=language, variable=selected_language, value=language,
                                      command=update_language_or_direction)


create_language_menu()
menubar.add_cascade(menu=language_menu, label=f'▼ Меню выбора языка')
root.config(menu=menubar)

# Опции направления перевода
direction_frame = tk.Frame(root)
direction_frame.pack(pady=5)
tk.Radiobutton(direction_frame, text="С выбранного языка на Русский", variable=direction, value="на Русский",
               command=update_language_or_direction).pack(side=tk.LEFT)
tk.Radiobutton(direction_frame, text="С Русского на выбранный язык", variable=direction, value="на выбранный",
               command=update_language_or_direction).pack(side=tk.LEFT)

# Кнопка выбора файла (изначально отображается, так как первый режим выбран)
btn_open = tk.Button(root, text="Выбрать файл", command=open_file)
btn_open.pack(pady=20)

root.protocol("WM_DELETE_WINDOW", closing_program)

