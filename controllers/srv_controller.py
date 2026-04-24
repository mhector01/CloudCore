from models.database import Database

class ServidorController:
    def __init__(self):
        self.db = Database()
    
    def obtener_inventario_completo(self):
        """Ejecuta el INNER JOIN para unir servidores"""
        conexion = self.db.conectar()
        if conexion:
            # dictionary=True facilita el manejo de datos en la vista posteriormente
            cursor = conexion.cursor(dictionary=True)
            query = """
                SELECT s.hostname, s.direccion_ip, s.sistema_operativo,
                       c.tipo, c.especificacion, c.capacidad_gb
                FROM servidores s
                INNER JOIN componentes c ON s.id_servidor = c.id_servidor
            """

            cursor.execute(query)
            resultados = cursor.fetchall()
            cursor.close()
            conexion.close()
            return resultados
        return []
    