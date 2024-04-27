from .conexion_bd import conectar_bd

def colorearmin(clave):
    conexion = conectar_bd()
    if conexion is not None:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM `minimos` WHERE Clave= %s",(clave,))
        datos = cursor.fetchall()
        if datos: 
            conexion.close()
            return True
        else:
            False