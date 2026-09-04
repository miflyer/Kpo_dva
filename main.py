from serialization import Serialization
import hashlib
import os
import pickle
from functools import wraps
import time

def timer(func):
    @wraps(func)  # Сохраняет имя и документацию исходной функции
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Функция {func.__name__} выполнилась за {end_time - start_time:.4f} сек.")
        return result
    return wrapper

def get_cache_key(func_name, args, kwargs):
    # Создаем строку из аргументов и хешируем её
    key_str = f"{func_name}{args}{tuple(sorted(kwargs.items()))}"
    return hashlib.md5(key_str.encode()).hexdigest()

# Простой декоратор для кэширования
def cache_func(cache_dir=".cache"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Создаем директорию для кэша
            os.makedirs(cache_dir, exist_ok=True)

            # Генерируем имя файла кэша
            key = get_cache_key(func.__name__, args, kwargs)
            cache_file = os.path.join(cache_dir, f"{key}.pkl")

            # Пытаемся прочитать из кэша
            if os.path.exists(cache_file):
                with open(cache_file, 'rb') as f:
                    return pickle.load(f)

            # Если кэша нет - выполняем функцию
            result = func(*args, **kwargs)

            # Сохраняем результат
            with open(cache_file, 'wb') as f:
                pickle.dump(result, f)

            return result

        return wrapper

    return decorator


@cache_func()
@timer
def slow_func(x):
    time.sleep(5)
    ans = x ** x * x ** x
    return ans

class Combined_data():
    def __init__(self, list_of, dict_of):
        self.list_of = list_of
        self.dict_of = dict_of

class Window_size():
    def __init__(self, height, length):
        self.height = height
        self.length = length

def main():
    list_of = [1, 2, 3, 4, 5]
    dict_of = {
        'user1': 'example@gmail.com',
        'user2': 'scg2211@gmail.com',
        'John123': 'ddr99@gmail.com'
    }

    combined_obj = Combined_data(list_of, dict_of)

    print(combined_obj, combined_obj.list_of, combined_obj.dict_of)
    Serialization.serialize_to_file(combined_obj, "file_sample.pkl")

    loaded_data = Serialization.deserialize_from_file("file_sample.pkl")
    print(loaded_data, loaded_data.list_of, loaded_data.dict_of)



    tree = Serialization.create_sample_tree()
    print("\n\nИсходное дерево:")
    Serialization.print_tree(tree)

    Serialization.serialize_to_file(tree, "tree.pkl")
    restored_tree = Serialization.deserialize_from_file("tree.pkl")
    print("\n\nЗагруженное дерево:")
    Serialization.print_tree(restored_tree)

    current_win = Window_size(300, 400)
    Serialization.serialize_to_file(current_win, "current_win.pkl")
    loaded_win = Serialization.deserialize_from_file("current_win.pkl")
    print(f"\n\nLoaded window size:{loaded_win.height}x{loaded_win.length}")


    print(slow_func(15))
    print(slow_func(15))
    print(slow_func(15))

if __name__ == '__main__':
    main()
