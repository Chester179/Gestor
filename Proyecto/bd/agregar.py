import mysql.connector
from .conexion_bd import conectar_bd
from tools.tools import Exito, Error, ObtenerFecha

def cargar_datos(nombre, caracteristicas, medida, unidad_Medida, proveedor, familia, maximo, minimo, imagen, cantidad):
    try:
        conexion = conectar_bd()
        if conexion is not None:
            cursor = conexion.cursor()

            consulta_select = "SELECT * FROM gastos WHERE Nombre = %s AND Categoria = %s AND Medida = %s AND U_Medida = %s"
            datos_select = (nombre, familia, medida, unidad_Medida)

            cursor.execute(consulta_select, datos_select)
            resultados = cursor.fetchall()

            if resultados:
                Error("Ya existe un registro con los mismos datos. No se realizará procesos.")
            else:
                cursor.execute("SELECT MAX(ID) FROM gastos")
                clave = int(cursor.fetchone()[0])+1
                clave=("GAST-"+'{:04d}'.format(clave))
                consulta_insert = "INSERT INTO gastos (Clave, Nombre, Medida, Categoria, U_Medida, Cantidad, Descripcion, Proveedor, IMG) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                datos_insert = (clave, nombre, medida, familia, unidad_Medida, cantidad, caracteristicas, proveedor, imagen)
                cursor.execute(consulta_insert, datos_insert)
                conexion.commit()
                maxmin(clave,maximo,minimo)
                msg = f"Se creó {nombre} con la medida de {medida} y un total de {cantidad}."
                Descripcion=f"Se creo la clave {clave} con la medida de {medida}{unidad_Medida} de la familia {familia}"
                Exito(msg)
                cargar_HistorialAcc(Descripcion, "Clave nueva de consumibles")

            cursor.close()
            conexion.close()

        else:
            Error("No se pudo establecer conexión con la base de datos.")

    except mysql.connector.Error as err:
        Error(f"Error al interactuar con la base de datos: {err}")

def maxmin(clave,maximo, minimo):
    try: 
        conexion = conectar_bd()
        if conexion is not None:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM min_max WHERE Clave = '{}'".format(clave))
            if cursor.fetchall():    
                consulta = "UPDATE `min_max` SET `Max`=%s,`Min`=%s WHERE Clave = %s"
                datos = (maximo,minimo,clave)
                cursor.execute(consulta,datos)
                conexion.commit()

        else:
            Error("No se pudo establecer conexión con la base de datos de máximos y mínimos.")
    except mysql.connector.Error as err:
        Error(f"Error al interactuar con la base de datos: {err}")
    cursor.close()
    conexion.close()



def anadir_datos(clave, proveedor, ingreso, Pedido, Folio):
    try:
        conexion = conectar_bd()
        if conexion is not None:
            cursor = conexion.cursor()

            consulta_select = "SELECT * FROM gastos WHERE Clave = %s"
            datos_select = (clave,)

            cursor.execute(consulta_select, datos_select)
            resultados1 = cursor.fetchall()
            
            consulta_select = "SELECT * FROM gastos WHERE Clave = %s AND Proveedor = %s"
            datos_select = (clave, proveedor)

            cursor.execute(consulta_select, datos_select)
            resultados = cursor.fetchall()

            if resultados1 and resultados:
                consulta_update = "UPDATE gastos SET Cantidad = Cantidad + %s WHERE Clave = %s AND Proveedor = %s"
                datos_update = (ingreso, clave, proveedor)
                cursor.execute(consulta_update, datos_update)
                conexion.commit()
                msg = f"Se agregó a {clave} la cantidad de {ingreso}."
                Descripcion=f"Se añadio la cantidad de {ingreso} Pza(s) a {clave}"
                Exito(msg)
                cargar_HistorialAcc(Descripcion, "Recepciòn de consumibles")
            elif resultados1:
                consulta_update = "UPDATE gastos SET Cantidad = Cantidad + %s, Proveedor = %s WHERE Clave = %s "
                datos_update = (ingreso, proveedor, clave)
                cursor.execute(consulta_update, datos_update)
                conexion.commit()
                msg = f"Se agregó a {clave} la cantidad de {ingreso} ."
                Descripcion=f"Se añadio la cantidad de {ingreso} Pza(s) a {clave} del proveedor {proveedor}\nPedido: {Pedido}\nFolio: {Folio}"
                Exito(msg)
                cargar_HistorialAcc(Descripcion, "Recepciòn de consumibles")
            else:
                Error("No se encontró la clave")

            cursor.close()
            conexion.close()

        else:
            Error("No se pudo establecer conexión con la base de datos.")

    except mysql.connector.Error as err:
        Error(f"Error al interactuar con la base de datos: {err}")

def agregarUsuarios(Usuario,Contrasena,Nivel,Nombre, ApeP, ApeM,Num, IMG):
    try:
        conexion = conectar_bd()
        if conexion is not None:
            cursor = conexion.cursor()

            consulta_select = "SELECT * FROM usuarios WHERE Usuario = %s"
            datos_select = (Usuario,)

            cursor.execute(consulta_select, datos_select)
            resultados = cursor.fetchall()

            if resultados:
                Error("Ya existe el usuario. Elige otro.")
            else:
                consulta_insert = "INSERT INTO `usuarios`(`Usuario`, `Nombre`, `ApellidoP`, `ApellidoM`, `Telefono`, `NivelAutoridad`, `Contrasena`, `IMG`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                datos_insert = (Usuario, Nombre, ApeP, ApeM, Num, Nivel, Contrasena, IMG)

                cursor.execute(consulta_insert, datos_insert)
                conexion.commit()
                msg = f"Felicidades {Nombre} se creo tu usuario {Usuario} con exito."
                Exito(msg)
                Descripcion=f"Se creo el usuario: {Usuario} de {Nombre} {ApeP} {ApeM}"
                cargar_HistorialAcc(Descripcion, "Crear usuario")
            cursor.close()
            conexion.close()

        else:
            Error("No se pudo establecer conexión con la base de datos.")

    except mysql.connector.Error as err:
        Error(f"Error al interactuar con la base de datos: {err}")




def cargar_HistorialAcc(Descripcion, Categoria):
    try:
        conexion = conectar_bd()
        if conexion is not None:
            cursor = conexion.cursor()
            Fecha=ObtenerFecha()
            consulta_insert = "INSERT INTO historialmovimientos (Descripcion, Categoria, Fecha) VALUES ( %s, %s, %s)"
            datos_insert = (Descripcion, Categoria, Fecha)
            cursor.execute(consulta_insert, datos_insert)
            conexion.commit()

            cursor.close()
            conexion.close()

        else:
            Error("No se pudo establecer conexión con la base de datos.")

    except mysql.connector.Error as err:
        Error(f"Error al interactuar con la base de datos: {err} \n En Historial de acciones")

def agregarcomentario(ID,Comentario):
    try:
        conexion = conectar_bd()
        if conexion is not None:
            cursor = conexion.cursor()
            consulta_insert = "UPDATE `historialmovimientos` SET `Observaciones`=%s WHERE ID=%s"
            
            datos_insert = (Comentario, ID)
            cursor.execute(consulta_insert, datos_insert)
            conexion.commit()
            Exito(f"Se agrego el comentario de {Comentario} con exito")
            cursor.close()
            conexion.close()

        else:
            Error("No se pudo establecer conexión con la base de datos.")

    except mysql.connector.Error as err:
        Error(f"Error al interactuar con la base de datos: {err} \n En Historial de acciones")