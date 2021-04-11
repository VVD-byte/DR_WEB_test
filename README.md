# DR_WEB_test
Запросы: <br />
  ```/token``` - ```GET``` - генерирует и возвращает персональный токен <br />
  ```/``` - ```POST``` - сохраняет в файловое системе переданный документ и возвращает хэш, принимает параметр token-ваш персанальный токен <br />
  ```/``` - ```GET``` - возвращает файл, принимает параметры token-ваш персанальный токен и hash-хэш файла <br />
  ```/``` - ```DELETE``` - удаляет файл, принимает параметры token-ваш персанальный токен и hash-хэш файла <br />

##Создание базы данных
Устанавливаете postgresql <br />
Запускаете его - ```sudo systemctl start postgresql```<br />
Заходите под пользователем postgres - ```sudo su postgres```<br />
Заходите в postgresql - ```psql```<br />
Создаете нового пользователя - ```CREATE USER wanuser;```<br />
Задаем пользователю пароль - ```ALTER USER wanuser WITH PASSWORD 'mysecretpassword';```<br />
Создаем миграции ```alembic revision --message="Initial" --autogenerate```<br />
Применяем миграции - ```alembic upgrade head```<br />

##Установка демона
```git clone https://github.com/VVD-byte/DR_WEB_test``` - клонируем приложение с гита<br />
```python -m venv venv``` - создание вертуального окружения<br />
```source venv/bin/activate``` - вход в виртуальное окружение<br />
```pip install DR_WEB_test/requirements.txt``` - установка необходимых зависимостей<br />
```sudo mv DR_WEB_test/filemanager.service /etc/systemd/system/```<br />
```sudo systemctl daemon-reload```<br />
```sudo systemctl enable filemanager.service```<br />
```sudo systemctl start filemanager.service```<br />

## Установка с Docker
```git clone https://github.com/VVD-byte/DR_WEB_test``` - клонируем приложение с гита<br />
```sudo docker build -t drweb-test .``` - создаем докер<br />
```sudo docker run drweb-test``` - запускаем докер<br />

## Запуск без Docker и демонов
Запуск - ```python -m api``` <br />


## Примеры запросов
Пример взаимодействия с api лежит в файле requests.txt<br />
