import bcrypt
from .rutas import dir
import dotenv
def encryptPassword(password:str):
    """
        nos permite encriptar cosas no solo claves
    """
    salt          = bcrypt.gensalt(10)
    bytesPassword =  password.encode('utf-8')
    hashed        =  bcrypt.hashpw(bytesPassword,salt).decode()

    return hashed

def matchPassword(password,savedPassword):
    """
        saber si lo que encriptamos coincide con lo ingresado
    """
    if not isinstance(savedPassword,bytes):
        savedPassword = bytes(savedPassword or "","utf-8")
    try:
        return  bcrypt.checkpw(bytes(password,"utf-8"),savedPassword)
    except ValueError:
        return False

def generate_env_value(key,value):
        file = open(f"{dir}/.env",'r').readlines()
        print(file)
        print(f"{key} = {value}" in file)
        if f"{key} = {value}\n" in file:
            print(key)
            result = file.index(f"{key} = {value}\n")
            file[result] = f"{key} = {value}\n"
            out = open(f"{dir}/.env",'w')
            out.writelines(file)

            out.close()
        else :
            with open(f"{dir}/.env",'a+') as file:
                file.write(f"\n{key} = {value}\n")

def read_env_value(key):
    env = dotenv.dotenv_values()

    return env.get(key)