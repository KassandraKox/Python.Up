from random import randint


def secret_game(start, stop, attempts):
    secret = randint(start, stop)
    for i in range(1, attempts + 1):
        n = int(input(f"Попытка {i}, угадай число: "))
        if n > secret:
            turn = "Меньше"
        elif n < secret:
            turn = "Больше"
        else:
            print("Ты выиграл!")
            return True
        print(turn)
    else:
        print("Попыток больше нет, ты проиграл.")
        return False

if __name__ == "__main__":
    secret_game(1, 100, 1000)