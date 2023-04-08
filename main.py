from flask import Flask, request, render_template_string
# re sirve para las regular expressions
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        password1 = request.form['password1']
        password2 = request.form['password2']
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return "Dirección de email invalida"
        if password1 != password2:
            return "Las contraseñas no coinciden"
        if len(password1) < 12:
            return "La contraseña debe de ser al menos 12 caracteres"
        if not re.search(r"[A-Z]", password1):
            return "La contraseña debe de tener alguna letra en mayuscula"
        if not re.search(r"[a-z]", password1):
            return "La contraseña debe tener al menos una minuscula"
        if not re.search(r"[{}\[\]\-+.,()]", password1):
            return "La contraseña debe tener uno de los siguientes caracteres especiales: {,}, [,], -, +,. , (, )"
        if re.search(r"\s", password1):
            return "La contraseña no puede contener espacios"
        return "Email y password son validos"
    return render_template_string('''
    <form method="post">
        Email: <input type="email" name="email"><br>
        Contraseña: <input type="password" name="password1"><br>
        Confirmar contraseña: <input type="password" name="password2"><br>
        <input type="submit" value="Submit">
    </form>
    ''')

if __name__ == '__main__':
    app.run()