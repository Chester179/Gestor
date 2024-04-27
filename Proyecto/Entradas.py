import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
from tools.tools import *
from bd.agregar import anadir_datos
from tools.menu import menu

class Entradas(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setObjectName("Chester")
        # Obtener las dimensiones de la pantalla
        screen_geometry = QDesktopWidget().screenGeometry()

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
        self.titulo=Titulo(self.centralwidget,"Entradas de consumibles",screen_geometry.width(),screen_geometry.height())
        # Label
        self.label = label(self.centralwidget, "Clave de consumible:", screen_geometry.width()//2-190, (screen_geometry.height() // 4)+(screen_geometry.height() // 24))
        self.Clave = editarTexto(self.centralwidget, screen_geometry.width() // 2, (screen_geometry.height() // 4)+(screen_geometry.height() // 24))
        self.label = label(self.centralwidget, "Proveedor:", screen_geometry.width()//2-100,(screen_geometry.height() // 3)+(screen_geometry.height() // 100))
        self.Provedor = editarTexto(self.centralwidget, screen_geometry.width() // 2, ((screen_geometry.height() // 3)+(screen_geometry.height() // 100)))
        self.label = label(self.centralwidget, "Cantidad ingresada:", screen_geometry.width()//2-180, (screen_geometry.height() // 2)-(screen_geometry.height() // 9)+(screen_geometry.height() // 160))
        self.Ingreso = editarTexto(self.centralwidget, screen_geometry.width() // 2, (screen_geometry.height() // 2)-(screen_geometry.height() // 9)+(screen_geometry.height() // 160))
        self.label = label(self.centralwidget, "No. de folio:", screen_geometry.width()//2-110, (screen_geometry.height() // 2)-(screen_geometry.height() // 19))
        self.Folio = editarTexto(self.centralwidget, screen_geometry.width() // 2, (screen_geometry.height() // 2)-(screen_geometry.height() // 19))
        self.label = label(self.centralwidget, "Pedido PO:", screen_geometry.width()//2-105, (screen_geometry.height() // 2))
        self.PedidoPO = editarTexto(self.centralwidget, screen_geometry.width() // 2, (screen_geometry.height() // 2))
        self.PedidoPO.setText("Sin OC")

        self.boton=boton(self.centralwidget,(screen_geometry.width()//2)-100,(screen_geometry.height())-((screen_geometry.height()//5)-(screen_geometry.height()//55)))
        self.boton.clicked.connect(self.ingresos)

        self.logo=logo(self.centralwidget, screen_geometry.width(), screen_geometry.height())
        
        self.botoninfo=botonInfo(self.centralwidget, screen_geometry.width(),screen_geometry.height())
        self.botoninfo.clicked.connect(Info)

        self.setCentralWidget(self.centralwidget)

        # Barra de menú y submenús
        menu(self,"Entradas de consumibles")
    # Método para abrir una nueva ventana
   

    #Enviar datos a la base de datos
    def ingresos(self):
    # Obtener el texto ingresado en los widgets de la interfaz de usuario
        proveedor = self.Provedor.text()
        ingreso = self.Ingreso.text()
        clave=self.Clave.text()
        Pedido=self.PedidoPO.text()
        Folio=self.Folio.text()
        #Manda los datos a la base de datos
        anadir_datos(clave,proveedor,ingreso, Pedido, Folio)
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Entradas()
    window.showMaximized()

    sys.exit(app.exec_())
