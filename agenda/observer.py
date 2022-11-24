from peewee import DateTimeField
from peewee import Model
from peewee import CharField
from peewee import SqliteDatabase
from peewee import AutoField
from datetime import datetime

try:

    ddbb = SqliteDatabase('base_datos.db')

    class BaseModel(Model):
    
        class Meta:
        
            database = ddbb

    class Registro (BaseModel):
        id =  AutoField(unique=True)
        evento =  CharField()
        fecha = DateTimeField(default=datetime.now())
    
    ddbb.connect()
    ddbb.create_tables([Registro])

except:
    pass

class Observer():
    
    def __init__(self, estado):
        self.estado = estado

    def update(self):
        """
        Registra los cambios de estado en una base de datos.
        """
        #Se crea la base de datos.
        reg = Registro()
        reg.evento = self.estado
        reg.save()

    

