from flask import Flask, render_template, request, url_for, session, redirect

# Pre configuracion
app = Flask(__name__);
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'; # Llave secreta aleatoria para las sesioens

# Pagina principal
@app.route('/')
def index():
    
    # Validar si existe una secion activa
    if 'username' in session:
        return f'Welcome {session["username"]}';
    else:
        return 'You are not logged!';
    

# Pagina de logeo
@app.route('/login', methods = ['POST', 'GET'])
def login():
    
    # Validacion de datos de entrada con base de datos
    def ValidateDB(user, pw):
        if (user == 'Usuario1') & (pw == '1234'):
            return True;
        else:
            return False;

    if request.method == 'POST':    # Si los datos vienen de un formulario => Validarlos
        if res:=(ValidateDB(user=request.form['username'], pw = request.form['password'])) == True:
            # Si el usuario fue validado correctamente => Iniciar sesion
            session['username'] = request.form['username'];
            
            return redirect(url_for('index'));
    else:
        return render_template("login.html");

# Pagina para cerrar login
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(port=80, debug=True);