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
