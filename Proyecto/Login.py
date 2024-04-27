import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QLineEdit
from bd.lectura import minimos, log
from tools.tools import *
from tools.menu import setrango
from tools.Espera import Espera

class Login(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setObjectName("Chester")
        # Obtener las dimensiones de la pantalla
        screen_geometry = QDesktopWidget().screenGeometry()
        icono = QIcon("img/POIxtac.png")
        self.setWindowIcon(icono)
        # Configurar la geometría de la ventana para que tenga el tamaño máximo
        self.setGeometry(0, 0, screen_geometry.width(), screen_geometry.height())
        
        # Paleta de colores y estilo de fondo
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(57, 163, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.All, QtGui.QPalette.Background, brush)
        self.setPalette(palette)
        self.setStyleSheet("background-color: rgb(57, 163, 255);")
        
        # Widget central y elementos
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")





        self.TablaMinimos = QtWidgets.QTableWidget(self.centralwidget)
        self.TablaMinimos.setGeometry(QtCore.QRect((screen_geometry.width()//2)-(screen_geometry.width()//8), (screen_geometry.height()//25), ((screen_geometry.width()//4)),(screen_geometry.height()//4)+(screen_geometry.height()//50)))
        self.TablaMinimos.setObjectName("TablaMinimos debajo del promedio")
        self.TablaMinimos.setColumnCount(4)
        self.TablaMinimos.setRowCount(0)
        x=(screen_geometry.width()//4)
        self.TablaMinimos.setStyleSheet("background-color: lightgray;")
        tamaños_filas = [(x//5), (x//2)+(x//24),(x//4)-(x//25), (x//4)-(x//25)]  # Lista de tamaños de fila para cada fila en píxeles
        # Configurar los tamaños de fila
        for fila, tamaño in enumerate(tamaños_filas):
            self.TablaMinimos.setColumnWidth(fila, tamaño)
            
        self.logo=logo(self.centralwidget, screen_geometry.width(), screen_geometry.height())
        
        self.botoninfo=botonInfo(self.centralwidget, screen_geometry.width(),screen_geometry.height())
        self.botoninfo.clicked.connect(Info)
        
        
        self.setCentralWidget(self.centralwidget)
        
        ########################################################################################################################
        self.label = label(self.centralwidget, "Usuario:", screen_geometry.width() // 2-screen_geometry.width() // 20, screen_geometry.height() // 2)
        self.usuario = editarTexto(self.centralwidget, screen_geometry.width()//2+screen_geometry.width()//132, screen_geometry.height() // 2 )
        self.label = label(self.centralwidget, "Contraseña:", screen_geometry.width() // 2-screen_geometry.width() // 13, screen_geometry.height() // 2 + (screen_geometry.height() // 11))
        self.contra = editarTexto(self.centralwidget, screen_geometry.width()//2+screen_geometry.width()//132, screen_geometry.height() // 2 + (screen_geometry.height() // 10))
        self.contra.setEchoMode(QLineEdit.Password)
        self.ingresara = botoningresar(self.centralwidget,screen_geometry.width()//2-screen_geometry.width()//7-screen_geometry.width()//140, screen_geometry.height() // 2 + (screen_geometry.height() // 5))
        self.invitados = invitado(self.centralwidget,screen_geometry.width()//2+screen_geometry.width()//132, screen_geometry.height() // 2+(screen_geometry.height() // 5))
        #################################################################################################
        #                                        ACIONES                                                #
        #################################################################################################
        self.ingresara.clicked.connect(self.ingresar)
        self.invitados.clicked.connect(self.externos)
        #################################################################################################
        

        # Traducción de textos
        self.retranslateUi()
    def ingresar(self):
        user=self.usuario.text()
        passw=self.contra.text()
        a=log(user, passw)
        
        if a=="a":
            Error("Usuario o contraseña equivocado")
        elif a=="b":
            Error("Escribe el usuario y/o contraseña")
        else:
            setrango(a)
            self.new_window = Espera()
            self.new_window.show()
            self.hide()
    def externos(self):
        
        setrango(0)
        self.new_window = Espera()
        self.new_window.show()
        self.hide()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Login", "Login"))
        self.TablaMinimos.setHorizontalHeaderLabels(["Clave", "Nombre", "Medida", "Existencias"])
        minimos(self.TablaMinimos)
        
