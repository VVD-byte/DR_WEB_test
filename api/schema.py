import hashlib

from asyncpgsa import create_pool


class DBConnect:
    def __init__(self, pg_connection):
        self._pg = pg_connection

    async def insert(self, *args, **kwargs):
        """
        Создает запись
        """
        async with self._pg.transaction() as conn:
            await conn.fetch("INSERT INTO file VALUES ('%s', %s, '%s')"
                                          % (kwargs.get('hash', ''), kwargs.get('time', 0), kwargs.get('name', ''))
                                          )

    async def select(self, *args, **kwargs):
        """
        Проверяет наличие файла в бд по хэшу и проверяет валидность токена
        :return: bool
        """
        async with self._pg.transaction() as conn:
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
            async with self._pg.transaction() as conn:
                dat = await conn.fetch(f"DELETE FROM file WHERE hash='{kwargs.get('hash')}'")
                return True
        return False
