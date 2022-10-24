import random
guess_number = -1
number = random.randint(1, 10)
attempt = 0
while guess_number != number:
    if attempt == 5:
        print("Вы не смогли отгадать число раньше, чем с третьего раза. Попробуйте ещё раз")
        break
    guess_number = int(input("Введите число: "))
    if guess_number > number:
        print("Ваше число больше, чем загаданое. Попробуйте ещё раз.")
        attempt += 1
        continue
    elif guess_number < number:
        print("Ваше чило меньше, чем загаданое. Попробуйте ещё раз.")
        attempt += 1
        continue
    elif guess_number == number and attempt == 5:
        print("Поздравляю! Вы отгадали загаданое число.")
    elif guess_number == number and attempt < 5:
        attempt +=1
        print(f"Вы справились с заданием с {attempt} попытки! Поздравляю!")
        break
