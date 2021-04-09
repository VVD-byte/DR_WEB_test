import os
import hashlib
import random
import time


async def create_if_not_exist_dir(dir):
    if not os.path.exists(f'./store/{dir}'):
        os.mkdir(f'./store/{dir}')


async def gen_token():
    return hashlib.sha256(bytes(f'{int(time.time())} - '
                                f'{random.randint(1,99999999999999999)} - {random.randint(1,99999999999999999)}',
                                'utf-8')).hexdigest()


async def chek_file(hash_):
    if os.path.exists(f'store/{hash_[0:2]}/{hash_}'):
        return True
    return False
