import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QMessageBox
from tools.tools import *
from bd.Eliminar import eliminar_datos
from tools.menu import menu

class Eliminar(QMainWindow):
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
        self.setStyleSheet("background-color: rgb(100, 0, 0);")

        # Widget central y elementos
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.titulo=Titulo(self.centralwidget,"Eliminar consumibles",screen_geometry.width(),screen_geometry.height())
        # Label
        self.label_nombre = QtWidgets.QLabel(self.centralwidget)
        self.label_nombre.setGeometry(QtCore.QRect(screen_geometry.width()//2-250,(screen_geometry.height() // 3)+(screen_geometry.height() // 100), 300, 30))
        self.label_nombre.setText("Clave consumible:")    
        self.label_nombre.setStyleSheet("color: white; font-family: Arial; font-size: 30px;")
        self.clave = QtWidgets.QLineEdit(self.centralwidget)
        self.clave.setGeometry(screen_geometry.width() // 2, ((screen_geometry.height() // 3)+(screen_geometry.height() // 70)), 200, 25)
        self.clave.setStyleSheet("background-color: white; font-size: 28px;")

        self.boton_enviar = QtWidgets.QPushButton(self.centralwidget)
        self.boton_enviar.setGeometry(QtCore.QRect(screen_geometry.width()//2-100,(screen_geometry.height())-(screen_geometry.height()//3), 300, 90))
        self.boton_enviar.setText("Eliminar")
        self.boton_enviar.setStyleSheet("""
            QPushButton {
                background-color: #444444;
                color: white;
                font-size: 30px;
                font-weight: bold;
                text-align: center;
                padding: 10px; /* Ajusta el espacio entre el borde y el texto */
            }
            QPushButton:hover {
                background-color: gray;
            }
            QPushButton:pressed {
                background-color: #444444;
            }
        """)


        self.boton_enviar.setCursor(QtCore.Qt.PointingHandCursor)
        self.boton_enviar.clicked.connect(self.eliminar)

        self.logo=logo(self.centralwidget, screen_geometry.width(), screen_geometry.height())
        
        self.botoninfo=botonInfo(self.centralwidget, screen_geometry.width(),screen_geometry.height())
        self.botoninfo.clicked.connect(Info)

        self.setCentralWidget(self.centralwidget)

        # Barra de menú y submenús
        menu(self,"Eliminar consumibles")
    # Método para abrir una nueva ventana
        
        
    #Enviar datos a la base de datos
    def eliminar(self):
        reply=SiNo()

        if reply == QMessageBox.Yes:
            a=str(self.clave.text())
            
            eliminar_datos(a)

    


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Eliminar()
    window.showMaximized()

    sys.exit(app.exec_())
