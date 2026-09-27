import os
import random
import time

# Настройки поля
WIDTH = 20
HEIGHT = 10

def play_game():
    #Начало игры
    snake = [[5, 5], [5, 4], [5, 3]] #Змейка из 3 точек [Y, X]
    direction = "RIGHT"

    #Спавним еду
    food = [random.randint(1, HEIGHT-2), random.randint(1, WIDTH-2)]
    score = 0

    while True:
        # Очищаем экран консоли (для Windows)
        os.system('cls')
        print(f"---ОЧКИ: {score} --- (Для движения: пишите в консоль W/A/S/D и Enter)")

        # Рисуем карту буквами
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if y == 0 or y == HEIGHT - 1 or x == 0 or x == WIDTH - 1:
                    print("#", end="") # Стены поля
                elif [y, x] == snake[0]:
                    print("X", end="") #Голова змейки
                elif [y, x] in snake[1:]:
                    print("0", end="") #Тело змейки
                elif [y, x] == food:
                    print("*", end="") #Еда
                else:
                    print("", end="") #Пустое место
            print() #Перенос строки

        #Спрашиваем направление(W- вверх, S - вниз, A - влево, D - вправо)
        #Если просто нажать Enter - змейка сделает шаг вперед
        move = input("Куда летим? (W/A/S/D): ").upper()
        if move == "W": direction = "UP"
        elif move == "S": direction = "DOWN"
        elif move == "A": direction = "LEFT"
        elif move == "D": direction = "RIGHT"

        #Считаем новую голову
        head_y, head_x = snake[0]
        if direction == "UP": head_y -= 1
        elif direction == "DOWN": head_y += 1
        elif direction == "LEFT": head_x -= 1
        elif direction == "RIGHT": head_x += 1

        new_head = [head_y, head_x]
        snake.insert(0, new_head)

        #Проверка еды
        if new_head == food:
            score += 1
            food = [random.randint(1, HEIGHT-2), random.randint(1, WIDTH-2)]
        else:
            snake.pop() #Стираем хвост

        #Проверка проигрыша (врезка в стены или себя)
        if head_y == 0 or head_y == HEIGHT-1 or head_x == 0 or head_x == 0 or head_x == WIDTH-1 or new_head in snake[1:]:
            print("ИГРА ОКОНЧЕНА! ВЫ ПРОИГРАЛИ!")
            break
if __name__ == "__main__":
    play_game()

