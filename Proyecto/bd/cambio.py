import mysql.connector
from tools.tools import Exito, Error
from .agregar import cargar_HistorialAcc
from .conexion_bd import conectar_bd

def modificar(clave,nombre, medida,descripcion,lugar,material,umedida,familia,byte_array,maximo,minimo):
    try:
        with conectar_bd() as conexion:
            if conexion is not None:
                    cursor = conexion.cursor()
                    cursor.execute("UPDATE gastos SET Nombre = %s, Medida = %s, Categoria = %s, U_Medida = %s, Lugar = %s, TipoMaterial = %s, Descripcion = %s, IMG = %s WHERE Clave = %s", (nombre, medida,familia,umedida,lugar,material,descripcion,byte_array, clave))
                    conexion.commit()
                    cursor.execute("UPDATE min_max SET `Max`=%s,`Min`=%s WHERE Clave = %s", (maximo, minimo, clave))
                    conexion.commit()
                    Exito("Se realizo el cambio pedido")
                    #Se puede hacer mas certero.... pero es mucho show
                    Descripcion=f"Se realizo un cambio de información en el consumible {clave}"
                    cargar_HistorialAcc(Descripcion,"Cambio de información de consumibles")
            else:
                Error("No se pudo establecer conexión con la base de datos.")

    except mysql.connector.Error as err:
        Error(f"Error al interactuar con la base de datos: {err}")

def modificarUsuarios(id,Usuario,Contrasena,Nivel,Nombre, ApeP, ApeM,Num, img):
    try:
        with conectar_bd() as conexion:
            if conexion is not None:
                    cursor = conexion.cursor()
                    consulta_select = "SELECT * FROM usuarios WHERE ID = %s"
                    datos_select = (id,)
                    cursor.execute(consulta_select, datos_select)
                    resultados = cursor.fetchall()
                    
                    
                    if resultados:
                        consulta_select = "SELECT * FROM usuarios WHERE Usuario = %s"
                        datos_select = (Usuario,)
                        cursor.execute(consulta_select, datos_select)
                        resultados = cursor.fetchall()
                        if resultados:
                            cursor.execute("UPDATE usuarios SET Usuario = %s, Nombre = %s, ApellidoP = %s, ApellidoM = %s, Telefono = %s, NivelAutoridad = %s, Contrasena = %s, IMG = %s WHERE ID = %s", (Usuario,Nombre,ApeP,ApeM,Num,Nivel,Contrasena,img, id))
                            conexion.commit()
                            Descripcion=f"Se modifico los datos del {Usuario}"
                            Exito("Se genero el cambio correctamente")
                            cargar_HistorialAcc(Descripcion, "Modificar usuario")
                        else:
                             Error("Este usuario esta ocupado")
                    else:
                        Error("No se encuentra ese usuario")
            else:
                Error("No se pudo establecer conexión con la base de datos.")

    except mysql.connector.Error as err:
        Error(f"Error al interactuar con la base de datos: {err}")