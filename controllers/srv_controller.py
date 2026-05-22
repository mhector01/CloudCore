from models.database import Database
from models.hardware import HardwareMonitor

class ServidorController:
    def __init__(self):
        self.db = Database()
        self.hw = HardwareMonitor()
    
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
    
    def obtener_datos_dashboard(self):
        """Combina Inventario (DB) y Telemetría (Hardware)"""
        return{
            'servidores': self.obtener_inventario_completo(),
            'monitoreo': self.hw.obtener_metricas()
        }
    
    def registrar_auditoria(self, accion, descripcion):
        """ Método privado para generar bitacora de auditoría """
        sql = "INSERT INTO auditoria (tabla_afectada, accion, descripcion) VALUES (%s, %s, %s)"
        valores = ('infrastructura', accion, descripcion)
        self.db.ejecutar_query(sql, valores)

    
    def registrar_servidor(self, datos):
        """ Registra un nuevo servidor en la base de datos """
        sql_srv = "INSERT INTO servidores (hostname, direccion_ip, sistema_operativo) VALUES (%s, %s, %s)"
        valores_srv = (datos['hostname'], datos['ip'], datos['so'])

        if self.db.ejecutar_query(sql_srv, valores_srv):
            # Si el servidor se registra correctamente, también registramos la auditoría
            self.registrar_auditoria('INSERT', f"Alta de servidor {datos['hostname']} ({datos['ip']})")            
            return True
        return False