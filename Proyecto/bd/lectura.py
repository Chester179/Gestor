from PyQt5 import QtWidgets
from .conexion_bd import conectar_bd
from tools.tools import minmax
from tools.menu import getrango

def cargar_datos(TablaGastos,ext):
    conexion = conectar_bd()
    if conexion is not None:
        cursor = conexion.cursor()
        consulta="SELECT Clave, Nombre, Medida, U_Medida, Categoria, Descripcion, Cantidad FROM gastos {}".format(ext)
        cursor.execute(consulta)
        datos = cursor.fetchall()
        TablaGastos.setRowCount(0)
        for row_number, row_data in enumerate(datos):
            TablaGastos.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                TablaGastos.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            if getrango() != 0:
                minmax(TablaGastos,row_number)
        
        conexion.close()
    
def cargar_datosCambio(TablaGastos,ext):
    conexion = conectar_bd()
    if conexion is not None:
        cursor = conexion.cursor()
        consulta="SELECT Clave, Nombre, Medida, U_Medida, Categoria, Descripcion, Cantidad FROM gastos {}".format(ext)
        cursor.execute(consulta)
        datos = cursor.fetchall()
        TablaGastos.setRowCount(0)
        for row_number, row_data in enumerate(datos):
            TablaGastos.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                TablaGastos.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        conexion.close()
def cargar_datosUsuarios(TablaGastos,ext):
    conexion = conectar_bd()
    if conexion is not None:
        cursor = conexion.cursor()
        consulta="SELECT ID, Nombre, ApellidoP, ApellidoM, Telefono FROM usuarios {}".format(ext)
        cursor.execute(consulta)
        datos = cursor.fetchall()
        TablaGastos.setRowCount(0)
        for row_number, row_data in enumerate(datos):
            TablaGastos.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                TablaGastos.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        conexion.close()
def datos_opc(tema, ext,x):
    conexion = conectar_bd()
    z=""
    if x==1:
       z="gastos"
    elif x==2:
        z="vales"
    elif x==3:
        z="listasolicitantes"
    elif x==4:
        z="historialmovimientos"
    if conexion is not None:
        cursor = conexion.cursor()
        if(ext ==""):
            0
        elif "---" in ext :
            ext = ""
        # Utilizar comillas simples para los valores de cadena
        consulta = "SELECT DISTINCT {} FROM {} {}".format(tema,z, ext)
        cursor.execute(consulta)
        a = cursor.fetchall()
        conexion.close()
        return a
def cargar_vales(TablaGastos,ext):
    conexion = conectar_bd()
    if conexion is not None:
        cursor = conexion.cursor()
        cursor.execute("SELECT Folio, Clave, Nombre, Medida, Motivo, Almacenista, Solicitante, Salida, Fecha FROM vales {}".format(ext))
        datos = cursor.fetchall()
        TablaGastos.setRowCount(0)
        for row_number, row_data in enumerate(datos):
            TablaGastos.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                TablaGastos.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        conexion.close()
def cargar_movs(TablaGastos,ext):
    conexion = conectar_bd()
    if conexion is not None:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM historialmovimientos {}".format(ext))
        datos = cursor.fetchall()
        TablaGastos.setRowCount(0)
        for row_number, row_data in enumerate(datos):
            TablaGastos.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                TablaGastos.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        conexion.close()
def maxmin(clave):
    conexion = conectar_bd()
    if conexion is not None:
        cursor=conexion.cursor()
        comando="SELECT Max, Min FROM min_max WHERE Clave='{}'".format(clave)
        cursor.execute(comando)
        rows=cursor.fetchall()
        conexion.close()
        if rows:  
            return rows[0]
        else:
            return None 
def datosTabla(clave,x):
    conexion = conectar_bd()
    a=""
    z=""
    m=""
    if x==1:
        a="Nombre, Medida, Descripcion, Lugar, TipoMaterial, U_Medida, Categoria, Proveedor, IMG"
        z="gastos"
        m="Clave"
    elif x==2:
        a="Clave, Nombre, Medida, Motivo, Almacenista, Solicitante, Fecha"
        z="vales"
        m="Folio"
    elif x==3:
        a="ID, Usuario, Contrasena, NivelAutoridad, Nombre, ApellidoP, ApellidoM, Telefono, IMG"
        z="usuarios"
        m="ID"
    elif x==4:
        a="*"
        z="historialmovimientos"
        m="ID"
    elif x==5:
        a="Nombre, Medida"
        z="gastos"
        m="Clave"
    if conexion is not None:
        cursor = conexion.cursor()
        comando="SELECT {} FROM {} WHERE {} = '{}'".format(a,z,m,clave,)
        cursor.execute(comando)
        rows = cursor.fetchall()
        conexion.close()

        if rows:  
            return rows[0]
        else:
            if x==5:
                return ["",""]
            else:
                return None  

def log(user, passw):
    conexion = conectar_bd()
    if user == "" or passw == "": 
        return "b"
    elif conexion is not None:
        cursor = conexion.cursor()
        consulta = "SELECT NivelAutoridad FROM usuarios WHERE Usuario = '{}' AND Contrasena = '{}'".format(user, passw)
        cursor.execute(consulta)
        # Fetchone() obtiene la primera fila de resultados
        fila = cursor.fetchone()
        conexion.close()
        if fila:
            # Extraer el valor de NivelAutoridad de la fila
            nivel_autoridad = fila[0]
            return nivel_autoridad
        else:
            return "a"

        
    
    

def minimos(TablaMinimos):
    conexion = conectar_bd()
    if conexion is not None:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM `minimos`")
        datos = cursor.fetchall()
        TablaMinimos.setRowCount(0)
        for row_number, row_data in enumerate(datos):
            TablaMinimos.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                TablaMinimos.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        conexion.close()