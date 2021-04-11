# DR_WEB_test
Запросы: <br />
  ```/token``` - ```GET``` - генерирует и возвращает персональный токен <br />
  ```/``` - ```POST``` - сохраняет в файловое системе переданный документ и возвращает хэш, принимает параметр token-ваш персанальный токен <br />
  ```/``` - ```GET``` - возвращает файл, принимает параметры token-ваш персанальный токен и hash-хэш файла <br />
  ```/``` - ```DELETE``` - удаляет файл, принимает параметры token-ваш персанальный токен и hash-хэш файла <br />

##Создание базы данных
Устанавливаете postgresql <br />
Запускаете его - ```sudo systemctl start postgresql```
Заходите под пользователем postgres - ```sudo su postgres```
Заходите в postgresql - ```psql```
Создаете нового пользователя - ```CREATE USER wanuser;```
Задаем пользователю пароль - ```ALTER USER wanuser WITH PASSWORD 'mysecretpassword';```
Создаем миграции ```alembic revision --message="Initial" --autogenerate```
Применяем миграции - ```alembic upgrade head```

##Установка демона
```git clone https://github.com/VVD-byte/DR_WEB_test``` - клонируем приложение с гита
```python -m venv venv``` - создание вертуального окружения
```source venv/bin/activate``` - вход в виртуальное окружение
```pip install DR_WEB_test/requirements.txt``` - установка необходимых зависимостей
```sudo mv DR_WEB_test/filemanager.service /etc/systemd/system/```
```sudo systemctl daemon-reload```
```sudo systemctl enable filemanager.service```
```sudo systemctl start filemanager.service```

## Установка с Docker
```git clone https://github.com/VVD-byte/DR_WEB_test``` - клонируем приложение с гита
```sudo docker build -t drweb-test .``` - создаем докер
```sudo docker run drweb-test``` - запускаем докер

## Запуск без Docker и демонов
Запуск - ```python -m api``` <br />


## Примеры запросов
Пример взаимодействия с api лежит в файле requests.txt
