from dotenv import dotenv_values
from private.connection_sql import App
from pymysql.cursors import DictCursor
config = dotenv_values('.env')

try:
    keys_db = {
        "host": config['HOST_DATABASE'],
        "user": config['USER_DATABASE'],
        "database": config['DATABASE'],
        "cursorclass": DictCursor
    }
except KeyError as error:
    print("no se encontraron las variables de entorno")
    App()