import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import os

random_numbers = []
file_paths = ["file1.txt", "file2.txt", "file3.txt"]

def greet_user():
    """Функция для приветствия пользователя."""
    name = simpledialog.askstring("Ввод имени", "Введите ваше имя:")
    if name:
        messagebox.showinfo("Приветствие", f"Привет, {name}!")

def show_arithmetic_operations():
    """Открывает окно для арифметических операций."""
    arithmetic_window = tk.Toplevel(root)
    arithmetic_window.title("Арифметические операции")
    arithmetic_window.geometry("400x300")

    tk.Label(arithmetic_window, text="Введите первое число:").pack(pady=5)
    entry_num1 = tk.Entry(arithmetic_window, width=30)
    entry_num1.pack(pady=5)

    tk.Label(arithmetic_window, text="Введите второе число:").pack(pady=5)
    entry_num2 = tk.Entry(arithmetic_window, width=30)
    entry_num2.pack(pady=5)

    result_label = tk.Label(arithmetic_window, text="Результаты появятся здесь", wraplength=350)
    result_label.pack(pady=20)

    def calculate_operations():
        try:
            num1 = float(entry_num1.get())
            num2 = float(entry_num2.get())

            # Все операции
            summation = num1 + num2
            subtraction = num1 - num2
            multiplication = num1 * num2
            division = "Деление на ноль невозможно" if num2 == 0 else num1 / num2

            # Отображение результата
            result_label.config(
                text=(
                    f"Сумма: {summation}\n"
                    f"Разность: {subtraction}\n"
                    f"Умножение: {multiplication}\n"
                    f"Деление: {division}"
                )
            )
        except ValueError:
            result_label.config(text="Ошибка: Введите корректные числа!")

    # Кнопка расчета
    calc_button = tk.Button(arithmetic_window, text="Рассчитать", command=calculate_operations)
    calc_button.pack(pady=10)

def generate_random_numbers():
    global random_numbers
    random_numbers = [random.randint(1, 100) for _ in range(10)]
    messagebox.showinfo("Случайные числа", f"Сгенерировано: {random_numbers}")

def find_min_max():
    if not random_numbers:
        messagebox.showerror("Ошибка", "Сначала сгенерируйте числа!")
        return
    min_number = min(random_numbers)
    max_number = max(random_numbers)
    messagebox.showinfo("Результаты", f"Минимальное: {min_number}\nМаксимальное: {max_number}")

def create_and_save_files():

    try:
        data = []
        for _ in range(3):
            unique_numbers = set()
            while len(unique_numbers) < 10:
                unique_numbers.add(random.randint(1, 100))
            data.append(list(unique_numbers))

        for i, path in enumerate(file_paths):
            with open(path, "w") as f:
                f.write("\n".join(map(str, data[i])))

        messagebox.showinfo("Файлы созданы", f"Файлы сохранены:\n{', '.join(file_paths)}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось создать файлы: {e}")

def open_files():
    try:
        for path in file_paths:
            if os.path.exists(path):
                os.startfile(path)
            else:
                messagebox.showwarning("Файл не найден", f"Файл {path} не найден!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось открыть файлы: {e}")

root = tk.Tk()
root.title("Многофункциональное приложение")
root.geometry("400x400")


greet_button = tk.Button(root, text="Приветствие", command=greet_user, width=25, height=2)
greet_button.pack(pady=10)

calc_button = tk.Button(root, text="Арифметические операции", command=show_arithmetic_operations, width=25, height=2)
calc_button.pack(pady=10)

generate_button = tk.Button(root, text="Сгенерировать 10 чисел", command=generate_random_numbers, width=25, height=2)
generate_button.pack(pady=10)

min_max_button = tk.Button(root, text="Найти мин. и макс.", command=find_min_max, width=25, height=2)
min_max_button.pack(pady=10)


create_files_button = tk.Button(root, text="Создать файлы с числами", command=create_and_save_files, width=25, height=2)
create_files_button.pack(pady=10)

open_files_button = tk.Button(root, text="Открыть файлы", command=open_files, width=25, height=2)
open_files_button.pack(pady=10)

root.mainloop()