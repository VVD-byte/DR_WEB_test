# DR_WEB_test
Запуск - ```python -m api``` <br />
Запросы: <br />
  ```/token``` - ```GET``` - генерирует и возвращает персональный токен <br />
  ```/``` - ```POST``` - сохраняет в файловое системе переданный документ и возвращает хэш, принимает параметр token-ваш персанальный токен <br />
  ```/``` - ```GET``` - возвращает файл, принимает параметры token-ваш персанальный токен и hash-хэш файла <br />
  ```/``` - ```DELETE``` - удаляет файл, принимает параметры token-ваш персанальный токен и hash-хэш файла <br />
