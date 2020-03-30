"""Capitulo 3, Ahora con archivos del disco."""
# -*- coding: utf-8 -*-
import csv
import os

CLIENT_TABLE = '.clients.csv'  # Abro archivo
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']  # Lista de llaves usadas por csv para construir diccionarios
clients = []  # Inicio con lista vacia

def _initialize_Clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)  # Lee archivo con las llaves

        for row in reader:  # Cada fila es un cliente
            clients.append(row)  # Inicializa lista con diccionarios de clientes


def _save_Clients_to_storage():
    """Una vez abierto un archivo, no se puede reescribir, por eso se usa tabla temporal, le modifico el nombre y elimino tabla inicial."""
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)  # Creo tabla temporal con mismo nombre que la otra, pero extension tmp
    with open(tmp_table_name, mode='w') as f:  # Abro tmp table en modo escritura
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)  # Paso archivo para que lo pueda leer
        writer.writerows(clients)  # Escribe filas con la lista que ya tengo
        os.remove(CLIENT_TABLE)
        os.rename(tmp_table_name, CLIENT_TABLE)  # Guarda en disco los nuvos cleintes


def create_clients(client):  # Crear nuevo Cliente
    """Create a new client."""
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('The client name is alredy in the client\'s list')


def list_clients():  # Listar clientes
    """List all of the clients in the DB."""
    global clients

    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position'])
        )


def update_client(client_id, updated_client):
    """Update some name client in the DB."""
    global clients

    if int(client_id) not in _get_clients_idx_sequence():
        print("Client isn\'t in the client list")
    else:
        clients[int(client_id)] = updated_client  # Actualizo con id


def delete_client(client_id):
    """Delete some client name in the DB."""
    global clients

    if int(client_id) not in _get_clients_idx_sequence():
        print("Client isn\'t in the client list")
    else:
        del clients[int(client_id)]  # Elimino cliente  con id


def search_client(client_name):
    """Buscar algun cliente."""
    global clients

    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True  # Busco con nombre de cliente


def _get_client_field(field_name):
    """Crear algun campo del diccionario de clientes."""
    field = None

    while not field:
        field = input('Which is the client {}? \t'.format(field_name))
    return field  # Pedir un campo, con validacion


def _get_client_from_user():
    """Crear algun cliente."""
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position')
    }

    return client  # Pido campos de cliente


def _get_clients_idx_sequence():
    global clients
    clients_idx = []
    for idx in range(len(clients)):
        clients_idx.append(idx)
    return clients_idx


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
    _initialize_Clients_from_storage()  # Abre csv con clientes
    _print_welcome()
    command = input()
    command = command.upper()  # Pongo en mayuscula el input

    if command == 'C':  # Crear nuevo cliente
        client = _get_client_from_user()
        create_clients(client)  # Creo cliente con dicho nombre
        list_clients()  # Listo el total de clientes

    elif command == 'L':  # Listar clientes
        list_clients()

    elif command == 'D':  # Eliminar cliente
        client_id = _get_client_field('id')  # Recibo id
        delete_client(client_id)  # Eliimino
        list_clients()  # Listo

    elif command == 'U':  # Actualizo algun cliente
        client_id = _get_client_field('id')  # Recojo nombre a remplazar
        print('Which is the info from the new client?')
        updated_client = _get_client_from_user()
        update_client(client_id, updated_client)
        list_clients()  # Listo clientes

    elif command == 'S':  # Buscar cliente
        client_name = _get_client_field('name')  # Recojo nombre a remplazar
        found = search_client(client_name.capitalize())  # Busco

        if found:  # Mensaje, encontro o no
            print('The client is in the client\'s list')
        else:
            print('The client with the name: {} is not in our client\'s list'.format(
                client_name)
            )
        list_clients()

    else:  # Opcion  invalida
        print('Invalid Command')

    _save_Clients_to_storage()  # Tras todas las operaciones, cierra csv con clientes
