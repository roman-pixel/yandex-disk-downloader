import os
import yadisk
import base64


def create_token():
    print("Введите новый токен:")
    token = input()

    # Кодирование токена
    encoded_token = base64.b64encode(token.encode("utf-8")).decode("utf-8")

    # # Сохранение закодированного токена в файл
    with open("token", "w") as token_file:
        token_file.write(encoded_token)

    if os.name == "nt":
        # В Windows, добавляем атрибут скрытого файла
        file_attributes = os.stat("token").st_file_attributes
        os.stat("token").st_file_attributes = file_attributes | 2
    elif os.name == "posix":
        # В macOS, добавляем точку перед именем файла, чтобы его было сложнее найти
        os.rename("token", ".token")
    else:
        return


def token():
    # Определение пути к скрытому файлу в зависимости от операционной системы
    if os.name == "posix":
        # Linux и macOS
        hidden_file_path = ".token"
    elif os.name == "nt":
        # Windows
        hidden_file_path = "token"

    # Чтение закодированного токена из файла
    with open(hidden_file_path, "r") as token_file:
        encoded_token = token_file.read()

    # Декодирование токена
    decoded_token = base64.b64decode(encoded_token).decode("utf-8")

    return decoded_token


def main():
    yadisk_token = ''
    count_downloaded_files = 0

    if not os.path.isfile('token'):
        print("Файл token не найден")
        print("Создать новый файл? [Y/n]")
        confirm_create_token = input()

        if confirm_create_token.casefold() == 'y':
            create_token()
            yadisk_token = yadisk.YaDisk(token=token())
        elif confirm_create_token.casefold() == 'n':
            return
        else:
            print('Неверное значение')
            return
    else:
        yadisk_token = yadisk.YaDisk(token=token())

    print("Проверка валидности токена:")
    try:
        if yadisk_token.check_token():
            print("токен валиден")
        else:
            print("токен не валиден")
            print("Хотите обновить токен? [Y/n]")
            confirm_create_token = input()

            if confirm_create_token.casefold() == 'y':
                create_token()
                yadisk_token = yadisk.YaDisk(token=token())
            elif confirm_create_token.casefold() == 'n':
                return
            else:
                print('Неверное значение')
                return
    except Exception as e:
        print(f"ошибка проверки токена:\n{e}")
        return

    print("\nВведите путь до папки в формате \"/some/path\" (если это корень диска - оставьте пыстым и нажмите Enter):")
    dir = input()

    # Получает общую информацию о диске
    # print(y.get_disk_info())

    # Выводит содержимое "/some/path"
    try:
        file_list = list(yadisk_token.listdir(dir))
    except Exception as e:
        print(f"Ошибка при чтении дирректории:\n{e}")

    print("Начинаю скачивание (это может занять некоторое время)")

    if not os.path.exists("download"):
        os.mkdir("download")

    for file in file_list:
        if file.type == 'file':
            try:
                print(f'Скачивается: {file.name}')
                yadisk_token.download(
                    f"{dir}/{file.name}", f"download/{file.name}")
                count_downloaded_files += 1
            except Exception as e:
                print(f"Не удалось скачать {file.name}. Ошибка:\n{e}")
                continue

    print(f'\nСкачано файлов: {count_downloaded_files}')

    # # Безвозвратно удаляет "/file-to-remove"
    if dir != '':
        print(
            f"\nВы действительно хотите безвозвратно удалить \"/{dir}\"? [Y/n]")
        confirm_del = input()

        if confirm_del.casefold() == 'y':
            yadisk_token.remove(dir, permanently=True)
            print('Папка удалена')
        elif confirm_del.casefold() == 'n':
            return
        else:
            print('Неверное значение')
            return
    else:
        print(
            f"\nВы действительно хотите безвозвратно удалить {count_downloaded_files} файлов? [Y/n]")
        confirm_del = input()

        if confirm_del.casefold() == 'y':
            for file in file_list:
                if file.type == 'file':
                    yadisk_token.remove(file.name, permanently=True)
            print('Файлы удалены')
        elif confirm_del.casefold() == 'n':
            return
        else:
            print('Неверное значение')
            return


main()
