# Яндекс диск worker

[![Button Icon]][Link] 

## Как пользоваться программой
- добавьте/обновите токен, если токен не найден/не валиден
- укажите путь до папки в формате "/some/path" (если это корень диска - оставьте пустым и нажмите Enter)
- дождитесь окончания загрузки файлов
- вы можете удалить файлы c Яндекс диска после окончания загрузки
- все скачанные файлы будут находится в папке *"download"*

## Как создать токен
- перейдите по сслыке: *https://oauth.yandex.ru/client/new*
- выберите платформу - Веб-сервисы
- введите данный url: *https://oauth.yandex.ru/verification_code*
- в поле "Доступ к данным" введите следующее значение: **cloud_api:disk**
- выберите все значения из выпадающего списка
- укажите почту для связи
- полная инструкция по созданию токена: *https://yandex.ru/dev/direct/doc/start/register.html*

## Как получить токен
- после создания токена перейдите по ссылке для получения токена: *https://oauth.yandex.ru/authorize?response_type=token&client_id=ИДЕНТИФИКАТОР_ПРИЛОЖЕНИЯ* 
где ИДЕНТИФИКАТОР_ПРИЛОЖЕНИЯ - ClientID
- полная инструкция по получению токена: *https://yandex.ru/dev/direct/doc/start/token.html*

## Сборка программы
Для сборки исполняемого файла запустите командную строку и введите следующую команду:

```sh
pyinstaller --onefile --icon=icon.ico yadisk_downloader.py --name "Яндекс диск downloader"
```

*Вы также можете сделать сборку с помощью программы "auto_assembly.py" на вашем локальном компьютере*

[Button Icon]: https://img.shields.io/badge/Installation-EF2D5E?style=for-the-badge&logoColor=white&logo=DocuSign
[Link]: https://disk.yandex.ru/d/k99KrjewiRh_wA
