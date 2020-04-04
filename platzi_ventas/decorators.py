# -*- coding: utf-8 -*-
PASSWORD = '12345'

def password_required(func):
    def wrapper():  # wrapper se usa por convecion
        password = input('Cuál es tu contraseña? \t')

        if (password == PASSWORD):
            return func()
        else:
            print('La contraseña es incorrecta')
    return wrapper  # Limito acceso a funcion a situaciones restrigidas


@password_required
def needs_password():
    print('La contraseña es correcta')


def upper(func):
    def wrapper(*args, **kwargs):  # Recibo parametros, y en sgte linea los paso. Asi no determio de antemano quienes son los parametros
        result = func(*args, **kwargs)  # Paso a la func los parametros

        return result.upper()  # Tomo el nombre y lo devuelvo en mayusculas
    return wrapper


@upper
def say_my_name(name):
    return 'Hola {}'.format(name)


if __name__ == '__main__':
    print(say_my_name('David'))
