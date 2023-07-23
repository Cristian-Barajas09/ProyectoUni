from dotenv import dotenv_values
from private.connection_sql import App
from pymysql.cursors import DictCursor
from tkinter.messagebox import showerror

config = dotenv_values('.env')

try:
    keys_db = {
        "host": config.get("HOST_DATABASE"),
        "user": config.get("USER_DATABASE"),
        "database": config.get("DATABASE"),
        "cursorclass": DictCursor
    }
    if config.get('PASSWORD_DATABASE'):
        keys_db["password"] = config.get("PASSWORD_DATABASE")

except KeyError as error:
    showerror("error","no se encontraron las variables de entorno")
    print(error)
    App()
