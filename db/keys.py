from dotenv import dotenv_values
from private.connection_sql import App
config = dotenv_values('.env')

try:
    keys_db = {
        "host": config['HOST_DATABASE'],
        "user": config['USER_DATABASE'],
        "database": config['DATABASE']
    }
except KeyError as error:
    print("no se encontraron las variables de entorno")
    App()