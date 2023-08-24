credenciales = {
    "user": "user123",
    "administrador123": "administrador123",
    "superuser": "superuser"
}

def autenticacion(nivel):
    def decorator(func):
        def wrapper(user, contraseña, *args, **kwargs):
            if (user in credenciales) and (credenciales[user] == contraseña):
                if nivel == "user":
                    return func(*args, **kwargs) if user == "user" else nivel + "Autenticación fallida."
                elif nivel == "administrador":
                    return func(*args, **kwargs) if user == "administrador123" else nivel + "Autenticación fallida."
                elif nivel == "superuser":
                    return func(*args, **kwargs) if user == "superuser" else nivel + "Autenticación fallida."
                else:
                    return "El nivel de autenticación no es valido."
            return nivel + "||Autenticación fallida||"
        return wrapper
    return decorator

@autenticacion(nivel="user")
def usuario():
    return "Usuario ||Autenticación  Aceptada||"

@autenticacion(nivel="administrador")
def administrador():
    return "Administrador ||Autenticación  Aceptada||"

@autenticacion(nivel="superuser")
def superusuario():
    return "Superuser ||Autenticación  Aceptada||"

print(usuario("user", "user123"))
print(administrador("administrador123", "administrador"))
print(superusuario("superuser", "superuser"))