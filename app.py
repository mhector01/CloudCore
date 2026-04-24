from controllers.srv_controller import ServidorController
from flask import Flask, render_template

# Inicializamos el servidor web e indicamos que nuestras vistas están en la carpeta 'views'
app = Flask(__name__, template_folder='views')
controlador = ServidorController()

# Creamos nuestra primera ruta web (La página principal)
@app.route('/')

def index():
    # 1. El controlador pide los datos al modelo (MySQL)
    datos = controlador.obtener_inventario_completo()

    # 2. Enviamos esos datos a nuestro archivo HTML
    return render_template('index.html', servidores=datos)


if __name__ == "__main__":
    # Arrancamos el servidor en el puerto 5000
    print("Iniciando servidor web en http://127.0.0.1:5000")
    app.run(debug=True, port=5000)