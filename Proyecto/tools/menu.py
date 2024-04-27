from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon, QFont
def setrango(rango):
       global x
       x=rango
def getrango():
        return x
       
#############################################################################################
def menu(self,titulo):                                                                      #
        self.menubar = QtWidgets.QMenuBar(self)                                                 #
        #self.menubar.setGeometry(QtCore.QRect(0, 0, 1813, 0))     
        self.menubar.setFixedHeight(30)                             #
        self.menubar.setStyleSheet("QMenuBar { background-color: #000000; color: #FFFFFF; font-size: 18px; }"
                                        "QMenuBar::item { background-color: #000000; }"
                                        "QMenuBar::item:selected { background-color: #66CDAA; color: #FFFFFF; font-size: 18px; }"
                                        "QMenu { background-color: white; }"
                                        "QMenu::item:selected { background-color: #66CDAA; color: #000000; }")
                

        
        self.menubar.setObjectName("menubar")                                                   #
        self.menuBuscar = QtWidgets.QMenu(self.menubar)                                         #
        self.menuBuscar.setObjectName("menuBuscar")                                             #
        self.menuEntrada = QtWidgets.QMenu(self.menubar)                                        #
        self.menuEntrada.setObjectName("menuEntrada")                                           #
        self.menuHistorial = QtWidgets.QMenu(self.menubar)                                      #
        self.menuHistorial.setObjectName("menuHistorial")
        self.menuUsuarios = QtWidgets.QMenu(self.menubar)                                       #
        self.menuUsuarios.setObjectName("menuUsuario")
        self.menuExtras = QtWidgets.QMenu(self.menubar)                                         #
        self.menuExtras.setObjectName("menuExtras")                                             #
        self.menuSalida = QtWidgets.QMenu(self.menubar)                                         #
        self.menuSalida.setObjectName("menuSalida")  
        self.setMenuBar(self.menubar)                                                           #

        # Barra de estado
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        # Acciones
        self.menubar.addAction(self.menuBuscar.menuAction())
        self.menubar.addAction(self.menuEntrada.menuAction())
        self.menubar.addAction(self.menuHistorial.menuAction())
        self.menubar.addAction(self.menuUsuarios.menuAction())
        self.menubar.addAction(self.menuExtras.menuAction())
        self.menubar.addAction(self.menuSalida.menuAction())


        self.setWindowTitle(titulo)
        icono = QIcon("img/prue.jpg")
        self.setWindowIcon(icono)
        self.menuBuscar.setTitle("Buscar herramienta")
        self.menuEntrada.setTitle("Movimiento de consumible")
        self.menuHistorial.setTitle("Historial")
        self.menuUsuarios.setTitle("Usuarios")
        self.menuExtras.setTitle("Otros")
        self.menuSalida.setTitle("Salir")
        
        

        # Conexiones de señales y slots
        QtCore.QMetaObject.connectSlotsByName(self)
        
        # Establecer hoja de estilo para las acciones del menú
        

        # Aplicar el estilo a cada acción del menú
        self.actionBuscar = QtWidgets.QAction("Buscar consumible", self)
        self.menuBuscar.addAction(self.actionBuscar)

        self.actionEntrada = QtWidgets.QAction("Entradas de consumibles", self)
        self.menuEntrada.addAction(self.actionEntrada)

        self.actionSalida = QtWidgets.QAction("Salidas de consumibles", self)
        self.menuEntrada.addAction(self.actionSalida)

        self.actionHistorial = QtWidgets.QAction("Historial de vales", self)
        self.menuHistorial.addAction(self.actionHistorial)

        self.actionHistorialAcc = QtWidgets.QAction("Historial de acciones", self)
        self.menuHistorial.addAction(self.actionHistorialAcc)

        self.actionUsuarios = QtWidgets.QAction("Usuarios de almacén", self)
        self.menuUsuarios.addAction(self.actionUsuarios)

        self.actionExtras = QtWidgets.QAction("Añadir consumible", self)
        self.menuExtras.addAction(self.actionExtras)

        self.actionModificar = QtWidgets.QAction("Modificar consumible",self)
        self.menuExtras.addAction(self.actionModificar)

        self.actionEliminar = QtWidgets.QAction("Eliminar consumible", self)
        self.menuExtras.addAction(self.actionEliminar)

        self.actionSalir = QtWidgets.QAction("Salir", self)
        self.menuSalida.addAction(self.actionSalir)


        menu_actions = [self.actionBuscar, self.actionEntrada, self.actionSalida, 
                self.actionHistorial, self.actionUsuarios, self.actionExtras,
                self.actionModificar, self.actionEliminar, self.actionSalir, self.actionHistorialAcc]

        if titulo!="Eliminar consumibles":
                for action in menu_actions:
                        action.setFont(QFont("Arial", 16))

        
        if x==0:
                self.actionBuscar.setVisible(True)
                self.actionEntrada.setVisible(False)
                self.actionSalida.setVisible(True)
                self.actionHistorial.setVisible(False)
                self.actionExtras.setVisible(False)
                self.menuHistorial.menuAction().setVisible(False)
                self.menuExtras.menuAction().setVisible(False)
                self.actionSalir.setVisible(True)
                self.actionModificar.setVisible(False)
                self.actionEliminar.setVisible(False)
                self.menuUsuarios.menuAction().setVisible(False)
                self.actionHistorialAcc.setVisible(False)

        elif x==2:
                self.actionEliminar.setVisible(False)
                self.menuUsuarios.menuAction().setVisible(False)

                #Solo no eliminar
        elif x==3:
                self.actionEliminar.setVisible(False)
                self.actionModificar.setVisible(False)
                self.menuUsuarios.menuAction().setVisible(False)
                #No modificar, eliminar
        elif x==1:
                0
        # Conectar la acción a la función irEntrada()
        self.actionBuscar.triggered.connect(lambda: irBuscador(self))
        self.actionEntrada.triggered.connect(lambda: irEntrada(self))
        self.actionSalida.triggered.connect(lambda: irSalidas(self))
        self.actionHistorial.triggered.connect(lambda: irHistorial(self))
        self.actionHistorialAcc.triggered.connect(lambda: irHistorialAcc(self))
        self.actionUsuarios.triggered.connect(lambda: irUsuarios(self))
        self.actionExtras.triggered.connect(lambda: irExtras(self))
        self.actionModificar.triggered.connect(lambda: irModificar(self))
        self.actionEliminar.triggered.connect(lambda: irEliminar(self))
        self.actionSalir.triggered.connect(lambda: Salir(self))
        #############################################################################################
