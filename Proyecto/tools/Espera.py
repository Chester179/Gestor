import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QDesktopWidget
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QTimer
from Buscador import Buscador  # Importa la clase Buscador desde el archivo Buscador.py

class Espera(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cargando")
        icono = QIcon("img/POIxtac.png")
        self.setWindowIcon(icono)
        # Cargar la imagen
        pixmap = QPixmap("img/Espera.png")
        self.setFixedSize(pixmap.width(), pixmap.height())  # Fijar el tamaño de la ventana
        
        # Obtener el tamaño de la pantalla y centrar la ventana en ella
        screen_size = QDesktopWidget().screenGeometry(-1)
        self.move((screen_size.width() - self.width()) // 2, (screen_size.height() - self.height()) // 2)
        
        
        # Crear un QLabel para mostrar la imagen
        self.image_label = QLabel(self)
        self.image_label.setPixmap(pixmap)
        self.image_label.setGeometry(0, 0, pixmap.width(), pixmap.height())

        # Crear un temporizador para cerrar la ventana después de 4 segundos
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.close_window)
        self.timer.start(2000)  # 1000 milisegundos = 1 segundos

    def close_window(self):
        # Abre la nueva ventana de Buscador
        self.timer.stop()
        
        self.new_window = Buscador()
        self.new_window.showMaximized()
        self.close()# Cierra la ventana actual
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    viewer = Espera()
    viewer.show()  # Mostrar la ventana maximizada
    sys.exit(app.exec_())
