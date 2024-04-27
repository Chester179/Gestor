import mysql.connector
import datetime
from tools.tools import Exito, Error
from .agregar import cargar_HistorialAcc
from vales.pruebatexto import vales
from .conexion_bd import conectar_bd

def salir_datos(Tabla, motivo, almacenista, solicitante):
    try:
        with conectar_bd() as conexion:
            if conexion is not None:
                cursor = conexion.cursor()
                cursor.execute("SELECT MAX(Folio) FROM vales")
                mensaje="" 
                nombres=()
                medidas=()
                cantidades=()
                fecha=""
                a=cursor.fetchone()[0]
                if a:
                    folio = a+1
                else:
                    folio=1
                for row in range(Tabla.rowCount()):
                    if Tabla.item(row, 0) is not None:
                        clave = Tabla.item(row, 0).text()
                        salida = Tabla.item(row, 1).text()
                        consulta_select = "SELECT Nombre, Medida FROM gastos WHERE Clave = %s AND Cantidad >= %s"
                        cursor.execute(consulta_select, (clave, salida))
                        resultado = cursor.fetchone()
                        if resultado:
                            nombre, medida = resultado
                            consulta_update = "UPDATE gastos SET Cantidad = Cantidad - %s WHERE Clave = %s"
                            cursor.execute(consulta_update, (salida, clave))
                            conexion.commit()

                            fecha = datetime.datetime.now().date()
                            consulta_insert = "INSERT INTO `vales` (`Folio`,`Clave`, `Nombre`, `Medida`, `Motivo`, `Almacenista`, `Solicitante`, `Salida`, `Fecha`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                            cursor.execute(consulta_insert, (folio, clave, nombre, medida, motivo, almacenista, solicitante, salida, fecha))
                            conexion.commit()
                            nombres+=(nombre,)
                            medidas+=(medida,)
                            cantidades+=(salida,)
                            mensaje += f"Se entregó {nombre} a {solicitante} la cantidad de {salida}"+"\n"

                        else:
                            Error(f"El {clave} no existe o no hay suficientes existencias")
                            break
                if cantidades== () and nombres == ():
                    Error("Escribe bien las claves o las cantidades")
                else:
                    vales(nombres, medidas, cantidades, fecha, almacenista, solicitante, folio, motivo)
                    Exito(mensaje)
                    cargar_HistorialAcc(mensaje, "Salida de consumibles")
            else:
                Error("No se pudo establecer conexión con la base de datos.")

    except mysql.connector.Error as err:
        Error(f"Error al interactuar con la base de datos: {err}")