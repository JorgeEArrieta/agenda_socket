import socket
import binascii
from observer import Observer

class Cliente():

    DIRECCION = 'localhost'
    PUERTO = 10000
    data_array = list()

    def read_subscription():
        """
        Lee si la suscripción esta activa.
        """
        file = open('subscription.txt', 'r')
        value = file.read()
        file.close()
        if value == 'True':
                return True
        else: 
            return False

    def conexion_servidor(self):

        """
        Crea una conexión para el cliente y envia la información al servidor.
        """
        
        try:

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
            sock.connect((self.DIRECCION, self.PUERTO))

            
            while True:
                print(self.data_array)
                for i in self.data_array:

                    #Envia información al servidor
                    s_data = str(i).encode().hex()
                    b_array = bytearray(s_data,'utf-8')
                    sock.sendall(b_array)
                    print('Información enviada al servidor: ' + binascii.unhexlify(b_array).decode('utf-8'))

                    #Recibe información
                    r_data = binascii.unhexlify(sock.recv(1024)).decode('utf-8')
                    print("Información recibida del servidor: " + r_data)
                
                if Cliente.read_subscription() == True:
                    #Recibe información del servidor.
                    evento = sock.recv(1024).decode('utf-8')
                    print(evento)
                    #Crea suscriptor
                    suscriptor = Observer(evento)
                    suscriptor.update()
                    #Finaliza conexión.
                    mensaje = 'Finalizar'
                    sock.sendall(bytearray(mensaje, 'utf-8'))
                    sock.close() 
                    print('Finalización de la conexión.')
                    self.data_array.clear()
                    break

                else:
                    #Envia el mensaje al servidor para finalizar la comunicación
                    mensaje = 'Finalizar'
                    e_mensaje = mensaje.encode().hex()
                    sock.sendall(bytearray(e_mensaje, 'utf-8'))
                    sock.close() 
                    
                    print('Finalización de la conexión.')
                    self.data_array.clear()
                    break
                    
            return True

        except ConnectionRefusedError:
            print('Sin conexión al servidor.')
            return False

    def read_bbdd(self):

        """
        Solicita al servidor la información que se encuentre en la base de datos para poder
        actualizar el treeview de la vista.
        """
        try:
            tv_array = list()

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
            sock.connect((self.DIRECCION, self.PUERTO))
            informacion_recibida = 0

            while True:
                
                #Envia el mensaje para comenzar la operación.
                mensaje = 'leer'
                s_data = mensaje.encode().hex() 
                data = bytearray(s_data, 'utf-8')

                print("Enviando al servidor: " + binascii.unhexlify(data).decode('utf-8'))
    
                sock.sendall(data)
        
                while True:
            
                    info = binascii.unhexlify(sock.recv(1024)).decode('utf-8').strip()
                    
                    
                    if info == 'Sin datos':
                        print('Sin datos en la bbdd.')
                        break

                    elif info.strip() == '|end|':
                        print('Ingreso')
                        mensaje = 'Finalizar'
                        s_mensaje = mensaje.encode().hex()
                        print('Finalización de la conexión.')
                        print('Datos recibidos: ' + str(informacion_recibida))
                        sock.sendall(bytearray(s_mensaje, 'utf-8'))
                        break

                    else:
                        print('Datos recibidos: ' + info)
                        tv_array.append(info)
                        info = str(info).encode().hex()
                        info = bytearray(info, 'utf-8')
                        sock.sendall(info)

                        informacion_recibida += 1 

                break

            return tv_array

        except ConnectionRefusedError:
            print('Sin conexión al servidor.')

    def get_id(self, registro):

        """
        Envía al servidor una solicitud para verificar que un registro exista en la bbdd. De existir, devuelve true. 
        Caso contrario devuelve False.
        """

        try:
        
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
            sock.connect((self.DIRECCION, self.PUERTO))

            #Envia el mensaje al servidor para que comience con la función 
            message_i = 'Obtener'
            s_data = message_i.encode().hex()
            sock.sendall(bytearray(s_data, 'utf-8'))

            #Recibe la confirmación del servidor.
            r_data = binascii.unhexlify(sock.recv(1024)).decode('utf-8')

            if  r_data == 'Esperando...':
        
                while True:
            
                    #Envia el registro a verificar.
                    message_r = str(registro).encode().hex()
                    sock.sendall(bytearray(message_r, 'utf-8'))

                    #Indica al servidor la finalización de la operación

                    resultado = binascii.unhexlify(sock.recv(1024)).decode('utf-8')

                    #Termina la conexión
                    mensaje = 'Finalizar'
                    mensaje_f = mensaje.encode().hex()
                    sock.sendall(bytearray(mensaje_f, 'utf-8'))
                    print('Finalización de la conexión.')
                    break

            if resultado == 'T':
                return True
            else:
                return False

        except ConnectionRefusedError:
            print('Sin conexión al servidor.')

    def cambia_subscripcion(self, n):

        """
        Notifica al servidor de un cambio en la subscripción.
        """

        try:

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
            sock.connect((self.DIRECCION, self.PUERTO))
        
            message_i = 'subscripcion'
            message_i =  message_i.encode().hex()
            sock.sendall(bytearray(message_i, 'utf-8'))

            message_r = binascii.unhexlify(sock.recv(1024)).decode('utf-8')
            
            if message_r == 'Esperando...':
        
                while True:
                    #Envia información al servidor.
                    n = str(n).encode().hex()
                    data = bytearray(n, 'utf-8')
                    sock.sendall(data)

                    #Indica al servidor la finalización de la operación
                    print(binascii.unhexlify(sock.recv(1024)).decode('utf-8'))
                    
                    #Termina la conexión
                    mensaje_f = 'Finalizar'
                    mensaje_f = mensaje_f.encode().hex()
                    sock.sendall(bytearray(mensaje_f, 'utf-8'))
                    print('Finalización de la conexión.')
                    break

        except ConnectionRefusedError:
            print('Sin conexión al servidor.')


