from controllers.srv_controller import ServidorController
from flask import Flask, render_template, request, redirect

# Inicializamos el servidor web e indicamos que nuestras vistas están en la carpeta 'views'
app = Flask(__name__, template_folder='views')
controlador = ServidorController()

# Creamos nuestra primera ruta web (La página principal)
@app.route('/')

def index():
    # 1. El controlador pide los datos al modelo (MySQL)
    # datos = controlador.obtener_inventario_completo()
    # Cambio: Ahora pedimos el paquete completo DB + Hardware
    
    paquete_datos = controlador.obtener_datos_dashboard()

    # 2. Enviamos esos datos a nuestro archivo HTML
    return render_template('index.html',
                            servidores=paquete_datos['servidores'],
                            monitoreo=paquete_datos['monitoreo'])

# Nuevas rutas
@app.route('/registro')
def vista_registro():
    """ Muestra el formulario de registro de servidores """
    return render_template('registro.html')
    
@app.route('/guardar_servidor', methods=['POST'])
def guardar_servidor():
    """ Recibe el formulario y lo envia al controlador"""
    datos_formulario = {
        'hostname': request.form['hostname'],
        'ip': request.form['ip'],
        'so': request.form['so']
    }

    controlador.registrar_servidor(datos_formulario)
    return redirect('/')


if __name__ == "__main__":
    # Arrancamos el servidor en el puerto 5000
    print("Iniciando servidor web en http://127.0.0.1:5000")
    app.run(debug=True, port=5000)