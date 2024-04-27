import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
from bd.lectura import cargar_vales, datos_opc, datosTabla
from tools.tools import *
from tools.menu import menu

class Historial(QMainWindow):
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
        self.TablaVales = QtWidgets.QTableWidget(self.centralwidget)
        self.TablaVales.setGeometry(QtCore.QRect((screen_geometry.width()//25), ((screen_geometry.height()//2)+(screen_geometry.height()//18)+(screen_geometry.height()//911)), (screen_geometry.width()-screen_geometry.width()//11),(screen_geometry.height()//3)-(screen_geometry.height()//30)))
        self.TablaVales.setObjectName("TablaVales")
        self.TablaVales.setColumnCount(9)
        self.TablaVales.setRowCount(0)
        self.TablaVales.setStyleSheet("background-color: lightgray;")
        x=(screen_geometry.width()-screen_geometry.width()//11)
        tamaños_filas = [x//13+x//450,x//9,x//9,x//9,x//9,x//9,x//9,x//9,x//9]
        # Configurar los tamaños de fila
        for fila, tamaño in enumerate(tamaños_filas):
            self.TablaVales.setColumnWidth(fila, tamaño)

        self.TablaVales.setHorizontalHeaderLabels(["Folio", "Clave","Nombre", "Medida", "Motivo", "Almacenista", "Solicitante", "Salida", "Fecha"])

        self.TablaVales.cellClicked.connect(self.clikeo)
        
        self.logo=logo(self.centralwidget, screen_geometry.width(), screen_geometry.height())
        
        self.botoninfo=botonInfo(self.centralwidget, screen_geometry.width(),screen_geometry.height())
        self.botoninfo.clicked.connect(Info)
        self.titulo=Titulo(self.centralwidget,"Historial de vales",screen_geometry.width(),screen_geometry.height())
        
        self.setCentralWidget(self.centralwidget)
        
        ########################################################################################################################
        
        
        
        
        self.label = label(self.centralwidget, "Folio:", screen_geometry.width() // 10, (screen_geometry.height() // 5)-(screen_geometry.height() // 100))
        self.Folio = editarTexto(self.centralwidget, screen_geometry.width()//5, (screen_geometry.height() // 5)-(screen_geometry.height() // 210))
        self.Folio.setText("0000")
        self.label = label(self.centralwidget, "Clave:", screen_geometry.width() // 10, (screen_geometry.height() // 4)-(screen_geometry.height() // 219))
        self.Clave = editarTexto(self.centralwidget, screen_geometry.width()//5, (screen_geometry.height() // 4)-(screen_geometry.height() // 318))
        self.label = label(self.centralwidget, "Nombre:", screen_geometry.width() // 10, (screen_geometry.height() // 3)-(screen_geometry.height() // 30))
        self.Nombre = editarTexto(self.centralwidget, screen_geometry.width()//5, (screen_geometry.height() // 4)+(screen_geometry.height()//20))
        self.label = label(self.centralwidget, "Medida:", screen_geometry.width() // 10,(screen_geometry.height() // 3)+(screen_geometry.height() // 48))
        self.Medida = editarTexto(self.centralwidget, screen_geometry.width()//5, (screen_geometry.height() // 3)+(screen_geometry.height() // 56))
        
        
        tema=datos_opc("Motivo","",2)
        self.label = label(self.centralwidget, "Motivo:", screen_geometry.width() // 2+screen_geometry.width() // 10, (screen_geometry.height() // 5)-(screen_geometry.height() // 100))
        self.Motivo = opcmultiple(self.centralwidget, screen_geometry.width() // 2+screen_geometry.width() // 5, (screen_geometry.height() // 5)-(screen_geometry.height() // 210),tema)
        tema=datos_opc("Almacenista","",2)
        self.label = label(self.centralwidget, "Almacenista:", screen_geometry.width() // 2+screen_geometry.width() // 10, (screen_geometry.height() // 4)-(screen_geometry.height() // 219))
        self.Almacenista = opcmultiple(self.centralwidget, screen_geometry.width() // 2+screen_geometry.width() // 5, (screen_geometry.height() // 4)-(screen_geometry.height() // 318),tema)
        tema=datos_opc("Solicitante","",2)
        self.label = label(self.centralwidget, "Solicitante:", screen_geometry.width() // 2+screen_geometry.width() // 10, (screen_geometry.height() // 3)-(screen_geometry.height() // 30))
        self.Solicitante = opcmultiple(self.centralwidget, screen_geometry.width() // 2+screen_geometry.width() // 5, (screen_geometry.height() // 4)+(screen_geometry.height()//20),tema)
        tema=datos_opc("Fecha","",2)
        self.label = label(self.centralwidget, "Fecha:", screen_geometry.width() // 2+screen_geometry.width() // 10, (screen_geometry.height() // 3)+(screen_geometry.height() // 48))
        self.Fecha = opcmultiple(self.centralwidget, screen_geometry.width() // 2+screen_geometry.width() // 5, (screen_geometry.height() // 3)+(screen_geometry.height() // 56),tema)
        self.boton = botonBuscar(self.centralwidget,screen_geometry.width()//20,(screen_geometry.height() // 2)-(screen_geometry.height() // 16)-(screen_geometry.height() // 911),screen_geometry.width())
        self.imprimir = botonModificar(self.centralwidget,screen_geometry.width()//2-screen_geometry.width()//8,(screen_geometry.height() // 2)-(screen_geometry.height() // 16)-(screen_geometry.height() // 911),screen_geometry.width())
        self.limpiar = botonLimpiar(self.centralwidget,screen_geometry.width()-screen_geometry.width()//3,(screen_geometry.height() // 2)-(screen_geometry.height() // 16)-(screen_geometry.height() // 911),screen_geometry.width())
        self.imprimir.setText("Imprimir")
        #################################################################################################
        #                                        ACIONES                                                #
        #################################################################################################
        self.boton.clicked.connect(self.buscartabla)
        self.limpiar.clicked.connect(self.limpia)
        self.imprimir.clicked.connect(self.Imprimir)
        #################################################################################################
        
        
        
        
        
        
        
        
        ########################################################################################################################
        # Barra de menú y submenús
        menu(self,"Historial de vales")
        cargar_vales(self.TablaVales,"")
    def clikeo(self, row,column):
        item = self.TablaVales.item(row, 0)
        a=str(item.text())
        #       "a" es la variable que tiene la clave
        self.Clave.setText(a)
        Clave,Nombre,Medida,motivo,almacenista,solicitante,fecha = datosTabla(a,2)
        self.Nombre.setText(Nombre)
        self.Medida.setText(Medida)
        self.Clave.setText(Clave)
        self.Folio.setText(a)
        self.Almacenista.setCurrentText(almacenista)
        self.Solicitante.setCurrentText(solicitante)
        self.Motivo.setCurrentText(motivo)
        self.Fecha.setCurrentText(fecha.strftime('%Y-%m-%d'))

    def Imprimir(self):
        from tools.Excel import export_to_excel
        export_to_excel(self)

    def limpia(self):
        self.Clave.setText("")
        self.Nombre.setText("")
        self.Medida.setText("")
        self.Folio.setText("0000")
        self.Almacenista.setCurrentText("---")
        self.Solicitante.setCurrentText("---")
        self.Fecha.setCurrentText("---")
        self.Motivo.setCurrentText("---")
        cargar_vales(self.TablaVales,"")
    def buscartabla(self):
        folio=self.Folio.text()
        clave=self.Clave.text()
        nombre=self.Nombre.text()
        medida=self.Medida.text()
        almacenista=self.Almacenista.currentText()
        solicitante=self.Solicitante.currentText()
        fecha=self.Fecha.currentText()
        motivo=self.Motivo.currentText()
        comando=""
        b=()
        a=""
        constructor=True
        if((clave=="0000" or clave=="000" or clave=="00" or clave=="0") and nombre=="" and medida=="" and almacenista=="---" and solicitante=="---" and fecha=="---" and motivo=="---" and clave==""):
            Error("Escribe bien la clave o borrala")
        elif(nombre=="" and medida=="" and almacenista=="---" and solicitante=="---" and fecha=="---" and motivo=="---" and clave=="" and (clave=="0000" or clave=="")):
            Error("¡¡Escriba algo!!")
            constructor=False
        elif("" != clave and nombre=="" and medida=="" and almacenista=="---" and solicitante=="---" and fecha=="---" and motivo=="---" and clave==""):
            a = "WHERE Clave = '{}'"
            comando=a.format(clave)
            constructor=False
        if(solicitante=="---"):
            solicitante=""
        if(fecha=="---"):
            fecha=""
        if(motivo=="---"):
            motivo=""
        if(almacenista=="---"):
            almacenista=""
        if(nombre!=""):
            if("WHERE" in a):
                a+=" AND Nombre LIKE '%{}%'"
                b+=(nombre,)
            else:
                a+="WHERE Nombre LIKE '%{}%'"
                b+=(nombre,)

        if(clave!=""):
            if("WHERE" in a):
                a+=" AND Clave LIKE '%{}%'"
                b+=(clave,)
            else:
                a+="WHERE Clave LIKE '%{}%'"
                b+=(clave,)

        if(medida!=""):
            if("WHERE" in a):
                a+=" AND Medida LIKE '%{}%'"
                b+=(medida,)
            else:
                a+="WHERE Medida LIKE '%{}%'"
                b+=(medida,) 
        
        if(folio!="" and folio!="0000"):
            if("WHERE" in a):
                a+=" AND Folio LIKE '%{}%'"
                b+=(folio,)
            else:
                a+="WHERE Folio LIKE '%{}%'"
                b+=(folio,)
        
        if(motivo!=""):
            if("WHERE" in a):
                a+=" AND Motivo LIKE '%{}%'"
                b+=(motivo,)
            else:
                a+="WHERE Motivo LIKE '%{}%'"
                b+=(motivo,) 
        
        if(almacenista!=""):
            if("WHERE" in a):
                a+=" AND Almacenista LIKE '%{}%'"
                b+=(almacenista,)
            else:
                a+="WHERE Almacenista LIKE '%{}%'"
                b+=(almacenista,) 
        
        if(solicitante!=""):
            if("WHERE" in a):
                a+=" AND Solicitante LIKE '%{}%'"
                b+=(solicitante,)
            else:
                a+="WHERE Solicitante LIKE '%{}%'"
                b+=(solicitante,)
        
        if(fecha!=""):
            if("WHERE" in a):
                a+=" AND Fecha LIKE '%{}%'"
                b+=(fecha,)
            else:
                a+="WHERE Fecha LIKE '%{}%'"
                b+=(fecha,)
        
        if constructor:
            comando=a.format(*(str(item) for item in b))
        cargar_vales(self.TablaVales,comando)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Historial()
    window.showMaximized()
    sys.exit(app.exec_())
