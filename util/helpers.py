import bcrypt

def encryptPassword(password:str):
    salt          = bcrypt.gensalt(10)
    bytesPassword =  password.encode('utf-8')
    hashed        =  bcrypt.hashpw(bytesPassword,salt).decode()

    return hashed

def matchPassword(password,savedPassword):
    if not isinstance(savedPassword,bytes):
        savedPassword = bytes(savedPassword or "","utf-8")
    try:
        return  bcrypt.checkpw(bytes(password,"utf-8"),savedPassword)
    except ValueError:
        return False


def calendar_format(date:str):
    lista = []
    for i in date:
        if i.isdigit():
            lista.append(i)
    print(lista)

date = "08/30/04"

# calendar_format(date)