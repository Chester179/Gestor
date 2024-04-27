# tools.py
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap,QIcon, QColor
from bd.ColorTabla import colorearmin
import datetime


def editarTexto(centralwidget, x, y):
    texto_input = QtWidgets.QLineEdit(centralwidget)
    texto_input.setGeometry(x, y, 200, 25)
    texto_input.setStyleSheet("background-color: white; font-size: 18px;")  # Setting background color and font size
    return texto_input
def opcmultiple(centralwidget,x,y, tema):
    texto_input = QtWidgets.QComboBox(centralwidget)
    texto_input.setGeometry(x, y, 200, 25)
    if tema is not None:
        temas_str = ["---"]+[str(item[0]) for item in tema]
    else:
        temas_str = ["---"]
    texto_input.addItems(temas_str)
    texto_input.setStyleSheet("background-color: white; font-size: 18px;")
    texto_input.setEditable(False)
    return texto_input
def opcmultipleE(centralwidget,x,y, tema):
    texto_input = QtWidgets.QComboBox(centralwidget)
    texto_input.setGeometry(x, y, 200, 25)
    if tema is not None:
        temas_str = ["---"]+[str(item[0]) for item in tema]
    else:
        temas_str = ["---"]
    texto_input.addItems(temas_str)
    texto_input.setStyleSheet("background-color: white; font-size: 18px;")
    texto_input.setEditable(True)
    return texto_input
def cuadroTexto(centralwidget, x, y):
    texto_input = QtWidgets.QTextEdit(centralwidget)
    texto_input.setGeometry(x, y, 200, 180)  # Tamaño ajustado según sea necesario
    texto_input.setStyleSheet("background-color: white; font-size: 16px;")  # Establecer color de fondo y tamaño de fuente

    # Conectar la función de verificación de longitud del texto
    texto_input.textChanged.connect(lambda: Limitador(texto_input, 250))

    return texto_input
def SiNo():
    msg_box = QtWidgets.QMessageBox()
    msg_box.setIcon(QtWidgets.QMessageBox.Warning)
    icono = QIcon("img/prue.jpg")
    
    msg_box.setWindowIcon(icono)
    msg_box.setStyleSheet("QMessageBox { background-color: red; color: #FFFFFF; }""QPushButton { background-color: yellow; color: black; }")
    msg_box.setText("¿Estás seguro de que deseas realizar esta acción?")
    msg_box.setWindowTitle("Confirmar acción")
    msg_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
    msg_box.setDefaultButton(QtWidgets.QMessageBox.No)
    reply = msg_box.exec_()
    return reply

# Función para verificar la longitud del texto
def Limitador(text_edit, max_length):
      # Límite máximo de caracteres
    if len(text_edit.toPlainText()) > max_length:
        # Si el texto excede el límite máximo, mostrar un mensaje de advertencia y truncar el texto
        QtWidgets.QMessageBox.warning(None, "Advertencia", f"El texto no puede exceder los {max_length} caracteres.")
        text_edit.setPlainText(text_edit.toPlainText()[:max_length])
def Info():
    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle("Información")
    msg.setText("Proyecgto:Gestor de almacén \nVersion 1.8.6.5")
    msg.setFixedSize(1000, 400)
    msg.exec_()
