from cliente import Cliente
import re

class Modelo():

    def check_name(registro):
        """
        Verifica datos de tipo caracter. Solo tienen que ser caracteres de la "a" a la "z" (distingue entre mayúsculas y
        minusculas). Si la cadena a analizar tiene datos no admitidos, devuelve True. Sino, False.
        """
        patron = '[^A-Za-z áéíóúÁÉÍÓÚ]'

        if re.search(patron, registro):
            return True
        else:
            return False


    def check_alphanum(registro):
        """
        Verifica datos de tipo caracter. Solo tienen que ser caracteres de la "a" a la "z" (distingue entre mayúsculas y
        minusculas). Tambien admite números. Si la cadena a analizar tiene datos no admitidos, devuelve True. Sino, False.
        """
        patron = '[^A-Za-z 0-9áéíóúÁÉÍÓÚ]'
        

        if re.search(patron, registro):
            return True
        else:
            return False


    def check_num(registro):
    
        """
        Verifica que la variable "registro" solo contenga numeros enteros. 
        """
        patron = '[^0-9]'

        if re.search(patron, registro):
            return True
        else:
            return False


    def crear_registro(self, name, lname, dire, par, prov, tel):
        
        """
        Establece la conexion con el servidor para crear un registro en la bbdd. 
        """
        try:  
            #Verifica los datos ingresados.
            if Modelo.check_name(name):
                print('Error en ingreso de nombre')
                raise TypeError
            elif Modelo.check_name(lname):
                print('Error en ingreso de apellido')
                raise TypeError
            elif Modelo.check_alphanum(dire):
                print('Error en ingreso de dirección')
                raise TypeError
            elif Modelo.check_alphanum(par):
                print('Error en ingreso de partido')
                raise TypeError
            elif Modelo.check_alphanum(prov):
                print('Error en ingreso de provincia')
                raise TypeError
            elif Modelo.check_num(tel):
                print('Error en ingreso de telefono')
                raise TypeError

            customer =  Cliente()

            #Recopila la información a enviar al servidor.
            customer.data_array.append('crear')
            customer.data_array.append(name)
            customer.data_array.append(lname)
            customer.data_array.append(dire)
            customer.data_array.append(par)
            customer.data_array.append(prov)
            customer.data_array.append(tel)
            customer.data_array.append('end')

            #Establece conexión.
            conexion = customer.conexion_servidor()
  
            #Indica si la conexión fue exitosa.
            if conexion == True:
                return True
            else:
                return False 
        except:
            return False

    def actualizar_registro(self, registro, name, lname, dire, par, prov, tel):
        
        """
        Establece la conexion con el servidor para actualizar un registro en la bbdd.
        """
        try:

            #Verifica los datos ingresados.
            if Modelo.check_name(name):  
                print('Error en ingreso de nombre')
                raise TypeError
            elif Modelo.check_name(lname):
                print('Error en ingreso de apellido')
                raise TypeError
            elif Modelo.check_alphanum(dire):
                print('Error en ingreso de dirección')
                raise TypeError
            elif Modelo.check_alphanum(par):
                print('Error en ingreso de partido')
                raise TypeError
            elif Modelo.check_alphanum(prov):
                print('Error en ingreso de provincia')
                raise TypeError
            elif Modelo.check_num(tel):
                print('Error en ingreso de telefono')
                raise TypeError

            customer =  Cliente()
            #Recopila la información a enviar al servidor.
            customer.data_array.append('actualizar')
            customer.data_array.append(registro)
            customer.data_array.append(name)
            customer.data_array.append(lname)
            customer.data_array.append(dire)
            customer.data_array.append(par)
            customer.data_array.append(prov)
            customer.data_array.append(tel)
            customer.data_array.append('end')
    
            #Establece conexión.
            conexion = customer.conexion_servidor()

            #Indica si la conexión fue exitosa.
            if conexion == True:
                return True
            else:
                return False 
            
        except:
            return False

    def eliminar_registro(self, registro):

        """
        Establece la conexion con el servidor para actualizar un registro en la bbdd.
        """
        try:
            #Recopila la información a enviar al servidor.
            
            customer =  Cliente()

            if customer.get_id(str(registro)) == False:
                raise NoExisteRegistro

            customer.data_array.append('eliminar')
            customer.data_array.append(registro)
            customer.data_array.append('end')

            #Establece conexión        
            conexion = customer.conexion_servidor()
        
            #Indica si la conexión fue exitosa.
            if conexion == True:
                return True
            else:
                return False                                                    
        except:
            return False 
            
    
    def actualiza_tv(self, objeto, QTable_WidgetItem):

        """
        Ejecuta la actualización del treeview de la vista.
        """

        try:
            data_array = list()

            customer = Cliente()

            tv_array = customer.read_bbdd()
    
    
            for i in tv_array:
                i = str(i)
                data_array.append(i.split('|')) 
    
   
            for x in data_array:
        
                position = objeto.rowCount()
                objeto.insertRow(position)
                y = 0

                for n in x:
            
                    if n != 'end':
   
                        objeto.setItem(position, y, QTable_WidgetItem(n))
                        y +=1
    
        except TypeError:
            print('No se pudo actualizar el treeview.')


    def cambia_subscripcion(self, n):
        """
        Activa o desactiva la suscripción. 
        """
        customer =  Cliente()
        
        if n == 'T':
            file = open('subscription.txt', 'w')
            file.write('True')
            file.close()
            customer.cambia_subscripcion('T')

        else:
            file = open('subscription.txt', 'w')
            file.write('False')
            file.close()
            customer.cambia_subscripcion('F')

    
class NoExisteRegistro(Exception):
    
    def __init__(self):
        super().__init__()
        self.mensaje = 'No existe registro'
        self.informacion = 'El registro seleccionado no existe en la base de datos.'
        print(self.mensaje)
        print(self.informacion)