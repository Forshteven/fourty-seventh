import threading
import time

# Количество врагов у всех потоков
ENEMIES_COUNT = 100


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days_passed = 0

    def run(self):
        global ENEMIES_COUNT
        print(f"{self.name}, на нас напали!")

        while ENEMIES_COUNT > 0:
            # Сражение длится 1 день (1 секунда)
            time.sleep(1)

            # Уменьшаем количество врагов на силу рыцаря
            if ENEMIES_COUNT >= self.power:
                ENEMIES_COUNT -= self.power
            else:
                ENEMIES_COUNT = 0

            # Обновляем счетчик дней
            self.days_passed += 1

            # Сообщаем о ходе битвы
            print(f"{self.name} сражается {self.days_passed}... Осталось {ENEMIES_COUNT} воинов.")

        # Победная фраза после завершения битвы
        days_word = 'день' if self.days_passed == 1 else (
            'дней' if self.days_passed % 10 != 1 or self.days_passed > 20 else 'дня')
        print(f"{self.name} одержал победу спустя {self.days_passed} {days_word}!")


if __name__ == "__main__":
    # Создаем двух рыцарей
    knight_1 = Knight('Sir Lancelot', 10)
    knight_2 = Knight("Sir Galahad", 20)

    # Запускаем потоки
    knight_1.start()
    knight_2.start()

    # Ожидаем окончания работы обоих потоков
    knight_1.join()
    knight_2.join()

    # Сообщение об окончании битв
    print("Битвы окончены!")


# Создание класса

# Запуск потоков и остановка текущего
# Вывод строки об окончании сражения