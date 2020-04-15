"""Presentacion, Creo comandos basicos del grupo clients, Interfaz."""
# -*- coding: utf-8 -*-
import click
from clients.services import ClientService
from clients.models import Client
@click.group()  # Convierte funciones en comandos de click. Convierte a clients en decorador.
def clients():
    """Manages the clients lifecycle"""
    pass  # Define el grupo al que pertenecen las funciones


@clients.command()  # Hace que este sea un comando de clients
@click.option('-n', '--name',
                type = str,
                prompt = True, # Sino lo dan via patron abreviado, lo pida al usuario. El help es el texto parapedirlo
                help = 'The client name')   # El primer -, indica el shortname, sino lo dan por patron abreviado, lo pide
@click.option('-c', '--company',
                type = str,
                prompt = True, # Sino lo dan via patron abreviado, lo pida al usuario
                help = 'The client company')
@click.option('-e', '--email',
                type = str,
                prompt = True, # Sino lo dan via patron abreviado, lo pida al usuario
                help = 'The client email')
@click.option('-p', '--position',
                type = str,
                prompt = True, # Sino lo dan via patron abreviado, lo pida al usuario
                help = 'The client position')
@click.pass_context
def create(ctx, name, company, email, position):
    """Crete a new client."""
    client = Client(name, company, email, position)
    client_service = ClientService(ctx.obj['clients_table'])  # Del contexto saco el nombre de la tabla. Inicializo los servicios, con su respectiva tabla, es decir, paso datos del cliente

    client_service.create_client(client)  # Creo el cliente


@clients.command()  # Hace que este sea un comando de clients
@click.pass_context
def list(ctx):
    """List all clients"""
    client_service = ClientService(ctx.obj['clients_table'])
    click.echo('  ID  | NAME  |  COMPANY  |  EMAIL  | POSITION  ')
    click.echo('*' * 100)
    for client in client_service.list_clients():
        click.echo('  {uid}  |  {name}  |  {company}  |  {email}  |  {position}  '.format(
            uid= client['uid'],
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position']))


@clients.command()  # Hace que este sea un comando de clients
@click.pass_context
def update(ctx, client_uid):
    """Updates a client"""
    client_service = ClientService(ctx.obj['clients_table'])
    client_list = client_service.list_clients()
    client = [client for client in client_list if client['uid'] == client_uid]

    if client:
        client = _update_client_flow(Client(**client[0]))  # paso instancia de cliente, con el elemento 0, al ser un unco elemento que hace match
        client_service.update_client(client)
        click.echo('Client Updated')  # Si existe lo actualiza
    else:
        click.echo('Client not found')


def _update_client_flow(client):
    click.echo('Leave empty if you don\'t want to modify the value')
    client.name = click.prompt('New name', type =str, default= client.name)
    client.company = click.prompt('New company', type =str, default= client.company)
    client.email = click.prompt('New email', type =str, default= client.email)
    client.position = click.prompt('New position', type =str, default= client.position)
    return client



@clients.command()  # Hace que este sea un comando de clients
@click.pass_context
def delete(ctx, client_uid):
    """Deletes a client"""
    pass

all = clients  # Creo alias a clients
