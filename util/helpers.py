import bcrypt


def encryptPassword(password):
    salt = bcrypt.gensalt(10)
    bytes = password.encode('utf-8')
    hashed = bcrypt.hashpw(bytes,salt)
    return hashed

def matchPassword(password,savedPassword):
    print(password,savedPassword)
    if not isinstance(savedPassword,bytes):
        savedPassword = bytes(savedPassword or "","utf-8")
        print(type(savedPassword))
    try:
        return bcrypt.checkpw(bytes(password,"utf-8"),savedPassword)
    except ValueError:
        return False
