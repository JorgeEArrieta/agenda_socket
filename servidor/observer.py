class ObservadorPrincipal():

    def modificar_suscripcion(self, n):
        
        """
        Modifica el archivo donde se guarda el registro de la suscripción.
        """

        if n == 'T':
            file = open('subscription.txt', 'w')
            file.write('True')
            file.close()
        else:
            file = open('subscription.txt', 'w')
            file.write('False')
            file.close()

    def verificar_suscripcion(self):

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


class Observadores(ObservadorPrincipal):

    def __init__(self):
        self.estado = None

    def set_estado (self, estado):
        self.estado = estado

    def get_estado(self):
        return self.estado

    def send_event(self, mensaje, conexion):

        """
        Envia los eventos al suscriptor.
        """
    
        subscripcion = self.verificar_suscripcion()

        if subscripcion == True:
            
            while True:
                texto = bytearray(mensaje, 'utf-8')
                print(texto)
                conexion.sendall(texto)
                print('termino funcion')
                break