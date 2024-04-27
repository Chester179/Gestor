import sys
from PyQt5.QtWidgets import QApplication
from Login import Login

# Función principal del programa
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Crea una instancia de QApplication

    window = Login()  # Crea una instancia de la ventana principal
    window.showMaximized()  # Muestra la ventana principal

    sys.exit(app.exec_())
