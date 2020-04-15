"""Logica de negocio, acciones del programa."""
import csv
import os
from clients.models import Client
class ClientService:
    def __init__(self, table_name):  # Recibe el nombre dell archivo donde se guardan los datos (Recibe datos)
        self.table_name = table_name


    def create_client(self, client):
        with open(self.table_name, mode='a') as f:
            writter = csv.DictWriter(f, fieldnames = Client.schema())
            writter.writerow(client.to_dict())  # Escribe cliente en tabla


    def list_clients(self):
        with open(self.table_name, mode='r') as f:
            reader = csv.DictReader(f, fieldnames = Client.schema())

            return(list(reader))  # :isto clientes


    def update_client(self, updated_client):
        clients = self.list_clients()  # Veo la lista de los clientes
        updated_clients = []
        for client in clients:
            if client['uid'] == updated_client.uid:
                updated_clients.append(updated_client.to_dict())  # Lo paso a diccionario para escribir en el archivo de comas, eso significa que el updated client es una instancia del modelo
            else:
                updated_clients.append(client)  # Si los clientes tienen el mismo id, lo actualiza

        self._save_to_disk(updated_clients)


    def _save_to_disk(self, clients):
        tmp_table_name = self.table_name + '.tmp'
        with open(tmp_table_name, mode='w') as f:
            writter = csv.DictWriter(f, fieldnames = Client.schema())
            writter.writerows(clients)
        os.remove(self.table_name)
        os.rename(tmp_table_name, self.table_name)


    def delete_client(self, client_to_delete):
        clients = self.list_clients()
        for client in clients:
            if client_to_delete.uid == client['uid']:
                clients.remove(client)
                break
            else:
                continue
        self._save_to_disk(clients)
