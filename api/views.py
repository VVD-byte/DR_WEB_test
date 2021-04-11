from aiohttp.web import View
import hashlib
from .utils import create_if_not_exist_dir, gen_token, chek_file
import time
import json
import os
from aiohttp import web
from .schema import DBConnect


def serialise(func):
    async def warp(*args, **kwargs):
        return web.Response(text=json.dumps(await func(*args, **kwargs)))

    return warp


class WorkWithFile(View):
    async def get(self):
        hash_ = self.request.query.get('hash', '')
        if await self.request.app.get('db_controller').select(hash=hash_, token=self.request.query.get('token', '')):
            return web.FileResponse(f'store/{hash_[0:2]}/{hash_}')
        return web.Response(text=json.dumps({'error': 'Premission denied'}))

    @serialise
    async def post(self):
        if self.request.can_read_body and len(self.request.query.get('token', '')) == 64:
            async for obj in await self.request.multipart():
                if not obj.filename is None:
                    time_ = int(time.time())
                    hash_ = hashlib.sha256(bytes(f'{obj.filename} - {time_} - '
                                                 f'{self.request.query.get("token")}', 'utf-8')).hexdigest()
                    await create_if_not_exist_dir(hash_[0:2])
                    with open(f'./store/{hash_[0:2]}/{hash_}', 'wb') as t:
                        t.write(await obj.read())
                    await self.request.app.get('db_controller').insert(name=obj.filename, hash=hash_, time=time_)
                    return {'hash': hash_}
        return {'error': 'bad data'}

    @serialise
    async def delete(self):
        hash_ = self.request.query.get('hash')
        token = self.request.query.get('token', '')
        if await chek_file(hash_) and await self.request.app.get('db_controller').delete_row(hash=hash_, token=token):
            os.remove(f'store/{hash_[0:2]}/{hash_}')
        else:
            return {'error': 'file not found'}
        return {'delete': hash_}


class Token(View):
    @serialise
    async def get(self):
        return {'token': await gen_token()}
