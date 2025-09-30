import os

def load_file():
    filename = input("Введите имя файла для загрузки: ")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Содержимое файла:\n{content}")
            return content
    except FileNotFoundError:
        print("Файл не найден!")
        return None

def save_file():
    filename = input("Введите имя файла для сохранения: ")
    content = input("Введите содержимое файла: ")
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print("Файл успешно сохранен!")
    except Exception as e:
        print(f"Ошибка при сохранении: {e}")
3
def main_menu():
    print("=== Меню ===")
    print("1. Загрузить файл")
    print("2. Сохранить файл")
    print("3. Выход")
    return input("Выберите опцию: ")

def main():
    while True:
        choice = main_menu()
        if choice == "1":
            load_file()
        elif choice == "2":
            save_file()
        elif choice == "3":
            break
        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()