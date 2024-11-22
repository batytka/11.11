result = []
data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4} # Видалено некоректні ключі

def divider(a, b):
    try:
        if b > 100:
            raise IndexError("Дільник більший за 100")
        if a < b:
            raise ValueError("Ділене менше за дільник")
        if b == 0:
            raise ZeroDivisionError("Ділення на нуль")
        return a / b
    except (ValueError, IndexError, ZeroDivisionError) as e:
        print(f"Виникла помилка: {e}")
        return None # Повертаємо None, якщо виникла помилка


for key in data:
    try:
        if isinstance(key, (int, float)): # Перевіряємо, чи ключ є числом
            res = divider(key, data[key])
            if res is not None: # Додаємо результат тільки якщо помилки не було
                result.append(res)
    except KeyError as e:
        print(f"Виникла помилка: Ключ '{key}' не знайдено в словнику. {e}")
    except TypeError as e:
        print(f"Виникла помилка: Некоректний тип ключа '{key}'. {e}")


print(result)