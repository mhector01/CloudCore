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