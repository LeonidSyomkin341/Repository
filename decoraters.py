def add_ten_if_integer(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, int):  # Перевіряємо, чи результат є цілим числом
            return result + 10
        return result  # Повертаємо результат без змін, якщо це не ціле число
    return wrapper


@add_ten_if_integer
def some_function():
    return 5

print(some_function())



@add_ten_if_integer
def another_function():
    return 5.5

print(another_function())
