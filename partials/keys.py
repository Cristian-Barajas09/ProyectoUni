from dotenv import dotenv_values
from private.connection_sql import App
from pymysql.cursors import DictCursor
from tkinter.messagebox import showerror

config = dotenv_values('.env')

try:
    keys_db = {
        "host": config["HOST_DATABASE"],
        "user": config["USER_DATABASE"],
        "database": config["DATABASE"],
        "cursorclass": DictCursor
    }
    if config['PASSWORD_DATABASE']:
        keys_db["password"] = config["PASSWORD_DATABASE"]



except KeyError as error:
    showerror("error","no se encontraron las variables de entorno")

    App()