def irBuscador(self):
        from Buscador import Buscador
        self.new_window = Buscador()
        self.new_window.showMaximized()
        self.hide()

def irEntrada(self):
        from Entradas import Entradas
        self.new_window = Entradas()  # Crea una nueva instancia de la clase Entradas
        self.new_window.showMaximized()  # Muestra la nueva ventana
        self.hide()  # Oculta la ventana principal

def irUsuarios(self):
        from Usuarios import Usuarios
        self.new_window = Usuarios()
        self.new_window.showMaximized()
        self.hide()
def irSalidas(self):
        from Salidas import Salidas
        self.new_window = Salidas()
        self.new_window.showMaximized()
        self.hide()

def irHistorial(self):
        from Historial import Historial
        self.new_window = Historial()
        self.new_window.showMaximized()
        self.hide()
def irHistorialAcc(self):
        from Historialacciones import Historialacciones
        self.new_window = Historialacciones()
        self.new_window.showMaximized()
        self.hide()
def irExtras(self):
        from Agregar import Agregar
        self.new_window = Agregar()
        self.new_window.showMaximized()
        self.hide()
def irModificar(self):
        from Modificar import Modificar
        self.new_window = Modificar()
        self.new_window.showMaximized()
        self.hide()
def irEliminar(self):
        from Eliminar import Eliminar
        self.new_window = Eliminar()
        self.new_window.showMaximized()
        self.hide()
def Salir(self):
       from Login import Login
       self.new_window = Login()
       self.new_window.showMaximized()
       self.hide()