import psycopg2
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

try:
    conn = psycopg2.connect(
        database=os.getenv('FSTR_DB_NAME'),
        host=os.getenv('FSTR_DB_HOST'),
        port=os.getenv('FSTR_DB_PORT'),
        user=os.getenv('FSTR_DB_LOGIN'),
        password=os.getenv('FSTR_DB_PASS'),
    )
    # пытаемся подключиться к базе данных
except psycopg2.Error as e:
    # в случае сбоя подключения будет выведено сообщение в STDOUT
    print('Can`t establish connection to database', e)
else:
    print('Connection established')



class DataManipulate:
    pass
