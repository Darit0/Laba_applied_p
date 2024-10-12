import tkinter as tk
from random import randint
import time


class NumberGuessingGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Загадка числа")

        # Загадываем число
        self.number_to_guess = randint(1, 100)

        # Создаем фрейм для выбора уровня сложности
        self.difficulty_frame = tk.Frame(self.root)
        self.difficulty_frame.pack(pady=20)

        self.difficulty_var = tk.StringVar(self.root)
        self.difficulty_var.set("Средний")  # по умолчанию

        self.difficulty_option = tk.OptionMenu(self.difficulty_frame, self.difficulty_var,
                                               "Легкий", "Средний", "Сложный")
        self.difficulty_option.pack(side=tk.LEFT, padx=10)

        self.start_button = tk.Button(self.difficulty_frame, text="Начать игру", command=self.start_game)
        self.start_button.pack(side=tk.LEFT, padx=10)

        # Создаем метку для отображения результатов
        self.result_label = tk.Label(self.root, text="", font=('Helvetica', 12))
        self.result_label.pack()

    def start_game(self):
        difficulty = self.difficulty_var.get()
        if difficulty == "Легкий":
            time_limit = 60
        elif difficulty == "Средний":
            time_limit = 30
        else:
            time_limit = 15

        # Инициализируем переменные для отслеживания времени
        self.time_left = time_limit
        self.start_time = time.time()

        self.difficulty_frame.pack_forget()#закрываем окно

        # Оформление самой игры
        self.label = tk.Label(self.root, text=f"Угадайте число от 1 до 100 за {time_limit} секунд:",
                              font=('Helvetica', 16))
        self.label.pack(pady=20)

        self.entry = tk.Entry(self.root, width=30)
        self.entry.pack(pady=10)

        self.button = tk.Button(self.root, text="Угадать", command=self.check_number)
        self.button.pack(pady=10)

        self.time_label = tk.Label(self.root, text=f"Время: {self.time_left}", font=('Helvetica', 12))
        self.time_label.pack(side=tk.BOTTOM)

    def check_number(self): # Отражает саму игру
        try:
            guessed_number = int(self.entry.get())

            if guessed_number < self.number_to_guess:
                self.result_label.config(text=f"Число больше {guessed_number}")
            elif guessed_number > self.number_to_guess:
                self.result_label.config(text=f"Число меньше {guessed_number}")
            else:
                end_time = time.time()
                elapsed_time = end_time - self.start_time

                if elapsed_time <= self.time_left:
                    self.result_label.config(
                        text=f"Вы угадали! Число было {self.number_to_guess}. Вы справились за {elapsed_time:.2f} секунд.")
                else:
                    self.result_label.config(
                        text=f"Вы проиграли! Правильный ответ: {self.number_to_guess}. Вы превысили время в {elapsed_time - self.time_left:.2f} секунд.")

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
        self.difficulty_frame.pack()
        self.label.pack_forget()
        self.entry.delete(0, tk.END)
        self.button.config(state=tk.NORMAL)
        self.button.config(text="Угадать")
        self.time_left = 0
        self.start_time = time.time()
        self.time_label.pack_forget()

    def update_timer(self): # Функция замеров времени
        current_time = time.time() - self.start_time
        remaining_time = max(0, self.time_left - current_time)

        minutes, secs = divmod(remaining_time, 60)
        self.time_label.config(text=f"Время: {int(minutes):02d}:{secs:05.2f}")

        if remaining_time > 0:
            self.root.after(100, self.update_timer)
        else:
            self.time_label.config(text="Время вышло!")
            self.result_label.config(text=f"Вы проиграли! Правильный ответ: {self.number_to_guess}")

    def run(self):
        self.root.after(100, self.update_timer)
        self.root.mainloop()


if __name__ == "__main__":
    game = NumberGuessingGame()
    game.run()

