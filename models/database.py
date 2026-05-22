import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        self.config = {
            'host': 'localhost',
            'user': 'root',
            'password': '',
            'database': 'cloudcore_db'
        }
    
    def conectar(self):
        """ Establece la conexion con MySQL"""
        try:
            conexion = mysql.connector.connect(**self.config)
            if conexion.is_connected():
                return conexion
        
        except Error as e:
            print(f"Error critico de conexión {e}")
            return None
        
    
    def ejecutar_query(self, query, params=None):
        """ Ejecuta sentencias INSERT, UPDATE, DELETE """
        conexion = self.conectar()
        if conexion:
            cursor = conexion.cursor()
            try:
                # Usamos params para evitar inyecciones SQL
                cursor.execute(query, params or ())
                conexion.commit() # vital para guardar cambios
                return True
            except Error as e:
                print(f"Error al ejecutar query: {e}")
                conexion.rollback() # Si hay errores, deshacemos la transacción
                return False            
            finally:
                cursor.close()
                conexion.close()