
import mysql.connector

def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",  # Reemplaza con tu nombre de usuario
            password="",  # Reemplaza con tu contraseña
            database="almacenrefacciones"
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"Error de conexión a la base de datos: {err}")
        return None
