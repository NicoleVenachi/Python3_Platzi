"""Capitulo1 y 2, Intorduccion y Secuencias."""
# -*- coding: utf-8 -*-
import sys
clients = 'pablo,ricardo,'


def create_clients(client_name):
    """Create a new client."""
    global clients

    if client_name not in clients:
        clients += client_name
        _add_coma()
    else:
        print('The client name is alredy in the client\'s list')  # Crear nuevo Cliente


def list_clients():
    """List all of the clients in the DB."""
    global clients

    print(clients)  # Listar clientes


def update_client(client_name, updated_client_name):
    """Update some name client in the DB."""
    global clients

    if client_name in clients:
        clients = clients.replace(client_name, updated_client_name)
    else:
        print("Client isn\'t in the client list")  # Operacion modificar


def delete_client(client_name):
    """Delete some client name in the DB."""
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', '')
    else:
        print("Client isn\'t in the client list")


def search_client(client_name):
    """Buscar algun cliente."""
    global clients
    clients_list = clients.split(',')

    for client in clients_list:
        if client != client_name:
            continue
        else:
            return True


def _get_client_name():
    client_name = None
    while not client_name:
        client_name = input('What is the client name? \t')
        if client_name == 'exit':  # Si digito exit, nombre sigue vacio
            client_name = None
            break
        else:
            pass
    if not client_name:
        sys.exit()  # Si dijito exit, salgo del programa
    return client_name  # Obtiene input de nnombre de cliente o cierra programa


def _add_coma():
    """Add a coma to separate the cleint's names."""
    global clients
    clients += ','  # Anadir coma a clientes


def _print_welcome():
    """Print a menu."""
    print('Welcome')
    print('x' * 50)
    print('What wouldyou like to do today?')
    print('[C]reate Client')
    print('[D]elete Client')
    print('[U]pdate Client')
    print('[S]earch Client')  # Mostrar menu de bienvenida


if __name__ == '__main__':
    _print_welcome()  # Menu de inicio
    command = input()  # Pido operacion a realizar
    command = command.upper()  # Pongo en mayuscula el input
    # Ejecuto funcion ingresada
    if command == 'C':  # Crear nuevo cliente
        client_name = _get_client_name()  # Pido nombre
        create_clients(client_name)  # Creo cliente con dicho nombre
        list_clients()  # Listo el total de clientes

    elif command == 'D':  # Eliminar cliente
        client_name = _get_client_name()  # Recibo nombre
        delete_client(client_name)  # Eliimino
        list_clients()  # Listo

    elif command == 'U':  # Actualizo algun cliente
        client_name = _get_client_name()  # Recojo nombre aremplazar
        updated_client_name = input(
            'What is the name that you want to repleace?'
        )  # Nombre por el cual remplazar
        update_client(client_name, updated_client_name)
        list_clients()  # Listo clientes

    elif command == 'S':  # Buscar cliente
        client_name = _get_client_name()  # Recibo nombre
        found = search_client(client_name)  # Busco

        if found:  # Mensaje, encontro o no
            print('The client is the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(
                client_name)
            )
        list_clients()

    else:  # Opcion invalida
        print('Invalid Command')
