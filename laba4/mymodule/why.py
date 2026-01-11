def string(a):
    if isinstance(a, str):
        return "цифр нет"
    elif isinstance(a, int):
        return "цифры"
    else:
        return "пусто"
