import random

from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1> Добро пожаловать на домашнюю страницу!")


# Игра орел решка
def coin(request):
    choice = random.choice(["Орел", "Решка"])
    if choice == "Орел":
        return HttpResponse(f'Выпал: {choice}')
    elif choice == "Решка":
        return HttpResponse(f'Выпала: {choice}')


def random_roll(request):
    result = random.randint(0, 100)
    return HttpResponse(f'Случайное число от 0 до 100:<h1>{result}</h1>')


def random_number(request):
    result = random.randint(0, 6)
    return HttpResponse(f'На кубике выпало:<h1>{result}</h1>')
