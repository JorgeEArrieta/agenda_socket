from PyQt5 import QtCore 
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QFileDialog
from sys import argv
from sys import exit
from modelo import Modelo
from modelo import NoExisteRegistro


class MainWindow():
    
    def __init__(self):
        
        self.identificador = None

        app = QApplication(argv)
        MainWindow = QMainWindow()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(586, 454)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tv_agenda = QTableWidget(self.centralwidget)
        self.tv_agenda.setGeometry(QtCore.QRect(10, 10, 571, 192))
        self.tv_agenda.setObjectName("tv_agenda")
        self.tv_agenda.setColumnCount(7)
        self.tv_agenda.setRowCount(0)
        self.tv_agenda.itemClicked.connect(self.carga_informacion)
        item = QTableWidgetItem()
        self.tv_agenda.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tv_agenda.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.tv_agenda.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.tv_agenda.setHorizontalHeaderItem(3, item)
        item = QTableWidgetItem()
        self.tv_agenda.setHorizontalHeaderItem(4, item)
        item = QTableWidgetItem()
        self.tv_agenda.setHorizontalHeaderItem(5, item)
        item = QTableWidgetItem()
        self.tv_agenda.setHorizontalHeaderItem(6, item)
        self.tv_agenda.setFrameShape(QFrame.HLine)
        self.tv_agenda.setEditTriggers(QAbstractItemView.SelectedClicked)
        self.lbl_0 = QLabel(self.centralwidget)
        self.lbl_0.setGeometry(QtCore.QRect(10, 220, 47, 13))
        self.lbl_0.setObjectName("lbl_0")
        self.lbl_1 = QLabel(self.centralwidget)
        self.lbl_1.setGeometry(QtCore.QRect(300, 220, 47, 13))
        self.lbl_1.setObjectName("lbl_1")
        self.lbl_2 = QLabel(self.centralwidget)
        self.lbl_2.setGeometry(QtCore.QRect(10, 270, 47, 13))
        self.lbl_2.setObjectName("lbl_2")
        self.lbl_3 = QLabel(self.centralwidget)
        self.lbl_3.setGeometry(QtCore.QRect(300, 270, 47, 13))
        self.lbl_3.setObjectName("lbl_3")
        self.lbl_4 = QLabel(self.centralwidget)
        self.lbl_4.setGeometry(QtCore.QRect(10, 320, 47, 13))
        self.lbl_4.setObjectName("lbl_4")
        self.lbl_5 = QLabel(self.centralwidget)
        self.lbl_5.setGeometry(QtCore.QRect(300, 320, 47, 13))
        self.lbl_5.setObjectName("lbl_5")
        self.btn_generar = QPushButton(self.centralwidget, clicked=self.crear_registro)
        self.btn_generar.setGeometry(QtCore.QRect(500, 380, 75, 23))
        self.btn_generar.setObjectName("btn_generar")
        self.btn_modificar = QPushButton(self.centralwidget, clicked=self.actualiza_registro)
        self.btn_modificar.setGeometry(QtCore.QRect(410, 380, 75, 23))
        self.btn_modificar.setObjectName("btn_modificar")
        self.btn_eliminar = QPushButton(self.centralwidget, clicked = self.form_elimina)
        self.btn_eliminar.setGeometry(QtCore.QRect(320, 380, 75, 23))
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.btn_limpiar = QPushButton(self.centralwidget, clicked=self.limpiar_qlineedit)
        self.btn_limpiar.setGeometry(QtCore.QRect(230, 380, 75, 23))
        self.btn_limpiar.setObjectName("btn_limpiar")
        self.btn_logo = QPushButton(self.centralwidget, clicked=self.frm_logo_create)
        self.btn_logo.setObjectName(u"btn_logo")
        self.btn_logo.setGeometry(QtCore.QRect(140, 380, 75, 23))
        self.txt_name = QLineEdit(self.centralwidget)
        self.txt_name.setGeometry(QtCore.QRect(10, 240, 251, 20))
        self.txt_name.setObjectName("txt_name")
        self.txt_lname = QLineEdit(self.centralwidget)
        self.txt_lname.setGeometry(QtCore.QRect(300, 240, 251, 20))
        self.txt_lname.setObjectName("txt_lname")
        self.txt_direccion = QLineEdit(self.centralwidget)
        self.txt_direccion.setGeometry(QtCore.QRect(10, 290, 251, 20))
        self.txt_direccion.setObjectName("txt_direccion")
        self.txt_partido = QLineEdit(self.centralwidget)
        self.txt_partido.setGeometry(QtCore.QRect(300, 290, 251, 20))
        self.txt_partido.setObjectName("txt_partido")
        self.txt_provincia = QLineEdit(self.centralwidget)
        self.txt_provincia.setGeometry(QtCore.QRect(10, 340, 251, 20))
        self.txt_provincia.setObjectName("txt_direccion_2")
        self.txt_telefono = QLineEdit(self.centralwidget)
        self.txt_telefono.setGeometry(QtCore.QRect(300, 340, 251, 20))
        self.txt_telefono.setObjectName("txt_direccion_3")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 586, 21))
        self.menubar.setObjectName("menubar")
        self.mnu_archivo = QMenu(self.menubar)
        self.mnu_archivo.setObjectName("mnu_archivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.mnu_salir = QAction(MainWindow)
        self.mnu_salir.setObjectName("mnu_salir")
        self.mnu_salir.triggered.connect(lambda: app.quit())
        self.mnu_archivo.addAction(self.mnu_salir)
        self.menubar.addAction(self.mnu_archivo.menuAction())

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tv_agenda.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.tv_agenda.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tv_agenda.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Apellido"))
        item = self.tv_agenda.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Dirección"))
        item = self.tv_agenda.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Partido"))
        item = self.tv_agenda.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Provincia"))
        item = self.tv_agenda.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Teléfono"))
        self.lbl_0.setText(_translate("MainWindow", "Nombre:"))
        self.lbl_1.setText(_translate("MainWindow", "Apellido"))
        self.lbl_2.setText(_translate("MainWindow", "Dirección:"))
        self.lbl_3.setText(_translate("MainWindow", "Partido:"))
        self.lbl_4.setText(_translate("MainWindow", "Provincia:"))
        self.lbl_5.setText(_translate("MainWindow", "Teléfono:"))
        self.btn_generar.setText(_translate("MainWindow", "Crear"))
        self.btn_modificar.setText(_translate("MainWindow", "Modificar"))
        self.btn_eliminar.setText(_translate("MainWindow", "Eliminar"))
        self.btn_limpiar.setText(_translate("MainWindow", "Limpiar"))
        self.btn_logo.setText(_translate("MainWindow", "Eventos"))
        self.mnu_archivo.setTitle(_translate("MainWindow", "Archivo"))
        self.mnu_salir.setText(_translate("MainWindow", "Salir"))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actualiza_treeview()

        MainWindow.show()
        exit(app.exec_())


    def actualiza_treeview(self):
        
        """
        Limpia los datos del widget QTableWidget y actualiza la información.
        """
        obj = Modelo()

        cant_columnas = self.tv_agenda.rowCount()
            
        for i in range (0, cant_columnas):
            self.tv_agenda.removeRow(0)
            cant_columnas = self.tv_agenda.rowCount()

        obj.actualiza_tv(self.tv_agenda, QTableWidgetItem)

    
    def obtener_id(self):
        
        """
        Obtiene el id de los registros.
        """
        try:
            columna = self.tv_agenda.currentRow()
            self.identificador = self.tv_agenda.item(columna, 0).text()
            return int(self.identificador)
        
        except:

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Falta seleccionar un registro.")
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            #msg_box.buttonClicked.connect(msgButtonClick)
            msg_box.exec()



    def limpiar_qlineedit(self):
        """
        Limpia la información contenida en los QLineEdit.
        """
        self.identificador = None
        self.txt_name.clear()
        self.txt_lname.clear()
        self.txt_direccion.clear()
        self.txt_partido.clear()
        self.txt_provincia.clear()
        self.txt_telefono.clear()
    
    
    def carga_informacion(self):
        
        """
        Obtiene los datos del registro seleccionado, en el widget QTableWidget, y carga la información
        en los QLineEdit correspondientes.
        """
        try:
            columna = self.tv_agenda.currentRow()
            self.identificador = self.tv_agenda.item(columna, 0).text()
            #Campo nombre
            self.txt_name.clear()
            r0 = self.identificador = self.tv_agenda.item(columna, 1).text()
            self.txt_name.insert(r0)
            #Campo Apellido
            self.txt_lname.clear()
            r1 = self.identificador = self.tv_agenda.item(columna, 2).text()
            self.txt_lname.insert(r1)
            #Campo Dirección
            self.txt_direccion.clear()
            r3 = self.identificador = self.tv_agenda.item(columna, 3).text()
            self.txt_direccion.insert(r3)
            #Campo Partido
            self.txt_partido.clear()
            r4 = self.identificador = self.tv_agenda.item(columna, 4).text()
            self.txt_partido.insert(r4)
            #Campo Provincia
            self.txt_provincia.clear()
            r5 = self.identificador = self.tv_agenda.item(columna, 5).text()
            self.txt_provincia.insert(r5)
            #Campo Teléfono
            self.txt_telefono.clear()
            r6 = self.identificador = self.tv_agenda.item(columna, 6).text()
            self.txt_telefono.insert(r6)
    
        except AttributeError:
            pass

    def crear_registro(self):
        
        """
        Obtiene la información de los widgets QLineEdit y llama a la función crear_registro del modulo "modelo".
        Si el resultado de la función es correcto, envia un mensaje al usuario mediante un QMessageBox.
        """

        try:

            #Crea objeto Modelo
            obj = Modelo() 
            #Obtiene la información 
            name = str(self.txt_name.text())
            lname = str(self.txt_lname.text())
            direccion = str(self.txt_direccion.text())
            partido = str(self.txt_partido.text())
            provincia = str(self.txt_provincia.text())
            telefono = str(self.txt_telefono.text())
        
            if len(name) == 0:
                raise TypeError
            elif len(lname) == 0:
                raise TypeError
            elif len(direccion) == 0:
                raise TypeError
            elif len(partido) == 0:
                raise TypeError
            elif len(provincia) == 0:
                raise TypeError
            elif len(telefono) == 0:
                raise TypeError

            #Crea la base de datos.
            resultado = obj.crear_registro(name, lname, direccion, partido, provincia, telefono)

            #Actualiza el treeview.
            self.actualiza_treeview()
            self.limpiar_qlineedit()

            #Notifica al usuario que la operación fue exitosa.
            if resultado == True:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Se creo la base de datos correctamente")
                msg_box.setWindowTitle("Información")
                msg_box.setStandardButtons(QMessageBox.Ok)
                #msg_box.buttonClicked.connect(msgButtonClick)
                msg_box.exec()

            else:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Sin conexión al servidor.")
                msg_box.setWindowTitle("Error")
                msg_box.setStandardButtons(QMessageBox.Ok)
                #msg_box.buttonClicked.connect(msgButtonClick)
                msg_box.exec()


        
        except TypeError:
            #Notifica al usuario que existe un error en los datos.
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Falta completar un dato obligatorio o se introdujo un dato erroneo.")
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            #msg_box.buttonClicked.connect(msgButtonClick)
            msg_box.exec()
        

    def actualiza_registro(self):

        """
        Obtiene los datos para actualizar un registro seleccionado y llama a la función para 
        realizar el procedimiento.
        """
        obj = Modelo()
        
        try:

            #Verifica que se haya seleccionado un registro.
            if self.identificador == None:
                raise NoExisteRegistro
            
            #Obtiene la información 
            name = self.txt_name.text()
            lname = self.txt_lname.text()
            direccion = self.txt_direccion.text()
            partido = self.txt_partido.text()
            provincia = self.txt_provincia.text()
            telefono = str(self.txt_telefono.text())
            identificador = str(self.obtener_id())

            #Verifica los datos ingresados.
            if len(name) == 0:
                raise TypeError
            elif len(lname) == 0:
                raise TypeError
            elif len(direccion) == 0:
                raise TypeError
            elif len(partido) == 0:
                raise TypeError
            elif len(provincia) == 0:
                raise TypeError
            elif len(telefono) == 0:
                raise TypeError

            #Llama a la función para actualizar el registro.    
            resultado = obj.actualizar_registro(identificador, name, lname, 
                                                   direccion, partido, provincia, telefono)
            #Actualiza el treeview
            self.actualiza_treeview()
            
            #Notifica al usuario que la operación fue realizada exitosamente.
            if resultado == True:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Se actualizo el registro correctamente")
                msg_box.setWindowTitle("Información")
                msg_box.setStandardButtons(QMessageBox.Ok)
                #msg_box.buttonClicked.connect(msgButtonClick)
                msg_box.exec()
                self.actualiza_treeview()
                self.limpiar_qlineedit()

            else:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Sin conexión al servidor.")
                msg_box.setWindowTitle("Error")
                msg_box.setStandardButtons(QMessageBox.Ok)
                #msg_box.buttonClicked.connect(msgButtonClick)
                msg_box.exec()
    
        except TypeError:

            #Notifica al usuario que existe un error en los datos.
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Se introdujo un tipo de dato erroneo.")
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            #msg_box.buttonClicked.connect(msgButtonClick)
            msg_box.exec()

        except NoExisteRegistro:

            #Notifica al usuario que existe un error en los datos.
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Falta seleccionar un registro.")
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            #msg_box.buttonClicked.connect(msgButtonClick)
            msg_box.exec()

    
    def form_elimina(self):
        
        """
        Crea el formulario para eliminar registros de la base de datos.
        """
        self.frm_elimina = QDialog()
        self.frm_elimina.setObjectName("frm_elimina")
        self.frm_elimina.resize(257, 76)
        self.lb_0 = QLabel(self.frm_elimina)
        self.lb_0.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.lb_0.setObjectName("lb_0")
        self.txt_idregistro = QLineEdit(self.frm_elimina)
        self.txt_idregistro.setGeometry(QtCore.QRect(70, 10, 171, 20))
        self.txt_idregistro.setObjectName("lineEdit")
        self.btn_eliminar = QPushButton(self.frm_elimina, clicked=self.elimina_registro)
        self.btn_eliminar.setGeometry(QtCore.QRect(170, 40, 75, 23))
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.btn_cerrar = QPushButton(self.frm_elimina, clicked=self.frm_elimina.close)
        self.btn_cerrar.setGeometry(QtCore.QRect(80, 40, 75, 23))
        self.btn_cerrar.setObjectName("btn_cerrar")
        _translate = QtCore.QCoreApplication.translate
        self.frm_elimina.setWindowTitle(_translate("frm_elimina", "Elimina registro"))
        self.lb_0.setText(_translate("frm_elimina", "Id registro:"))
        self.btn_eliminar.setText(_translate("frm_elimina", "Eliminar"))
        self.btn_cerrar.setText(_translate("frm_elimina", "Cerrar"))    
        QtCore.QMetaObject.connectSlotsByName(self.frm_elimina)
    
        self.frm_elimina.exec_()
    
    def elimina_registro(self):
    
        """
        Llama a la función del modúlo "modelo" para eliminar un registro.
        """
        try: 
            var = self.txt_idregistro.text()
        
            obj = Modelo()
        
            result = obj.eliminar_registro(var)
        
            if result == True:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Se elimino el registro correctamente")
                msg_box.setWindowTitle("Información")
                msg_box.setStandardButtons(QMessageBox.Ok)
                #msg_box.buttonClicked.connect(msgButtonClick)
                msg_box.exec()
                self.actualiza_treeview()
                self.limpiar_qlineedit()
                self.frm_elimina.close()
        
            else:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Sin conexión al servidor.")
                msg_box.setWindowTitle("Error")
                msg_box.setStandardButtons(QMessageBox.Ok)
                #msg_box.buttonClicked.connect(msgButtonClick)
                msg_box.exec()
          
        except:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("No se encuentra el registro ingresado.")
            msg_box.setWindowTitle("Información")
            msg_box.setStandardButtons(QMessageBox.Ok)
            #msg_box.buttonClicked.connect(msgButtonClick)
            msg_box.exec()
            self.actualiza_treeview()
            self.frm_elimina.close()

    def frm_logo_create(self):

        """
        Crea el formulario para que el usuario indique si quiere crear un log de eventos.
        """
        
        self.frm_log = QDialog()
        self.frm_log.setObjectName("frm_log")
        self.frm_log.resize(396, 82)
        self.btn_aceptar = QPushButton(self.frm_log, clicked=self.cambia_subscripcion)
        self.btn_aceptar.setGeometry(QtCore.QRect(40, 40, 341, 32))
        self.btn_aceptar.setObjectName("buttonBox")
        self.chk_subscripcion = QCheckBox(self.frm_log)
        self.chk_subscripcion.setGeometry(QtCore.QRect(20, 10, 131, 17))
        self.chk_subscripcion.setObjectName("chk_subscripcion")

        #Verifica el estado de la subscripción para actualizar el checkbox
        
        _translate = QtCore.QCoreApplication.translate
        self.frm_log.setWindowTitle(_translate("frm_log", "Logo de eventos"))
        self.btn_aceptar.setText(_translate("frm_log", "Aceptar"))
        self.chk_subscripcion.setText(_translate("frm_log", "Genera log de evento"))
        #self.buttonBox.accepted.connect(self.frm_log.accept)
        QtCore.QMetaObject.connectSlotsByName(self.frm_log)

        self.estado_subscripcion()
        self.frm_log.exec_()

   
    def estado_subscripcion(self):
        
        """
        Verifica el estado de la subscripción para actualizar el checkbox
        
        """
        suscripcion = open('subscription.txt', 'r')

        if suscripcion.read() == 'True':
            self.chk_subscripcion.setChecked(True)
        else:
            self.chk_subscripcion.setChecked(False)
        
    def cambia_subscripcion(self):

        """
        Corre el proceso para cambiar el valor de la subscripción.
        """
        modelo = Modelo() 
        if self.chk_subscripcion.isChecked() == True:
            print('Actualizo el checkbox a true')
            modelo.cambia_subscripcion('T')
        elif self.chk_subscripcion.isChecked() == False:
            print('Actualizo el checkbox a false')
            modelo.cambia_subscripcion('F')

        self.frm_log.close()