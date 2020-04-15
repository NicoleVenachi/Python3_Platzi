"""Entry Point."""
# -*- coding: utf-8 -*-
import click
from clients import commands as clients_commands
CLIENTS_TABLE = '.clients.csv'

@click.group()  # Con este digo a click el pto de entrada
@click.pass_context  # Objeto contexto
def cli(ctx):
    ctx.obj = {}  # Inicializo ctx como dict vacio
    ctx.obj['clients_table'] = CLIENTS_TABLE  # El primer elemento contextual es la tabla from disk

cli.add_command(clients_commands.all)
