"""Datos, clientes sobre los que interactuo."""
import uuid  # Libreria para generar ids unicas

class Client:
    def __init__(self, name, company, email, position, uid = None):
        self.name = name
        self.company = company
        self.email = email
        self.position = position
        self.uid = uid or uuid.uuid4()  # Si manda uid, lo uso, sino uuid4 que es el usado en la industria
        pass

    def to_dict(self):
        return vars(self)  #Convierte objeto en diccionario, para escritura a csv en disco

    @staticmethod
    def schema():
         return ['name', 'company', 'email', 'position', 'uid']  # Regresa el Esquema de datos de la tabla (keys)
