import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
from tools.tools import *
from bd.lectura import datos_opc
from bd.salir import salir_datos
from tools.menu import menu


class Salidas(QMainWindow):
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


        #Tabla de salidas
        self.TablaSalidas = QtWidgets.QTableWidget(self.centralwidget)
        self.TablaSalidas.setGeometry(QtCore.QRect((screen_geometry.width()//2)-(screen_geometry.width()//12), ((screen_geometry.height()//2)-(screen_geometry.height()//15)), (((screen_geometry.width()//17)+(screen_geometry.width()//670)+(screen_geometry.width()//500))*2)+51,(screen_geometry.height()//3)-(screen_geometry.height()//30)))
        self.TablaSalidas.setObjectName("TablaSalidas")
        self.TablaSalidas.setColumnCount(2)
        self.TablaSalidas.setRowCount(20)
        self.TablaSalidas.setStyleSheet("background-color: lightgray;")
        x=(screen_geometry.width())
        tamaños_filas = [((x//17)+(x//670)+(x//500)),((x//17)+(x//670)+(x//500))]  # Lista de tamaños de fila para cada fila en píxeles
        # Configurar los tamaños de fila
        for fila, tamaño in enumerate(tamaños_filas):
            self.TablaSalidas.setColumnWidth(fila, tamaño)
        self.TablaSalidas.setHorizontalHeaderLabels(["Clave","Cantidad"])


        self.TablaSalidas.cellClicked.connect(self.clikeo)
        # Label
        
        self.titulo=Titulo(self.centralwidget,"Salidas de consumibles",screen_geometry.width(),screen_geometry.height())
        self.label = label(self.centralwidget, "Motivo de uso:", (screen_geometry.width()//2)-(screen_geometry.width()//8),(screen_geometry.height() // 4))
        self.Motivo = editarTexto(self.centralwidget, screen_geometry.width() // 2, (screen_geometry.height() // 4))
        self.label = label(self.centralwidget, "Almacenista:", (screen_geometry.width()//2)-(screen_geometry.width()//8), (screen_geometry.height() // 4)+(screen_geometry.height() // 24))
        self.Almacenista = editarTexto(self.centralwidget, screen_geometry.width() // 2, (screen_geometry.height() // 4)+(screen_geometry.height() // 24))
        self.label = label(self.centralwidget, "Solicitante:", (screen_geometry.width()//2)-(screen_geometry.width()//8), (screen_geometry.height() // 3)+(screen_geometry.height() // 300))
        tema=datos_opc("Solicitante","",3)
        self.Solicitante = opcmultipleE(self.centralwidget, screen_geometry.width() // 2, (screen_geometry.height() // 3)+(screen_geometry.height() // 300), tema)
        

        self.label = label(self.centralwidget, "Nombre:", screen_geometry.width() // 10, (screen_geometry.height() // 2)-(screen_geometry.height() // 30))
        self.Nombre = editarTexto(self.centralwidget, screen_geometry.width()//5, (screen_geometry.height() // 2)-(screen_geometry.height()//30))
        self.label = label(self.centralwidget, "Medida:", screen_geometry.width() // 10,(screen_geometry.height() // 2)+(screen_geometry.height() // 56))
        self.Medida = editarTexto(self.centralwidget, screen_geometry.width()//5, (screen_geometry.height() // 2)+(screen_geometry.height() // 56))
        


        self.boton=boton(self.centralwidget,(screen_geometry.width()//2)+20,(screen_geometry.height())-((screen_geometry.height()//5)-(screen_geometry.height()//55)))
        self.boton.clicked.connect(self.salidas)
        self.limpiar=boton(self.centralwidget,(screen_geometry.width()//2)-220,(screen_geometry.height())-((screen_geometry.height()//5)-(screen_geometry.height()//55)))
        self.limpiar.setText("Limpiar")
        self.limpiar.setStyleSheet("QPushButton{background-color: #FF0000; color: white;font-weight: bold;}QPushButton:hover {background-color: #FF6666;}QPushButton:pressed {background-color: #8B0000;}")
        self.limpiar.clicked.connect(self.Limpiar)
        self.logo=logo(self.centralwidget, screen_geometry.width(), screen_geometry.height())
        
        self.botoninfo=botonInfo(self.centralwidget, screen_geometry.width(),screen_geometry.height())
        self.botoninfo.clicked.connect(Info)

        self.setCentralWidget(self.centralwidget)

        # Barra de menú y submenús
        menu(self,"Salida de consumibles")
    def clikeo(self, row,column):
        from bd.lectura import datosTabla
        item = self.TablaSalidas.item(row, 0)
        
        #       "a" es la variable que tiene la clave
        if item != None:
            a=str(item.text())
            Nombre,Medida= datosTabla(a,5)
            self.Nombre.setText(Nombre)
            self.Medida.setText(Medida)
        
    def Limpiar(self):
        self.Motivo.setText("")
        self.Almacenista.setText("")
        self.Solicitante.setCurrentText("---")
        self.Nombre.setText("")
        self.Medida.setText("")
        for row_number in range(20):
            for column_number in range(2):
                self.TablaSalidas.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str("")))
        #Enviar datos a la base de datos
    def salidas(self):
    # Obtener el texto ingresado en los widgets de la interfaz de usuario
        
        motivo = self.Motivo.text()
        almacenista = self.Almacenista.text()
        solicitante = self.Solicitante.currentText()
        
        
        #Manda los datos a la base de datos
        salir_datos(self.TablaSalidas, motivo, almacenista,solicitante)
        self.Limpiar()
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Salidas()
    window.showMaximized()

    sys.exit(app.exec_())
