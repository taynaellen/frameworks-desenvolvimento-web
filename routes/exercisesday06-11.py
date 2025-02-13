from flask import Flask, request, render_template_string, redirect, url_for, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'chave_secreta' 

USUARIO_FIXO = 'usuario'
SENHA_FIXA = 'senha123'

LIMITE_TENTATIVAS = 2

@app.route('/', methods=['GET', 'POST'])
def login():
    if 'tentativas' not in session:
        session['tentativas'] = 0
    
    if session['tentativas'] >= LIMITE_TENTATIVAS:
        return "Número máximo de tentativas atingido. Tente novamente mais tarde."
    
    if request.method == 'POST':
        usuario = request.form['username']
        senha = request.form['password']
        
        if usuario == USUARIO_FIXO and senha == SENHA_FIXA:
            session.pop('tentativas', None) 
            return redirect(url_for('bem_vindo'))
        else:
            session['tentativas'] += 1 
            return "Usuário ou senha incorretos. Tente novamente."

    return render_template_string('''
        <form method="POST">
            <label>Usuário: <input type="text" name="username"></label><br>
            <label>Senha: <input type="password" name="password"></label><br>
            <button type="submit">Entrar</button>
        </form>
        <p>Tentativas restantes: {{ restante }}</p>
    ''', restante=LIMITE_TENTATIVAS - session['tentativas'])


@app.route('/bem_vindo')
def bem_vindo():
    hora_atual = datetime.now().hour
    if 5 <= hora_atual < 12:
        saudacao = "Bom dia"
    elif 12 <= hora_atual < 18:
        saudacao = "Boa tarde"
    else:
        saudacao = "Boa noite"

    return f"{saudacao}! Bem-vindo ao sistema."


if __name__ == '__main__':
    app.run(debug=True)
