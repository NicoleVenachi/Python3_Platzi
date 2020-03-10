# -*- coding: utf-8 -*-
"""Capitulo 3, Ahora clientes son una lista."""
import sys
clients = ['pablo', 'ricardo']


def create_clients(client_name):  # Crear nuevo Cliente
    """Create a new client."""
    global clients

    if client_name not in clients:
        clients.append(client_name)
    else:
        print('The client name is alredy in the client\'s list')


def list_clients():  # Listar clientes
    """List all of the clients in the DB."""
    global clients

    for idx, client in enumerate(clients):
        print('{}: {}'.format(idx, client))


def update_client(client_name, updated_client_name):  # Operacion modificar
    """Update some name client in the DB."""
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_client_name
    else:
        print("Client isn\'t in the client list")


def delete_client(client_name):
    """Delete some client name in the DB."""
    global clients

    if client_name in clients:
        clients.remove(client_name)
    else:
        print("Client isn\'t in the client list")


def search_client(client_name):
    """Buscar algun cliente."""
    global clients

    for client in clients:
        if client != client_name:
            continue
        else:
            return True


def _get_client_name():
    client_name = None
    while not client_name:
        client_name = input('What is the client name? \t')
        if client_name == 'exit':
            client_name = None
            break
        else:
            pass
    if not client_name:
        sys.exit()
    return client_name


def _print_welcome():
    """Print a menu."""
    print('Welcome')
    print('x' * 50)
    print('What wouldyou like to do today?')
    print('[C]reate Client')
    print('[L]ist Clients')
    print('[D]elete Client')
    print('[U]pdate Client')
    print('[S]earch Client')


if __name__ == '__main__':
    _print_welcome()
    command = input()
    command = command.upper()  # Pongo en mayuscula el input

    if command == 'C':  # Crear nuevo cliente
        client_name = _get_client_name()  # Pido nombre
        create_clients(client_name)  # Creo cliente con dicho nombre
        list_clients()  # Listo el total de clientes

    elif command == 'L':  # Listar clientes
        list_clients()

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
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(
                client_name)
            )
        list_clients()

    else:  # Opcion invalida
        print('Invalid Command')
