import psutil

class HardwareMonitor:
    def obtener_metricas(self):
        """Lee el estado real del hardware"""
        try:
            return {
                'cpu_uso': psutil.cpu_percent(interval=0.5),
                'ram_uso': psutil.virtual_memory().percent,
                'ram_total': round(psutil.virtual_memory().total / (1024**3),2),
                'disco_uso': psutil.disk_usage('/').percent
            }
        
        except Exception as e:
            print(f"Error al leer hardware: {e}")
            return None 