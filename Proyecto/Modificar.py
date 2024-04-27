
        # Debo de rajustar el codigo para que se modifique automaticamente la llamada con like en la bd (boton Buscador)
        # ademas de investigar como guardar las img 
        # Crear la bd del historial de acciones
import sys
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QPushButton,QFileDialog, QMessageBox
from PyQt5.QtCore import Qt
from bd.lectura import cargar_datosCambio, datosTabla, datos_opc,maxmin
from bd.cambio import modificar
from tools.tools import *
from tools.menu import menu

xe=1

def setx(d):
    global xe
    xe=d
def getx():
    return xe
class Modificar(QMainWindow):
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
        self.TablaGastos.setGeometry(QtCore.QRect((screen_geometry.width()//25), ((screen_geometry.height()//2)+(screen_geometry.height()//18)+(screen_geometry.height()//911)), (screen_geometry.width()-screen_geometry.width()//11),(screen_geometry.height()//3)-(screen_geometry.height()//30)))
        self.TablaGastos.setObjectName("TablaGastos")
        self.TablaGastos.setColumnCount(7)
        self.TablaGastos.setRowCount(0)
        self.TablaGastos.setStyleSheet("background-color: lightgray;")
        x=(screen_geometry.width()-screen_geometry.width()//11)
        tamaños_filas = [((x//17)+(x//670)+(x//500)),((x//4)-(x//110)+(x//1000)),((x//17)+(x//670)+(x//1000)),((x//17)+(x//670)+(x//1000)),((x//17)+(x//670)+(x//500)),((x//2)-(x//13)-(x//500)),((x//17)+(x//670)+(x//1000))]  # Lista de tamaños de fila para cada fila en píxeles
        # Configurar los tamaños de fila
        for fila, tamaño in enumerate(tamaños_filas):
            self.TablaGastos.setColumnWidth(fila, tamaño)
        self.TablaGastos.setHorizontalHeaderLabels(["Clave","Nombre", "Medida", "UniMedida", "Familia","Descripción", "Existencia"])
        self.TablaGastos.cellClicked.connect(self.clikeo)
        self.titulo=Titulo(self.centralwidget,"Modificar consumibles",screen_geometry.width(),screen_geometry.height()//2)
        self.logo=logo(self.centralwidget, screen_geometry.width(), screen_geometry.height())
        self.botoninfo=botonInfo(self.centralwidget, screen_geometry.width(),screen_geometry.height())
        self.botoninfo.clicked.connect(Info)
        
        """"
        
                            Buscador y muestra de datos

        """
        # Definir button como un atributo de la clase
        self.button = QPushButton(self)
        self.set_button_icon("img/Icono.png")  # Ruta de la imagen de fondo
        self.button.clicked.connect(self.load_image)
        self.button.setGeometry(QtCore.QRect(50, 60, 240, 300))
        self.button.setObjectName("Herramienta")

        self.label = label(self.centralwidget, "Clave de consumible:", screen_geometry.width() // 4-screen_geometry.width() // 33-screen_geometry.width() //911, screen_geometry.height() // 12)
        self.Clave = editarTexto(self.centralwidget, screen_geometry.width()//3+screen_geometry.width()//25, screen_geometry.height() // 11)
        self.Clave.setText("GAST-0000")
        self.label = label(self.centralwidget, "Nombre de consumible:", screen_geometry.width() // 4-screen_geometry.width() // 33-screen_geometry.width() //911, (screen_geometry.height() // 7)-(screen_geometry.height() // 120))
        self.Nombre = editarTexto(self.centralwidget, screen_geometry.width()//3+screen_geometry.width()//25, screen_geometry.height() // 7)
        self.label = label(self.centralwidget, "Medida:", screen_geometry.width() // 4-screen_geometry.width() // 33-screen_geometry.width() //911, (screen_geometry.height() // 5)-(screen_geometry.height() // 100))
        self.Medida = editarTexto(self.centralwidget, screen_geometry.width()//3+screen_geometry.width()//25, (screen_geometry.height() // 5)-(screen_geometry.height() // 210))
        self.label = label(self.centralwidget, "Descripción:", screen_geometry.width() // 4-screen_geometry.width() // 33-screen_geometry.width() //911,(screen_geometry.height() // 3))
        self.Descripcion = cuadroTexto(self.centralwidget, screen_geometry.width()//3+screen_geometry.width()//25, ((screen_geometry.height() // 4)-(screen_geometry.height() // 308)))
        
        self.label = Subtitulo(self.centralwidget, "Especificaciones del consumible", screen_geometry.width() // 2+screen_geometry.width() // 10, screen_geometry.height() // 12)
        tema=datos_opc("Proveedor","",1)
        self.label = label(self.centralwidget, "Proovedor:", screen_geometry.width() // 2+screen_geometry.width() // 13, (screen_geometry.height() // 7)-(screen_geometry.height() // 120))
        self.Proveedor = opcmultipleE(self.centralwidget, screen_geometry.width()//2+screen_geometry.width()//5, (screen_geometry.height() // 7),tema)
        tema=datos_opc("Categoria","",1)
        self.label = label(self.centralwidget, "Familia:", screen_geometry.width() // 2+screen_geometry.width() // 13, (screen_geometry.height() // 5)-(screen_geometry.height() // 100))
        self.Familia = opcmultipleE(self.centralwidget, screen_geometry.width()//2+screen_geometry.width()//5, (screen_geometry.height() // 5)-(screen_geometry.height() // 210),tema)
        tema=datos_opc("TipoMaterial","",1)
        self.label = label(self.centralwidget, "Tipo de material:", screen_geometry.width() // 2+screen_geometry.width() // 13, (screen_geometry.height() // 4)-(screen_geometry.height() // 219))
        self.TipoMaterial = opcmultipleE(self.centralwidget, screen_geometry.width()//2+screen_geometry.width() // 5, (screen_geometry.height() // 4)-(screen_geometry.height() // 318),tema)
        tema=datos_opc("U_Medida","",1)
        self.label = label(self.centralwidget, "Unidad de Medida:", screen_geometry.width() // 2+screen_geometry.width() // 13, (screen_geometry.height() // 3)-(screen_geometry.height() // 30))
        self.Unidamedida = opcmultipleE(self.centralwidget, screen_geometry.width()//2+screen_geometry.width() // 5, (screen_geometry.height() // 4)+(screen_geometry.height()//20),tema)
        tema=datos_opc("Lugar","",1)
        self.label = label(self.centralwidget, "Ubicación:", screen_geometry.width() // 2+screen_geometry.width() // 13, (screen_geometry.height() // 3)+(screen_geometry.height() // 48))
        self.Lugar = opcmultipleE(self.centralwidget, screen_geometry.width()//2+screen_geometry.width() // 5, (screen_geometry.height() // 3)+(screen_geometry.height() // 56),tema)
        self.label = label(self.centralwidget, "Máximos:", screen_geometry.width() // 2+screen_geometry.width() // 13,((screen_geometry.height() // 3)+(screen_geometry.height() // 14)-(screen_geometry.height())//911))
        self.Maximo = editarTexto(self.centralwidget, screen_geometry.width()//2+screen_geometry.width() // 5, ((screen_geometry.height() // 3)+(screen_geometry.height() // 14)-(screen_geometry.height())//911))
        self.label = label(self.centralwidget, "Mínimos:", screen_geometry.width() // 2+screen_geometry.width() // 13,((screen_geometry.height() // 2)-(screen_geometry.height() // 22)-(screen_geometry.height())//911))
        self.Minimo = editarTexto(self.centralwidget, screen_geometry.width()//2+screen_geometry.width() // 5, ((screen_geometry.height() // 2)-(screen_geometry.height() // 22)-(screen_geometry.height())//911))
        
        
        
        self.boton = botonBuscar(self.centralwidget,screen_geometry.width()//13,(screen_geometry.height() // 2)-(screen_geometry.height() // 110),screen_geometry.width())
        self.limpiar = botonLimpiar(self.centralwidget,screen_geometry.width()//2+screen_geometry.width()//10,(screen_geometry.height() // 2)-(screen_geometry.height() // 110),screen_geometry.width())
        self.modificar = botonModificar(self.centralwidget,screen_geometry.width()//2-screen_geometry.width()//6+screen_geometry.width()//250,(screen_geometry.height() // 2)-(screen_geometry.height() // 110),screen_geometry.width())
        
        #################################################################################################
        #                                        ACIONES                                                #
        #################################################################################################
        self.Proveedor.activated.connect(self.opcion)
        self.Familia.activated.connect(self.opcion)
        self.TipoMaterial.activated.connect(self.opcion)
        self.Unidamedida.activated.connect(self.opcion)
        self.Lugar.activated.connect(self.opcion)
        self.modificar.clicked.connect(self.modificacion)
        self.boton.clicked.connect(self.buscartabla)
        self.limpiar.clicked.connect(self.limpia)
        #################################################################################################
        self.setCentralWidget(self.centralwidget)
        
        # Barra de menú y submenús
        menu(self,"Modificar consumibles")
        cargar_datosCambio(self.TablaGastos,"")


    def modificacion(self):   
            clave=self.Clave.text()
            nombre=self.Nombre.text()
            medida=self.Medida.text()
            descripcion=self.Descripcion.toPlainText()
            lugar=self.Lugar.currentText()
            material=self.TipoMaterial.currentText()
            umedida=self.Unidamedida.currentText()
            familia=self.Familia.currentText()
            maximo=self.Maximo.text()
            minimo=self.Minimo.text()
            # Crear un objeto QPixmap desde el botón para obtener la imagen
            pixmap = self.button.icon().pixmap(QtCore.QSize(250, 300))

            # Convertir la imagen a bytes
            byte_array = QtCore.QByteArray()
            buffer = QtCore.QBuffer(byte_array)
            buffer.open(QtCore.QIODevice.WriteOnly)
            pixmap.save(buffer, "PNG")  # Puedes elegir otro formato como JPG si lo deseas
            byte_array = byte_array.data()
            if clave:
                reply=SiNo()

                if reply == QMessageBox.Yes:
                    modificar(clave,nombre, medida,descripcion,lugar,material,umedida,familia,byte_array,maximo,minimo)

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



    def clikeo(self, row,column):
        item = self.TablaGastos.item(row, 0)
        a=str(item.text())
        setx(0)
        #       "a" es la variable que tiene la clave
        self.Clave.setText(str(a))
        
        Maximo, Minimo=maxmin(a)
        Nombre,Medida,Descripcion,Lugar,TipoMaterial,U_Medida,Categoria,Proveedor, imagen = datosTabla(a,1)
        self.Nombre.setText(str(Nombre))
        self.Medida.setText(str(Medida))
        self.Descripcion.setText(str(Descripcion))
        self.Lugar.setCurrentText(str(Lugar))
        self.TipoMaterial.setCurrentText(str(TipoMaterial))
        self.Unidamedida.setCurrentText(str(U_Medida))
        self.Familia.setCurrentText(str(Categoria))
        self.Proveedor.setCurrentText(str(Proveedor))
        self.Maximo.setText(str(Maximo))
        self.Minimo.setText(str(Minimo))     
        if imagen:

            self.pixmap.loadFromData(imagen)
            self.set_button_icon(self.pixmap)
            
        else:
            self.pixmap=QPixmap("img/Icono.png")
            self.set_button_icon(self.pixmap)
    def opcion(self):
        if getx()==1:     
            comando=""
            a=""
            familia="---"
            material="---"
            medida="---"
            lugar="---"
            proveedor="---"
            
            if self.Familia.currentText() != "---":
                if "WHERE" in comando:
                    a+=(self.Familia.currentText(),)
                    familia=self.Familia.currentText()
                    comando=comando+" AND Categoria = '{}'"
                else:
                    a=(self.Familia.currentText(),)
                    familia=self.Familia.currentText()
                    comando=comando+" WHERE Categoria = '{}'"
            
            if self.Proveedor.currentText() != "---":
                if "WHERE" in comando:
                    a+=(self.Proveedor.currentText(),)
                    proveedor=self.Proveedor.currentText()
                    comando=comando+" AND Proveedor = '{}'"
                else:
                    a=(self.Proveedor.currentText(),)
                    proveedor=self.Proveedor.currentText()
                    comando=comando+" WHERE Proveedor = '{}'"

            if self.TipoMaterial.currentText() != "---":
                if "WHERE" in comando:
                    a+=(self.TipoMaterial.currentText(),)
                    material=self.TipoMaterial.currentText()
                    comando=comando+" AND TipoMaterial = '{}'"
                else:
                    a=(self.TipoMaterial.currentText(),)
                    material=self.TipoMaterial.currentText()
                    comando=comando+" WHERE TipoMaterial = '{}'"
            
            if self.Unidamedida.currentText() != "---":
                if "WHERE" in comando:
                    a+=(self.Unidamedida.currentText(),)
                    medida=self.Unidamedida.currentText()
                    comando=comando+" AND U_Medida = '{}'"
                else:
                    a=(self.Unidamedida.currentText(),)
                    medida=self.Unidamedida.currentText()
                    comando=comando+" WHERE U_Medida = '{}'"
            
            if self.Lugar.currentText() != "---":
                if "WHERE" in comando:
                    a+=(self.Lugar.currentText(),)
                    lugar=self.Lugar.currentText()
                    comando=comando+" AND Lugar = '{}'"
                else:
                    a=(self.Lugar.currentText(),)
                    lugar=self.Lugar.currentText()
                    comando=comando+" WHERE Lugar = '{}'"
                    
            comando = comando.format(*(str(item) for item in a))
            tema=datos_opc("Categoria",comando,1)
            temas_str = ["---"]+[str(item[0]) for item in tema]
            self.Familia.clear()
            self.Familia.addItems(temas_str)
            self.Familia.setCurrentText(familia)
            tema=datos_opc("TipoMaterial",comando,1)
            temas_str = ["---"]+[str(item[0]) for item in tema]
            self.TipoMaterial.clear()
            self.TipoMaterial.addItems(temas_str)
            self.TipoMaterial.setCurrentText(material)
            tema=datos_opc("U_Medida",comando,1)
            temas_str = ["---"]+[str(item[0]) for item in tema]
            self.Unidamedida.clear()
            self.Unidamedida.addItems(temas_str)
            self.Unidamedida.setCurrentText(medida)
            tema=datos_opc("Lugar",comando,1)
            temas_str = ["---"]+[str(item[0]) for item in tema]
            self.Lugar.clear()
            self.Lugar.addItems(temas_str)
            self.Lugar.setCurrentText(lugar)
            tema=datos_opc("Proveedor",comando,1)
            temas_str = ["---"]+[str(item[0]) for item in tema]
            self.Proveedor.clear()
            self.Proveedor.addItems(temas_str)
            self.Proveedor.setCurrentText(proveedor)
            
        #####################################################################################
        #                          Buscador de tabla                                        #
        #####################################################################################
    def buscartabla(self):
        clave=self.Clave.text()
        nombre=self.Nombre.text()
        medida=self.Medida.text()
        descripcion=self.Descripcion.toPlainText()
        lugar=self.Lugar.currentText()
        material=self.TipoMaterial.currentText()
        umedida=self.Unidamedida.currentText()
        familia=self.Familia.currentText()
        proveedor=self.Proveedor.currentText()
        comando=""
        b=()
        a=""
        constructor=True
        if((clave=="GAST-000" or clave=="GAST-00" or clave=="GAST-0") and proveedor=="---" and nombre=="" and medida=="" and descripcion=="" and lugar=="---" and material=="---" and umedida=="---" and familia=="---"):
            Error("Escribe bien la clave o borrala")
        elif(nombre=="" and medida=="" and proveedor=="---" and descripcion=="" and lugar=="---" and material=="---" and umedida=="---" and familia=="---" and (clave=="GAST-0000" or clave=="")):
            Error("¡¡Escriba algo!!")
            constructor=False
        elif(nombre=="" and medida=="" and proveedor=="---" and descripcion!="" and lugar=="---" and material=="---" and umedida=="---" and familia=="---" and (clave=="GAST-0000" or clave=="")):
            a = "WHERE Clave LIKE '%{}%' OR Nombre LIKE '%{}%' OR Medida LIKE '%{}%' OR Categoria LIKE '%{}%' OR U_Medida LIKE '%{}%' OR Cantidad LIKE '%{}%' OR Proveedor LIKE '%{}%' OR Lugar LIKE '%{}%' OR TipoMaterial LIKE '%{}%' OR Descripcion LIKE '%{}%'"
            comando = a.format(descripcion, descripcion, descripcion, descripcion, descripcion, descripcion, descripcion, descripcion, descripcion, descripcion, descripcion)
            constructor=False
        elif("GAST-" in clave and nombre=="" and proveedor=="---" and medida=="" and descripcion=="" and lugar=="---" and material=="---" and umedida=="---" and familia=="---"):
            a = "WHERE Clave = '{}'"
            comando=a.format(clave)
            constructor=False
        if(lugar=="---"):
            lugar=""
        if(material=="---"):
            material=""
        if(umedida=="---"):
            umedida=""
        if(familia=="---"):
            familia=""
        if(proveedor=="---"):
            proveedor=""
        if(nombre!=""):
            if("WHERE" in a):
                a+=" AND Nombre LIKE '%{}%'"
                b+=(nombre,)
            else:
                a+="WHERE Nombre LIKE '%{}%'"
                b+=(nombre,)
        
        if(medida!=""):
            if("WHERE" in a):
                a+=" AND Medida LIKE '%{}%'"
                b+=(medida,)
            else:
                a+="WHERE Medida LIKE '%{}%'"
                b+=(medida,) 
        
        if(familia!=""):
            if("WHERE" in a):
                a+=" AND Categoria LIKE '%{}%'"
                b+=(familia,)
            else:
                a+="WHERE Categoria LIKE '%{}%'"
                b+=(familia,)
        
        if(umedida!=""):
            if("WHERE" in a):
                a+=" AND U_Medida LIKE '%{}%'"
                b+=(umedida,)
            else:
                a+="WHERE U_Medida LIKE '%{}%'"
                b+=(umedida,) 
        
        if(descripcion!=""):
            if("WHERE" in a):
                a+=" AND Descripcion LIKE '%{}%'"
                b+=(descripcion,)
            else:
                a+="WHERE Descripcion LIKE '%{}%'"
                b+=(descripcion,) 
        
        if(proveedor!=""):
            if("WHERE" in a):
                a+=" AND Proveedor LIKE '%{}%'"
                b+=(proveedor,)
            else:
                a+="WHERE Proveedor LIKE '%{}%'"
                b+=(proveedor,) 
        if(lugar!=""):
            if("WHERE" in a):
                a+=" AND Lugar LIKE '%{}%'"
                b+=(lugar,)
            else:
                a+="WHERE Lugar LIKE '%{}%'"
                b+=(lugar,)
        
        if(material!=""):
            if("WHERE" in a):
                a+=" AND TipoMaterial LIKE '%{}%'"
                b+=(material,)
            else:
                a+="WHERE TipoMaterial LIKE '%{}%'"
                b+=(material,)
        
        if constructor:
            comando=a.format(*(str(item) for item in b))
        
        cargar_datosCambio(self.TablaGastos,comando)
        #####################################################################################
        #                                   Limpia                                          #
        #####################################################################################
    def limpia(self):
        setx(1)
        self.Clave.setText("GAST-0000")
        self.Nombre.setText("")
        self.Medida.setText("")
        self.Descripcion.setText("")
        self.Maximo.setText("")
        self.Minimo.setText("")
        self.Lugar.setCurrentText("---")
        self.TipoMaterial.setCurrentText("---")
        self.Unidamedida.setCurrentText("---")
        self.Proveedor.setCurrentText("---")
        self.Familia.setCurrentText("---")
        cargar_datosCambio(self.TablaGastos,"")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Modificar()
    window.showMaximized()

    sys.exit(app.exec_())
