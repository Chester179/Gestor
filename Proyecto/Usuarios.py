import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget,  QPushButton,QFileDialog, QMessageBox
from tools.tools import *
from bd.agregar import agregarUsuarios
from bd.Eliminar import eliminarUsuarios
from tools.menu import menu, setrango
from bd.cambio import modificarUsuarios
from PyQt5.QtCore import Qt
from bd.lectura import cargar_datosUsuarios, datosTabla, datos_opc,maxmin


class Usuarios(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pixmap = QPixmap()
        self.setObjectName("Chester")
        # Obtener las dimensiones de la pantalla
        screen_geometry = QDesktopWidget().screenGeometry()

        # Configurar la geometría de la ventana para que tenga el tamaño máximo
        self.setGeometry(0, 0, screen_geometry.width(), screen_geometry.height()-26)
        
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
        self.TablaGastos = QtWidgets.QTableWidget(self.centralwidget)
        self.TablaGastos.setGeometry(QtCore.QRect((screen_geometry.width()//6), ((screen_geometry.height()//2)+(screen_geometry.height()//18)+(screen_geometry.height()//911)), (screen_geometry.width()-(screen_geometry.width()//4+screen_geometry.width()//13+screen_geometry.width()//48)),(screen_geometry.height()//3)-(screen_geometry.height()//30)))
        self.TablaGastos.setObjectName("TablaGastos")
        self.TablaGastos.setColumnCount(5)
        self.TablaGastos.setRowCount(0)
        self.TablaGastos.setStyleSheet("background-color: lightgray;")
        x=(screen_geometry.width()-screen_geometry.width()//11)
        tamaños_filas = [((x//17)+(x//670)+(x//500)),((x//4)-(x//110)+(x//1000)),(x//3)-(x//5),(x//3)-(x//5),(x//3)-(x//5),(x//5)]  # Lista de tamaños de fila para cada fila en píxeles
        # Configurar los tamaños de fila
        for fila, tamaño in enumerate(tamaños_filas):
            self.TablaGastos.setColumnWidth(fila, tamaño)
        self.TablaGastos.setHorizontalHeaderLabels(["ID","Nombre", "Apellido paterno", "Apellido materno", "Numero telefonico"])
        self.TablaGastos.cellClicked.connect(self.clikeo)
        self.titulo=Titulo(self.centralwidget,"Usuarios de almacén",screen_geometry.width(),screen_geometry.height()//2)
        self.logo=logo(self.centralwidget, screen_geometry.width(), screen_geometry.height())
        self.botoninfo=botonInfo(self.centralwidget, screen_geometry.width(),screen_geometry.height())
        self.botoninfo.clicked.connect(Info)
        
        """"
        
                            Buscador y muestra de datos

        """
        # Definir button como un atributo de la clase
        self.button = QPushButton(self)
        self.set_button_icon("img/usuarios.png")  # Ruta de la imagen de fondo
        self.button.clicked.connect(self.load_image)
        self.button.setGeometry(QtCore.QRect(50, 60, 240, 300))
        self.button.setObjectName("Herramienta")

        self.label = label(self.centralwidget, "Usuario:", screen_geometry.width() // 4-screen_geometry.width() // 33-screen_geometry.width() //911, (screen_geometry.height() // 5)-(screen_geometry.height() // 100))
        self.Usuario = editarTexto(self.centralwidget, screen_geometry.width()//3+screen_geometry.width()//25,  (screen_geometry.height() // 5)-(screen_geometry.height() // 210))
        self.label = label(self.centralwidget, "ID:", screen_geometry.width() // 4-screen_geometry.width() // 33-screen_geometry.width() //911, (screen_geometry.height() // 7)-(screen_geometry.height() // 120))
        self.id = editarTexto(self.centralwidget, screen_geometry.width()//3+screen_geometry.width()//25, screen_geometry.height() // 7)
        self.label = label(self.centralwidget, "Nivel de autoridad:", screen_geometry.width() // 4-screen_geometry.width() // 33-screen_geometry.width() //911, (screen_geometry.height() // 3)-(screen_geometry.height() // 30))
        self.Nivel = opcmultiple(self.centralwidget, screen_geometry.width()//3+screen_geometry.width()//25, (screen_geometry.height() // 4)+(screen_geometry.height()//20),["1","2","3"])
        self.label = label(self.centralwidget, "Contraseña:", screen_geometry.width() // 4-screen_geometry.width() // 33-screen_geometry.width() //911, (screen_geometry.height() // 4)-(screen_geometry.height() // 219))
        self.Contrasena = editarTexto(self.centralwidget, screen_geometry.width()//3+screen_geometry.width()//25, (screen_geometry.height() // 4)-(screen_geometry.height() // 318))
        self.id.setReadOnly(True)

        self.label = Subtitulo(self.centralwidget, "Datos personales", screen_geometry.width() // 2+screen_geometry.width() // 10, screen_geometry.height() // 12)
        
        self.label = label(self.centralwidget, "Nombre:", screen_geometry.width() // 2+screen_geometry.width() // 18, (screen_geometry.height() // 7)-(screen_geometry.height() // 120))
        self.nombre = editarTexto(self.centralwidget, screen_geometry.width()//2+screen_geometry.width()//5, (screen_geometry.height() // 7))
        
        self.label = label(self.centralwidget, "Apellido Parterno:", screen_geometry.width() // 2+screen_geometry.width() // 18, (screen_geometry.height() // 5)-(screen_geometry.height() // 100))
        self.apellidop = editarTexto(self.centralwidget, screen_geometry.width()//2+screen_geometry.width()//5, (screen_geometry.height() // 5)-(screen_geometry.height() // 210))
        
        self.label = label(self.centralwidget, "Apellido Materno:", screen_geometry.width() // 2+screen_geometry.width() // 18, (screen_geometry.height() // 4)-(screen_geometry.height() // 219))
        self.apellidom = editarTexto(self.centralwidget, screen_geometry.width()//2+screen_geometry.width() // 5, (screen_geometry.height() // 4)-(screen_geometry.height() // 318))
        
        self.label = label(self.centralwidget, "Numero de telefono:", screen_geometry.width() // 2+screen_geometry.width() // 18, (screen_geometry.height() // 3)-(screen_geometry.height() // 30))
        self.num = editarTexto(self.centralwidget, screen_geometry.width()//2+screen_geometry.width() // 5, (screen_geometry.height() // 4)+(screen_geometry.height()//20))
        
        
        
        self.agregar = botonBuscar(self.centralwidget,screen_geometry.width()//13,(screen_geometry.height() // 2)-(screen_geometry.height() // 110),screen_geometry.width())
        self.eliminar = botonLimpiar(self.centralwidget,screen_geometry.width()//2+screen_geometry.width()//10,(screen_geometry.height() // 2)-(screen_geometry.height() // 110),screen_geometry.width())
        self.modificar = botonModificar(self.centralwidget,screen_geometry.width()//2-screen_geometry.width()//6+screen_geometry.width()//250,(screen_geometry.height() // 2)-(screen_geometry.height() // 110),screen_geometry.width())
        self.agregar.setText("Agregar")
        self.eliminar.setText("Eliminar")
        #################################################################################################
        #                                        ACIONES                                                #
        #################################################################################################
        
        self.agregar.clicked.connect(self.Agregar)
        self.eliminar.clicked.connect(self.Eliminar)
        self.modificar.clicked.connect(self.Modificar)
        #################################################################################################
        self.setCentralWidget(self.centralwidget)
        
        # Barra de menú y submenús
        menu(self,"Modificar consumibles")
        cargar_datosUsuarios(self.TablaGastos,"")
    def Eliminar(self):
        reply=SiNo()

        if reply == QMessageBox.Yes:
            a=str(self.id.text())
            b=str(self.Usuario.text())
            eliminarUsuarios(a, b)
            cargar_datosUsuarios(self.TablaGastos,"")
            self.Usuario.setText("")
            self.Contrasena.setText("")
            self.Nivel.setCurrentText("---")
            self.nombre.setText("")
            self.apellidop.setText("")
            self.apellidom.setText("")
            self.num.setText("")
            self.id.setText("")
            self.set_button_icon("img/usuarios.png")
    def Agregar(self):
        Usuario=self.Usuario.text()
        Contrasena=self.Contrasena.text()
        Nivel=self.Nivel.currentText()
        Nombre=self.nombre.text()
        ApeP=self.apellidop.text()
        ApeM=self.apellidom.text()
        Num=self.num.text()
        pixmap = self.button.icon().pixmap(QtCore.QSize(250, 300))
        # Convertir la imagen a bytes
        byte_array = QtCore.QByteArray()
        buffer = QtCore.QBuffer(byte_array)
        buffer.open(QtCore.QIODevice.WriteOnly)
        pixmap.save(buffer, "PNG")  # Puedes elegir otro formato como JPG si lo deseas
        byte_array = byte_array.data()
        if Usuario and Contrasena and Nivel:
            agregarUsuarios(Usuario,Contrasena,Nivel,Nombre, ApeP, ApeM,Num, byte_array)
            cargar_datosUsuarios(self.TablaGastos,"")

    def Modificar(self):
        id=self.id.text()
        Usuario=self.Usuario.text()
        Contrasena=self.Contrasena.text()
        Nivel=self.Nivel.currentText()
        Nombre=self.nombre.text()
        ApeP=self.apellidop.text()
        ApeM=self.apellidom.text()
        Num=self.num.text()
        pixmap = self.button.icon().pixmap(QtCore.QSize(250, 300))
        # Convertir la imagen a bytes
        byte_array = QtCore.QByteArray()
        buffer = QtCore.QBuffer(byte_array)
        buffer.open(QtCore.QIODevice.WriteOnly)
        pixmap.save(buffer, "PNG")  # Puedes elegir otro formato como JPG si lo deseas
        byte_array = byte_array.data()
        if Usuario and Contrasena:
            modificarUsuarios(id,Usuario,Contrasena,Nivel,Nombre, ApeP, ApeM,Num, byte_array)
            cargar_datosUsuarios(self.TablaGastos,"")
            setrango(str(Nivel))
            menu(self,"Modificar consumibles")
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
            file_path = "img/usuarios.png"
            self.set_button_icon(file_path)



    def clikeo(self, row,column):
        item = self.TablaGastos.item(row, 0)
        a=str(item.text())
        #       "a" es la variable que tiene la clave
        
        id,usuario,contra,nivel,nombre,apep,apem,numtel, imagen = datosTabla(a,3)
        self.id.setText(str(id))
        self.Usuario.setText(usuario)
        self.Contrasena.setText(contra)
        self.Nivel.setCurrentText(str(nivel))
        self.nombre.setText(nombre)
        self.apellidop.setText(apep)
        self.apellidom.setText(apem)
        self.num.setText(str(numtel))
        if imagen:

            self.pixmap.loadFromData(imagen)
            self.set_button_icon(self.pixmap)
            
        else:
            self.pixmap=QPixmap("img/usuarios.png")
            self.set_button_icon(self.pixmap)
        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Usuarios()
    window.showMaximized()

    sys.exit(app.exec_())
