import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
from bd.lectura import cargar_movs, datos_opc, datosTabla
from bd.agregar import agregarcomentario
from tools.tools import *
from tools.menu import menu

class Historialacciones(QMainWindow):
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
        self.TablaGastos = QtWidgets.QTableWidget(self.centralwidget)
        self.TablaGastos.setGeometry(QtCore.QRect((screen_geometry.width()//25), ((screen_geometry.height()//2)+(screen_geometry.height()//18)+(screen_geometry.height()//911)), (screen_geometry.width()-screen_geometry.width()//11),(screen_geometry.height()//3)-(screen_geometry.height()//30)))
        self.TablaGastos.setObjectName("TablaGastos")
        self.TablaGastos.setColumnCount(4)
        self.TablaGastos.setRowCount(0)
        self.TablaGastos.setStyleSheet("background-color: lightgray;")
        x=(screen_geometry.width()-screen_geometry.width()//11)
        tamaños_filas = [x//10,x//3+x//19,x//4,x//4]
        # Configurar los tamaños de fila
        for fila, tamaño in enumerate(tamaños_filas):
            self.TablaGastos.setColumnWidth(fila, tamaño)

        self.TablaGastos.setHorizontalHeaderLabels(["ID", "Descripción", "Categoria", "Fecha"])

        self.TablaGastos.cellClicked.connect(self.clikeo)
        
        self.logo=logo(self.centralwidget, screen_geometry.width(), screen_geometry.height())
        
        self.botoninfo=botonInfo(self.centralwidget, screen_geometry.width(),screen_geometry.height())
        self.botoninfo.clicked.connect(Info)
        self.titulo=Titulo(self.centralwidget,"Historial de acciones",screen_geometry.width(),screen_geometry.height())
        
        self.setCentralWidget(self.centralwidget)
        
        ########################################################################################################################
        
        
        
        
       
        self.label = label(self.centralwidget, "ID:", screen_geometry.width() // 10, (screen_geometry.height() // 5)-(screen_geometry.height() // 100))
        self.ID = editarTexto(self.centralwidget, screen_geometry.width()//5, (screen_geometry.height() // 5)-(screen_geometry.height() // 210))
        self.label = label(self.centralwidget, "Fecha:", screen_geometry.width() // 10, (screen_geometry.height() // 4)-(screen_geometry.height() // 219))
        self.Fecha = editarTexto(self.centralwidget, screen_geometry.width()//5, (screen_geometry.height() // 4)-(screen_geometry.height()//318))
        self.label = label(self.centralwidget, "Comentarios:", screen_geometry.width() // 10, (screen_geometry.height() // 3)-(screen_geometry.height() // 30))
        self.Observaciones = cuadroTexto(self.centralwidget, screen_geometry.width() // 5, (screen_geometry.height() // 3)-(screen_geometry.height() // 30))
        self.ID.setReadOnly(True)
        tema=datos_opc("Categoria","",4)
        self.label = label(self.centralwidget, "Categoria:", screen_geometry.width() // 2+screen_geometry.width() // 10, (screen_geometry.height() // 5)-(screen_geometry.height() // 100))
        self.Categoria = opcmultiple(self.centralwidget, screen_geometry.width() // 2+screen_geometry.width() // 5, (screen_geometry.height() // 5)-(screen_geometry.height() // 210), tema)
        
        self.label = label(self.centralwidget, "Descripciòn:", screen_geometry.width() // 2+screen_geometry.width() // 10, (screen_geometry.height() // 3)-(screen_geometry.height() // 30))
        self.Descripcion = cuadroTexto(self.centralwidget, screen_geometry.width() // 2+screen_geometry.width() // 5, (screen_geometry.height() // 4)-(screen_geometry.height() // 318))
        
        self.modificar = botonModificar(self.centralwidget,screen_geometry.width()//2-screen_geometry.width()//8,(screen_geometry.height() // 2)-(screen_geometry.height() // 16)-(screen_geometry.height() // 911),screen_geometry.width())
        self.boton = botonBuscar(self.centralwidget,screen_geometry.width()//2-screen_geometry.width()//8,(screen_geometry.height() // 2)-(screen_geometry.height() // 8)+(screen_geometry.height() // 140),screen_geometry.width())
        self.limpiar = botonLimpiar(self.centralwidget,screen_geometry.width()//2-screen_geometry.width()//8,(screen_geometry.height() // 2)-(screen_geometry.height() // 110),screen_geometry.width())
        
        #################################################################################################
        #                                        ACIONES                                                #
        #################################################################################################
        self.boton.clicked.connect(self.buscartabla)
        self.limpiar.clicked.connect(self.limpia)
        self.modificar.clicked.connect(self.modifica)
        #################################################################################################
        
        
        
        
        
        
        
        
        ########################################################################################################################
        # Barra de menú y submenús
        menu(self,"Historial de acciones")
        cargar_movs(self.TablaGastos,"")
    def clikeo(self, row,column):
        item = self.TablaGastos.item(row, 0)
        a=str(item.text())
        #       "a" es la variable que tiene la clave
        
        ID,Descripcion,Categoria,Fecha, Observaciones = datosTabla(a,4)
        self.ID.setText(str(ID))
        self.Descripcion.setText(str(Descripcion))
        self.Categoria.setCurrentText(Categoria)
        self.Fecha.setText(Fecha.strftime('%Y-%m-%d'))
        self.Observaciones.setText(str(Observaciones))
        
    def modifica(self):
        ID=self.ID.text()
        Comentario=self.Observaciones.toPlainText()
        agregarcomentario(ID,Comentario)
    def limpia(self):
        self.ID.setText("")
        self.Fecha.setText("")
        self.Descripcion.setText("")
        self.Categoria.setCurrentText("---")
        self.Observaciones.setText("")
        cargar_movs(self.TablaGastos,"")
    def buscartabla(self):
        ID=self.ID.text()
        Fecha=self.Fecha.text()
        Descripcion=self.Descripcion.toPlainText()
        Categoria=self.Categoria.currentText()
        Observaciones=self.Observaciones.toPlainText()
        comando=""
        b=()
        a=""
        constructor=True
        if(ID=="" and Fecha=="" and Descripcion=="" and Observaciones=="" and Categoria=="---"):
            Error("¡¡Escriba algo!!")
            constructor=False
        elif("" != ID and Fecha=="" and Descripcion=="" and Observaciones=="" and Categoria=="---"):
            a = "WHERE ID = '{}'"
            comando=a.format(ID)
            constructor=False
        
        if(Fecha!=""):
            if("WHERE" in a):
                a+=" AND Fecha LIKE '%{}%'"
                b+=(Fecha,)
            else:
                a+="WHERE Fecha LIKE '%{}%'"
                b+=(Fecha,)

        if(Observaciones!=""):
            if("WHERE" in a):
                a+=" AND Observaciones LIKE '%{}%'"
                b+=(Observaciones,)
            else:
                a+="WHERE Observaciones LIKE '%{}%'"
                b+=(Observaciones,)

        if(Descripcion!=""):
            if("WHERE" in a):
                a+=" AND Descripcion LIKE '%{}%'"
                b+=(Descripcion,)
            else:
                a+="WHERE Descripcion LIKE '%{}%'"
                b+=(Descripcion,)

        if(Categoria!="---"):
            if("WHERE" in a):
                a+=" AND Categoria LIKE '%{}%'"
                b+=(Categoria,)
            else:
                a+="WHERE Categoria LIKE '%{}%'"
                b+=(Categoria,) 
        
        
        
        if constructor:
            comando=a.format(*(str(item) for item in b))
        cargar_movs(self.TablaGastos,comando)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Historialacciones()
    window.showMaximized()
    sys.exit(app.exec_())
