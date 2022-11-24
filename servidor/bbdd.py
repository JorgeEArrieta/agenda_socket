from peewee import SqliteDatabase
from peewee import Model
from peewee import AutoField
from peewee import CharField
from peewee import IntegerField
from peewee import fn


#Implementación del ORM.

try:

    ddbb = SqliteDatabase('base_datos.db')

    class BaseModel(Model):
    
        class Meta:
        
            database = ddbb

    class Agenda (BaseModel):
    
        id =  AutoField(unique=True)
        nombre = CharField()
        apellido = CharField()
        direccion = CharField()
        partido = CharField()
        provincia = CharField()
        telefono = IntegerField()
    
    ddbb.connect()
    ddbb.create_tables([Agenda])

except:
    pass


def nuevo_registro(name, lname, dire, par, prov, tel):
    """
    Crea un registro en la bbdd.
    """
    registro = Agenda()
    registro.nombre = name
    registro.apellido = lname
    registro.direccion = dire
    registro.partido = par
    registro.provincia = prov
    registro.telefono = tel
    registro.save()


def act_registro(registro, name, lname, dire, par, prov, tel):
    """
    Modifica un registro en la bbdd.
    """

    actualizar = Agenda.update(nombre = name, apellido = lname, direccion = dire,
                 partido = par, provincia = prov, telefono = tel).where(Agenda.id == registro)

    actualizar.execute()


def del_registro(registro):
    """
    Elimina un registro en la bbdd.
    """
    
    try:
        eliminar = Agenda.get(Agenda.id == registro)
        eliminar.delete_instance()

    except:
        print('No existe el registro seleccionado.')


def lectura_bbdd():
    """
    Recompila los registros en la bbdd.
    """

    try:
        min_id = Agenda.select(fn.MIN(Agenda.id)).scalar()
        max_id = Agenda.select(fn.MAX(Agenda.id)).scalar()
    
        identificador = int(min_id)

        f_list= list()
    
        while identificador <= max_id:
        
            query = Agenda.select(Agenda.id, Agenda.nombre, Agenda.apellido, Agenda.direccion,
                          Agenda.partido, Agenda.provincia, Agenda.telefono).where(Agenda.id==identificador)
            for row in query:
                f_list.append(str(row.id) + '|' + str(row.nombre) + '|' + str(row.apellido) + '|' +
                              str(row.direccion) + '|' + str(row.partido) + '|' + str(row.provincia) + '|' +
                              str(row.telefono))
        
            identificador += 1
    
        f_list.append('|end|')

        return f_list

    except TypeError:

        print('Sin datos en bbdd.')

def check_id(registro):

    """
    Verifica que exista un registro en la BBDD.
    """

    resultado = None

    query = Agenda.select(Agenda.id).where(Agenda.id==registro)

    for row in query:
        resultado = str(row.id)

    if resultado == registro:
        return 'T'
    else:
        return 'F'