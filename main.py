import tkinter as tk
from random import randint


class NumberGuessingGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Загадка числа")

        # Загадываем число
        self.number_to_guess = randint(1, 100)

        # Создаем и размещаем элементы интерфейса
        self.label = tk.Label(self.root, text="Угадайте число от 1 до 100:", font=('Helvetica', 16))
        self.label.pack(pady=20)

        self.entry = tk.Entry(self.root, width=30)
        self.entry.pack(pady=10)

        self.button = tk.Button(self.root, text="Угадать", command=self.check_number)
        self.button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="", font=('Helvetica', 12))
        self.result_label.pack()

    def check_number(self):
        try:
            guessed_number = int(self.entry.get())

            if guessed_number < self.number_to_guess:
                self.result_label.config(text=f"Число больше {guessed_number}")
            elif guessed_number > self.number_to_guess:
                self.result_label.config(text=f"Число меньше {guessed_number}")
            else:
                self.result_label.config(text=f"Вы угадали! Число было {self.number_to_guess}")

                # Очищаем поле ввода и кнопку
                self.entry.delete(0, tk.END)
                self.button.config(state=tk.DISABLED)

                # Добавляем кнопку для новой игры
                new_game_button = tk.Button(self.root, text="Новая игра", command=self.start_new_game)
                new_game_button.pack(pady=10)
        except ValueError:
            self.result_label.config(text="Пожалуйста, введите целое число")

    def start_new_game(self):
        self.number_to_guess = randint(1, 100)
        self.result_label.config(text="")
        self.entry.delete(0, tk.END)
        self.button.config(state=tk.NORMAL)
        self.button.config(text="Угадать")
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button) and widget != self.button:
                widget.destroy()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    game = NumberGuessingGame()
    game.run()