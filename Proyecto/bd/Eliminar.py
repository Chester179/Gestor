import mysql.connector
from .conexion_bd import conectar_bd
from tools.tools import Exito, Error
from .agregar import cargar_HistorialAcc

def eliminar_datos(clave):
    try:
        conexion = conectar_bd()
        if conexion is not None:
            cursor = conexion.cursor()
            consulta_select = "SELECT * FROM gastos WHERE Clave = '{}'"
            datos_select = (clave)
            comando=consulta_select.format(datos_select)
            cursor.execute(comando)
            resultados = cursor.fetchall()

            if resultados:
                consulta_delete = "DELETE FROM `gastos` WHERE Clave = '{}'"
                datos_delete = (clave)
                comando=consulta_delete.format(datos_delete)
                cursor.execute(comando)
                conexion.commit()
                msg = f"Se elimino "+clave+" con exito."
                Descripción=f"Se elimino {clave}"
                Exito(msg)
                cargar_HistorialAcc(Descripción,"Eliminar consumible")
            else:
                Error(f"No existe la clave: "+clave)
            cursor.close()
            conexion.close()

        else:
            Error("No se pudo establecer conexión con la base de datos.")

    except mysql.connector.Error as err:
        Error(f"Error al interactuar con la base de datos: {err}")

def eliminarUsuarios(clave, usuario):
    try:
        conexion = conectar_bd()
        if conexion is not None:
            cursor = conexion.cursor()
            consulta_select = "SELECT * FROM usuarios WHERE ID = '{}'"
            datos_select = (clave)
            comando=consulta_select.format(datos_select)
            cursor.execute(comando)
            resultados = cursor.fetchall()

            if resultados:
                consulta_delete = "DELETE FROM `usuarios` WHERE ID = '{}'"
                datos_delete = (clave)
                comando=consulta_delete.format(datos_delete)
                cursor.execute(comando)
                conexion.commit()
                msg = f"Se elimino "+usuario+" con exito."
                Descripcion=f"Se elimino {usuario}"
                Exito(msg)
                cargar_HistorialAcc(Descripcion, "Eliminar usuario")
            else:
                Error(f"No existe el usuario: "+usuario)
            cursor.close()
            conexion.close()

        else:
            Error("No se pudo establecer conexión con la base de datos.")

    except mysql.connector.Error as err:
        Error(f"Error al interactuar con la base de datos: {err}")