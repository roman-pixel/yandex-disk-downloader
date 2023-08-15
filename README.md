# Яндекс диск worker

[![Button Icon]][Link] 

## Как пользоваться программой

- добавьте/обновите токен, если токен не найден/не валиден
- укажите путь до папки в формате "/some/path" (если это корень диска - оставьте пустым и нажмите Enter)
- дождитесь окончания загрузки файлов
- вы можете удалить файлы c Яндекс диска после окончания загрузки
- все скачанные файлы будут находится в папке *"download"*

## Сборка программы
Для сборки исполняемого файла запустите командную строку и введите следующую команду:

```sh
pyinstaller --onefile --icon=icon.ico yadisk_downloader.py --name "Яндекс диск downloader"
```

*Вы также можете сделать сборку с помощью программы "auto_assembly.py" на вашем локальном компьютере*

[Button Icon]: https://img.shields.io/badge/Installation-EF2D5E?style=for-the-badge&logoColor=white&logo=DocuSign
[Link]: https://disk.yandex.ru/d/k99KrjewiRh_wA
