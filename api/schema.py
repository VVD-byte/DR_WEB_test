from asyncpgsa import create_pool
import hashlib


class DBMixin:
    @staticmethod
    async def insert(*args, **kwargs):
        """
        Создает запись
        """
        async with create_pool(host='localhost', port=5432, database='analyzer',
                               user='wanuser', min_size=5, max_size=10) as pool:
            async with pool.transaction() as conn:
                await conn.fetch("INSERT INTO file VALUES ('%s', %s, '%s')"
                                          % (kwargs.get('hash', ''), kwargs.get('time', 0), kwargs.get('name', ''))
                                          )

    @staticmethod
    async def select(*args, **kwargs):
        """
        Проверяет наличие файла в бд по хэшу и проверяет валидность токена
        :return: bool
        """
        async with create_pool(host='localhost', port=5432, database='analyzer',
                               user='wanuser', min_size=5, max_size=10) as pool:
            async with pool.transaction() as conn:
                try:
                    dat = await conn.fetch(f"SELECT * FROM file WHERE hash='{kwargs.get('hash', '')}'")

                    if hashlib.sha256(bytes(f'{dat[0]["filename"]} - {dat[0]["time"]} - {kwargs.get("token")}',
                                            'utf-8')).hexdigest() == dat[0]['hash']:
                        return True
                except:
                    pass
        return False

    async def delete_row(self, *args, **kwargs):
        """
        Удаляет запись по хэшу
        :return: bool
        """
        if self.select(*args, **kwargs):
            async with create_pool(host='localhost', port=5432, database='analyzer',
                                   user='wanuser', min_size=5, max_size=10) as pool:
                async with pool.transaction() as conn:
                    dat = await conn.fetch(f"DELETE FROM file WHERE hash='{kwargs.get('hash')}'")
                    return True
        return False