def botonInfo(centralwidget, x, y):
    boton_enviar = QtWidgets.QPushButton(centralwidget)
    pixmap = QPixmap("img/info.png")  # Cambia "img/info.jpg" por la ruta de tu imagen
    boton_enviar.setIcon(QIcon(pixmap))  # Establece el icono en el botón
    boton_enviar.setGeometry(QtCore.QRect(x-(x//23),y-(y//5) , 50, 50))  # Establece las dimensiones del botón
    boton_enviar.setCursor(QtCore.Qt.PointingHandCursor)
    boton_enviar.setIconSize(pixmap.size()) 
    boton_enviar.setStyleSheet("background-color: transparent; border: none;")  # Establece el fondo transparente y elimina el borde del botón
    return boton_enviar
def botonBuscar(centralwidget, x, y,f):
    boton_enviar = QtWidgets.QPushButton(centralwidget)
    boton_enviar.setGeometry(QtCore.QRect(x, y, (f//4)-(f//110), 30))
    boton_enviar.setText("Buscar")
    boton_enviar.setStyleSheet("QPushButton{background-color: #008000;font-weight: bold; color: white;}QPushButton:hover {background-color: #7CCC00;}QPushButton:pressed {background-color: #006400;}")
    boton_enviar.setCursor(QtCore.Qt.PointingHandCursor)
    return boton_enviar
def botonLimpiar(centralwidget, x, y,f):
    boton_enviar = QtWidgets.QPushButton(centralwidget)
    boton_enviar.setGeometry(QtCore.QRect(x, y, (f//4)-(f//110), 30))
    boton_enviar.setText("Limpiar")
    boton_enviar.setStyleSheet("QPushButton{background-color: #FF0000; color: white;font-weight: bold;}QPushButton:hover {background-color: #FF6666;}QPushButton:pressed {background-color: #8B0000;}")
    boton_enviar.setCursor(QtCore.Qt.PointingHandCursor)
    return boton_enviar
def botonModificar(centralwidget, x, y,f):
    boton_enviar = QtWidgets.QPushButton(centralwidget)
    boton_enviar.setGeometry(QtCore.QRect(x, y, (f//4)-(f//110), 30))
    boton_enviar.setText("Modificar")
    boton_enviar.setStyleSheet("QPushButton{background-color: #FFFF00; color: black;font-weight: bold;}QPushButton:hover {background-color: #AAAA00;}QPushButton:pressed {background-color: #FFFF44;}")
    boton_enviar.setCursor(QtCore.Qt.PointingHandCursor)
    return boton_enviar
def boton(centralwidget, x, y):
    boton_enviar = QtWidgets.QPushButton(centralwidget)
    boton_enviar.setGeometry(QtCore.QRect(x, y, 200, 30))
    boton_enviar.setText("Enviar")
    boton_enviar.setStyleSheet("QPushButton{background-color: #008000; color: white;font-weight: bold;}QPushButton:hover {background-color: #7CCC00;}QPushButton:pressed {background-color: #006400;}")
    boton_enviar.setCursor(QtCore.Qt.PointingHandCursor)
    return boton_enviar
def label(centralwidget, texto, x, y):
    label_nombre = QtWidgets.QLabel(centralwidget)
    label_nombre.setGeometry(QtCore.QRect(x, y, 210, 30))
    label_nombre.setText(texto)
    label_nombre.setStyleSheet("color: black; font-family: Arial; font-size: 20px;")  # Setting font family and size
    return label_nombre
def Titulo(centralwidget, texto, x, y):
    label_nombre = QtWidgets.QLabel(centralwidget)
    label_nombre.setGeometry(QtCore.QRect((x//2)-250, y//20, 500, 50))
    label_nombre.setText(texto)
    label_nombre.setStyleSheet("color: Yellow; font-family: Arial; font-size: 40px;")  # Setting font family and size
    return label_nombre
def Subtitulo(centralwidget, texto, x, y):
    label_nombre = QtWidgets.QLabel(centralwidget)
    label_nombre.setGeometry(QtCore.QRect(x, y, 350, 30))
    label_nombre.setText(texto)
    label_nombre.setStyleSheet("color: black; font-family: Arial; font-size: 22px;font-weight: bold;")  # Setting font family and size
    return label_nombre
def botoningresar(centralwidget, x, y):
    boton_enviar = QtWidgets.QPushButton(centralwidget)
    boton_enviar.setGeometry(QtCore.QRect(x, y, 200, 30))
    boton_enviar.setText("Ingresar")
    boton_enviar.setStyleSheet("QPushButton{background-color: #008000; color: white; font-size: 16px; font-weight: bold;}QPushButton:hover {background-color: #7CCC00;}QPushButton:pressed {background-color: #006400;}")
    boton_enviar.setCursor(QtCore.Qt.PointingHandCursor)
    return boton_enviar
def invitado(centralwidget, x, y):
    boton_enviar = QtWidgets.QPushButton(centralwidget)
    boton_enviar.setGeometry(QtCore.QRect(x, y, 200, 30))
    boton_enviar.setText("Invitado")
    boton_enviar.setStyleSheet("""
            QPushButton {
                border-radius: 50px;
                background-color: #444444;
                color: white;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: gray;
            }
            QPushButton:pressed {
                background-color: #444444;
            }
        """)
    boton_enviar.setCursor(QtCore.Qt.PointingHandCursor)
    return boton_enviar
def logo(centralwidget,x,y):
    label = QtWidgets.QLabel(centralwidget)
    pixmap = QPixmap("img/prue.jpg")
    label.setPixmap(pixmap)
    label.setScaledContents(True)
    label.setGeometry(QtCore.QRect((x-(x//7)),-(y//50), 120, 120))
    label.setObjectName("Logo")

def Exito(mensaje):
    
    msg_box = QtWidgets.QMessageBox()
    msg_box.setIcon(QtWidgets.QMessageBox.Information)
    icono = QIcon("img/prue.jpg")
    msg_box.setWindowIcon(icono)
    msg_box.setWindowTitle("¡Logrado!")
    msg_box.setText("Se completo la acción")
    msg_box.setInformativeText(mensaje)
    msg_box.exec_()
  


def Error(mensaje):
    msg_box = QtWidgets.QMessageBox()
    msg_box.setIcon(QtWidgets.QMessageBox.Critical)
    icono = QIcon("img/prue.jpg")
    msg_box.setWindowIcon(icono)
    msg_box.setWindowTitle("¡¡¡ERROR!!!")
    msg_box.setText("Hubo un error en el proceso...")
    msg_box.setInformativeText(mensaje)
    msg_box.exec_()


def minmax(TablaGastos,i):
            clave = TablaGastos.item(i,0)
            if colorearmin(str(clave.text())):
                for k in range(TablaGastos.columnCount()):
                    TablaGastos.item(i, k).setBackground(QColor(255, 0, 0))  # Rojo
                    TablaGastos.item(i, k).setForeground(QColor(255, 255, 0))

def ObtenerFecha():
    fecha_actual = datetime.date.today()
    return fecha_actual

def detectar_horario():
    hora_actual = datetime.datetime.now().time()
    hora = hora_actual.hour
    if 6 <= hora < 14:
        return 1
    elif 14 <= hora < 21:
        return 2
    else:
        return 3