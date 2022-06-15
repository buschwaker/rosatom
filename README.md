[![](https://img.shields.io/badge/python-3.7.0-green)](https://img.shields.io/badge/python-3.7.0-green)
[![](https://img.shields.io/badge/Django-1.10-yellowgreen)](https://img.shields.io/badge/Django-1.10-yellowgreen)
[![](https://img.shields.io/badge/PostgreSQL-11.1-red)](https://img.shields.io/badge/PostgreSQL-11.1-red)
[![](https://img.shields.io/badge/Bootstrap-5-blue)](https://img.shields.io/badge/Bootstrap-5-blue)
# Проект для Электрохимприбор
## Особенности проекта
<p>Приложение представляет из себя справочник должностей и список сотрудников компании.</p>

- Пользователю без административных полномочий доступно:
    - Просмотр списка сотрудников
    - Просмотр списка должностей
- Пользователю, обладающим административными полномочиями доступно:
    - То же, что и пользователю без административных полномочий
    - Создание, изменение, удаление новых сотрудников
    - Создание, изменение, удаление новых должностей
    - Создание аккаунта нового пользователя сайтом
    
## Структура проекта

Проект состоит из 3 приложений: `jobs, users, core`.

1. Приложение `jobs` определяет структуру хранимых данных, связанных с моделями: `Employee, Position`, включает в себя формы, связанные с соответствующими моделями, а также пользовательский виджет для поля `дата рождения`. <br> Настраивает отображение объектов моделей в форме администратора. Включает URL-шаблоны для доступа к ресурсам сайта и функции представления, обрабатывающие запросы по соответствующим эндпоинтам.
2. Приложение `users` отвечает за систему аутентификации и регистрации пользователей.
3. Приложение `core` включает в себя пользовательские фильтры для HTML-шаблонов.

## Доступ к проекту по удаленному серверу

Просмотреть рабочий проект можно [здесь](http://buschwacker.pythonanywhere.com/)
<br><br>
Логин/Пароль администратора<br> логин: `admin`, пароль: `Akroshko_1995`<br>
Логин/Пароль пользователя без административных прав<br> логин: `erick`, пароль: `Akroshko_1995`



