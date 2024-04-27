import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QPushButton, QFileDialog
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
from tools.tools import *
from tools.menu import menu
from bd.lectura import datos_opc
from bd.agregar import cargar_datos

class Agregar(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setObjectName("Chester")
        # Obtener las dimensiones de la pantalla
        screen_geometry = QDesktopWidget().screenGeometry()
        menu(self,"Buscador de consumibles")
        # Configurar la geometría de la ventana para que tenga el tamaño máximo

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
        self.titulo=Titulo(self.centralwidget,"Agregrar consumibles",screen_geometry.width(),screen_geometry.height()//2)
        self.button = QPushButton(self)
        self.set_button_icon("img/Icono.png")  # Ruta de la imagen de fondo
        self.button.clicked.connect(self.load_image)
        self.button.setGeometry(QtCore.QRect(50, (screen_geometry.height() // 5)-(screen_geometry.height() // 100), 240, 300))
        self.button.setObjectName("Herramienta")

        self.label = label(self.centralwidget, "Cantidad a ingresar:", screen_geometry.width() // 4-screen_geometry.width() // 33-screen_geometry.width() //911, (screen_geometry.height() // 5)-(screen_geometry.height() // 100))
        self.Cantidad = editarTexto(self.centralwidget, screen_geometry.width()//3+screen_geometry.width()//25, (screen_geometry.height() // 5)-(screen_geometry.height()//210))
        self.label = label(self.centralwidget, "Nombre de consumible:", screen_geometry.width() // 4-screen_geometry.width() // 33-screen_geometry.width() //911, (screen_geometry.height() // 4)-(screen_geometry.height() // 219))
        self.Nombre = editarTexto(self.centralwidget, screen_geometry.width()//3+screen_geometry.width()//25, (screen_geometry.height() // 4)-(screen_geometry.height() // 308))
        self.label = label(self.centralwidget, "Medida:", screen_geometry.width() // 4-screen_geometry.width() // 33-screen_geometry.width() //911, (screen_geometry.height() // 3)-(screen_geometry.height() // 30))
        self.Medida = editarTexto(self.centralwidget, screen_geometry.width()//3+screen_geometry.width()//25, (screen_geometry.height() // 4)+(screen_geometry.height() // 20))
        self.label = label(self.centralwidget, "Descripción:", screen_geometry.width() // 4-screen_geometry.width() // 33-screen_geometry.width() //911,(screen_geometry.height() // 3)+(screen_geometry.height() // 14))
        self.Descripcion = cuadroTexto(self.centralwidget, screen_geometry.width()//3+screen_geometry.width()//25, (screen_geometry.height() // 3)+(screen_geometry.height()//56))
        
        self.label = Subtitulo(self.centralwidget, "Especificaciones del consumible", screen_geometry.width() // 2+screen_geometry.width() // 10, screen_geometry.height() // 8)
        tema=datos_opc("Proveedor","",1)
        self.label = label(self.centralwidget, "Proovedor:", screen_geometry.width() // 2+screen_geometry.width() // 13, (screen_geometry.height() // 5)-(screen_geometry.height() // 100))
        self.Proveedor = opcmultipleE(self.centralwidget, screen_geometry.width()//2+screen_geometry.width()//5, (screen_geometry.height() // 5)-(screen_geometry.height()//210),tema)
        tema=datos_opc("Categoria","",1)
        self.label = label(self.centralwidget, "Familia:", screen_geometry.width() // 2+screen_geometry.width() // 13, (screen_geometry.height() // 4)-(screen_geometry.height() // 219))
        self.Familia = opcmultipleE(self.centralwidget, screen_geometry.width()//2+screen_geometry.width()//5, (screen_geometry.height() // 4)-(screen_geometry.height() // 318),tema)
        tema=datos_opc("TipoMaterial","",1)
        self.label = label(self.centralwidget, "Tipo de material:", screen_geometry.width() // 2+screen_geometry.width() // 13, (screen_geometry.height() // 3)-(screen_geometry.height() // 30))
        self.TipoMaterial = opcmultipleE(self.centralwidget, screen_geometry.width()//2+screen_geometry.width() // 5, (screen_geometry.height() // 4)+(screen_geometry.height() // 20),tema)
        tema=datos_opc("U_Medida","",1)
        self.label = label(self.centralwidget, "Unidad de Medida:", screen_geometry.width() // 2+screen_geometry.width() // 13, (screen_geometry.height() // 3)+(screen_geometry.height() // 48))
        self.Unidamedida = opcmultipleE(self.centralwidget, screen_geometry.width()//2+screen_geometry.width() // 5, (screen_geometry.height() // 3)+(screen_geometry.height()//56),tema)
        tema=datos_opc("Lugar","",1)
        self.label = label(self.centralwidget, "Ubicación:", screen_geometry.width() // 2+screen_geometry.width() // 13, (screen_geometry.height() // 3)+(screen_geometry.height() // 14))
        self.Lugar = opcmultipleE(self.centralwidget, screen_geometry.width()//2+screen_geometry.width() // 5, (screen_geometry.height() // 3)+(screen_geometry.height() // 14)-(screen_geometry.height()//911),tema)
        self.label = label(self.centralwidget, "Máximos:", screen_geometry.width() // 2+screen_geometry.width() // 13,((screen_geometry.height() // 2)-(screen_geometry.height() // 22)-(screen_geometry.height())//911))
        self.Maximo = editarTexto(self.centralwidget, screen_geometry.width()//2+screen_geometry.width() // 5, ((screen_geometry.height() // 2)-(screen_geometry.height() // 22)-(screen_geometry.height())//911))
        self.label = label(self.centralwidget, "Mínimos:", screen_geometry.width() // 2+screen_geometry.width() // 13,((screen_geometry.height() // 2)+(screen_geometry.height() // 130)))
        self.Minimo = editarTexto(self.centralwidget, screen_geometry.width()//2+screen_geometry.width() // 5, ((screen_geometry.height() // 2)+(screen_geometry.height() // 130)))
        
        

        self.boton = boton(self.centralwidget, (screen_geometry.width()//2)-100, (screen_geometry.height())-((screen_geometry.height()//5)-(screen_geometry.height()//55)))
        self.boton.clicked.connect(self.ingresos)

        self.logo = logo(self.centralwidget, screen_geometry.width(), screen_geometry.height())

        self.botoninfo = botonInfo(self.centralwidget, screen_geometry.width(), screen_geometry.height())
        self.botoninfo.clicked.connect(Info)

        self.setCentralWidget(self.centralwidget)

    # Enviar datos a la base de datos
    def ingresos(self):
        # Obtener el texto ingresado en los widgets de la interfaz de usuario
        nombre = self.Nombre.text()
        caracteristica = self.Descripcion.toPlainText()
        medida = self.Medida.text()
        proveedor = self.Proveedor.currentText()
        unidad_Medida = self.Unidamedida.currentText()
        maximo = self.Maximo.text()
        minimo = self.Minimo.text()
        familia = self.Familia.currentText()
        cantidad= self.Cantidad.text()

        # Crear un objeto QPixmap desde el botón para obtener la imagen
        pixmap = self.button.icon().pixmap(QtCore.QSize(250, 300))

        # Convertir la imagen a bytes
        byte_array = QtCore.QByteArray()
        buffer = QtCore.QBuffer(byte_array)
        buffer.open(QtCore.QIODevice.WriteOnly)
        pixmap.save(buffer, "PNG")  # Puedes elegir otro formato como JPG si lo deseas
        byte_array = byte_array.data()

        # Enviar los datos y la imagen a la otra clase para almacenarlos en la base de datos
        cargar_datos(nombre, caracteristica, medida, unidad_Medida, proveedor,familia, maximo, minimo, byte_array, cantidad)

    def set_button_icon(self, image_path):
        pixmap = QPixmap(image_path)
        scaled_pixmap = pixmap.scaled(250, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)  # Escalar la imagen
        icon = QIcon(scaled_pixmap)
        self.button.setIcon(icon)
        self.button.setIconSize(QtCore.QSize(250, 300))  # Establecer el tamaño del icono del botón
        self.button.setStyleSheet("QPushButton { border: none; }")

    def load_image(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Seleccionar Imagen", "", "Imágenes (*.png *.jpg *.bmp)")

        if file_path:
            # Aquí puedes manejar la imagen cargada como lo desees
            self.set_button_icon(file_path)
        else:
            file_path = "img/icono.png"
            self.set_button_icon(file_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Agregar()
    window.showMaximized()

    sys.exit(app.exec_())
