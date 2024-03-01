from flask import Flask, render_template, redirect, request,  url_for, flash
from flask_bcrypt import Bcrypt


app = Flask(__name__)


@app.route('/')  # ruta principal
def base():
    # Redireccionar automáticamente desde la ruta principal ("/") a "/index"
    return redirect(url_for('index'))


@app.route('/index')  # ruta principal
def index():
    return render_template('index.html')


@app.route('/sobremi')  # ruta principal
def sobremi():
    return render_template('sobremi.html')


@app.route('/experiencia')  # ruta principal
def experiencia():
    return render_template('experiencia.html')


@app.route('/certificados')  # ruta principalc
def certificados():
    return render_template('certificados.html')


@app.route('/login')  # ruta principal
def login():
    return render_template('login.html')


bcrypt = Bcrypt(app)

# Lista para almacenar usuarios (en un entorno de producción, deberías usar una base de datos)
users = []


@app.route('/register', methods=['POST'])
def register():
    new_user = None  # Inicializar new_user para evitar el error de 'not defined'
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Verificar si el correo ya está registrado
        if any(user['email'] == email for user in users):
            flash('El correo ya está registrado. Por favor, inicia sesión.')
            return redirect(url_for('login'))

        # Hashear la contraseña antes de almacenarla
        hashed_password = bcrypt.generate_password_hash(
            password).decode('utf-8')

        # Almacenar usuario en la lista (en un entorno de producción, usar una base de datos)
        users.append({'email': email, 'password': hashed_password})
        users.append(new_user)

        flash('Registro exitoso. Por favor, inicia sesión.')
        return render_template('login.html', new_user=new_user)

        # return redirect(url_for('login'))


if __name__ == '__main__':
    app.secret_key = 'mysecretkey'  # Necesario para usar flash messages
    app.run(port=5000, debug=True)
