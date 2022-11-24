import socket
import bbdd
import binascii
from observer import Observadores


def crea_registro():
    """
    Llama a la función del modulo # para crear un registro en la base de datos.
    """

    bbdd.nuevo_registro(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5])
    
    lista.clear()


def  actualiza_registro():
    """
    Llama a la función del modulo # para actualizar un registro en la base de datos.
    """

    bbdd.act_registro(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6])
    
    lista.clear()


def elimina_registro():
    
    """
    Llama a la función del modulo # para eliminar un registro en la base de datos.
    """
    
    bbdd.del_registro(lista[0])
    
    lista.clear()


def info_treeview():
    """
    Llama a la función del modulo # para enviar los datos que contiene la bbdd.
    """

    lista.clear()
    
    return bbdd.lectura_bbdd()


#Servidor.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

direccion_local = ('localhost', 10000)

sock.bind(direccion_local)

sock.listen(1)

#Creo una lista que va a guardar la información del cliente.
lista = list()

try:

    while True:

        print('Esperando conexión...')

        connection, client_adress = sock.accept()

        print('Conexión desde: ' + client_adress[0])

        while True:

            informacion = binascii.unhexlify(connection.recv(1024)).decode('utf-8')

            print('Información recibida: ' + informacion)

            if informacion == 'crear':
                #Envia información a cliente.
                mensaje = 'Ejecutando acción'
                mensaje = mensaje.encode().hex()
                data = bytearray(mensaje, 'utf-8')
                
                connection.sendall(data)
                
                print('Información enviada : ' + binascii.unhexlify(data).decode('utf-8'))
                
                while True:

                    #Recepción de información.
                    incoming = binascii.unhexlify(connection.recv(1024)).decode('utf-8')
                    lista.append(incoming)
                    print('Información recibida: ' + incoming)

                    #Envio de información
                    s_mensaje = 'Recibido'
                    s_mensaje = s_mensaje.encode().hex()
                    data = bytearray(s_mensaje, 'utf-8')
                    connection.sendall(data)
                    print('Información enviada : ' + binascii.unhexlify(data).decode('utf-8'))
                        
                    if incoming == 'end':
                        observador = Observadores()
                        if observador.verificar_suscripcion() == True:
                            observador.set_estado('Alta')                            
                            observador.send_event(observador.estado, connection)
                            break
                        else:
                            break
            
                crea_registro()
        
            elif informacion == 'actualizar':
                mensaje = 'Ejecutando acción'
                mensaje =  mensaje.encode().hex()
                data = bytearray(mensaje, 'utf-8')
                connection.sendall(data)
                print('Información enviada : ' + binascii.unhexlify(data).decode('utf-8'))
                
                while True:
                    #Recepción de información.
                    incoming = binascii.unhexlify(connection.recv(1024)).decode('utf-8')
                    lista.append(incoming)
                    print('Información recibida: ' + incoming)

                    s_mensaje = 'Recibido.'
                    s_mensaje = s_mensaje.encode().hex()
                    data = bytearray(s_mensaje, 'utf-8')
                    connection.sendall(data)
                    print('Información enviada : ' + binascii.unhexlify(data).decode('utf-8'))
            
                    if incoming == 'end':
                        observador = Observadores()

                        if observador.verificar_suscripcion() == True:
                            observador.set_estado('Modificación')
                            observador.send_event(observador.estado, connection)
                            break
                        else:
                            break
                    
                
                print(lista)
                actualiza_registro()
        
            elif informacion == 'eliminar':
                s_mensaje = 'Ejecutando acción'
                s_mensaje = s_mensaje.encode().hex()
                data = bytearray(s_mensaje, 'utf-8')
                connection.sendall(data)
                print('Información enviada : ' + binascii.unhexlify(data).decode('utf-8'))
                
                while True:

                    #Recepción de información.
                    incoming = binascii.unhexlify(connection.recv(1024)).decode('utf-8')
                    lista.append(incoming)
                    print('Información recibida: ' + incoming)

                    #Envio de confirmación.
                    mensaje = 'Recibido'
                    mensaje = mensaje.encode().hex()
                    data = bytearray(mensaje, 'utf-8')
                    connection.sendall(data)
                    print('Información enviada : ' + binascii.unhexlify(data).decode('utf-8'))
                    
                    #Fin del registro.
                    if incoming == 'end':
                        observador = Observadores()
                        if observador.verificar_suscripcion() == True:
                            observador.set_estado('Baja')
                            observador.send_event(observador.estado, connection)
                            break   
                        else:
                            break            
                    

                elimina_registro()
        
            elif informacion == 'leer':
                
                try:
                    listado = info_treeview()

                    while True:

                        for i in listado:
                            #Envio de información
                            s_data = str(i).encode().hex()
                            data = bytearray(s_data, 'utf-8')
                            connection.sendall(data)
                            print('Información enviada : ' + binascii.unhexlify(data).decode('utf-8'))

                            #Recepción de información.
                            incoming = binascii.unhexlify(connection.recv(1024)).decode('utf-8')
                            print('Información recibida: ' + incoming)
                        break

                except TypeError:
                    s_mensaje = 'Sin datos'
                    s_mensaje = s_mensaje.encode().hex()
                    data = bytearray(s_mensaje, 'utf-8')
                    connection.sendall(data)

            elif informacion == 'Obtener':
                
                print('Ejecutando acción...')
                s_mensaje = 'Esperando...'
                s_mensaje = s_mensaje.encode().hex()
                connection.sendall(bytearray(s_mensaje,'utf-8'))
                
                while True:
                    
                    reg = binascii.unhexlify(connection.recv(1024)).decode('utf-8')
                    print(reg)
                    result = str(bbdd.check_id(reg)).encode().hex()
                    connection.sendall(bytearray(result,'utf-8'))
                    break

            elif informacion == 'subscripcion':

                observador = Observadores()

                s_mensaje = 'Esperando...'
                s_mensaje = s_mensaje.encode().hex()
                connection.sendall(bytearray(s_mensaje,'utf-8'))
                
                while True:
                    #Recibe la información y cambia el estado de la subscripción   
                    data = binascii.unhexlify(connection.recv(1024)).decode('utf-8')
                    observador.modificar_suscripcion(data)

                    #Envia confirmación de la operación al cliente.
                    s_mensaje = 'Listo'
                    s_mensaje = s_mensaje.encode().hex()
                    connection.sendall(bytearray(s_mensaje, 'utf-8'))
                    break

            if informacion != 'Finalizar':
                print('Cerrando conexión con el cliente.')
                break
            
            else:
                print('Finalización de la conexión.')    
                break

except:
    print('Error en conexión con el cliente.')