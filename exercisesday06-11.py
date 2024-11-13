from flask import Flask, request, render_template_string, redirect, url_for, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'chave_secreta'  # Necessário para gerenciar a sessão de forma segura

# Dados de autenticação fixos
USUARIO_FIXO = 'usuario'
SENHA_FIXA = 'senha123'

# Limite de tentativas de autenticação
LIMITE_TENTATIVAS = 2

# Página principal de login
@app.route('/', methods=['GET', 'POST'])
def login():
    # Inicializa as tentativas na sessão caso ainda não exista
    if 'tentativas' not in session:
        session['tentativas'] = 0
    
    # Verifica se o limite de tentativas foi atingido
    if session['tentativas'] >= LIMITE_TENTATIVAS:
        return "Número máximo de tentativas atingido. Tente novamente mais tarde."
    
    # Exibe a página de login e trata o envio do formulário
    if request.method == 'POST':
        usuario = request.form['username']
        senha = request.form['password']
        
        # Verifica se o usuário e a senha estão corretos
        if usuario == USUARIO_FIXO and senha == SENHA_FIXA:
            session.pop('tentativas', None)  # Reinicia o contador de tentativas
            return redirect(url_for('bem_vindo'))  # Redireciona para a página de boas-vindas
        else:
            session['tentativas'] += 1  # Incrementa o contador de tentativas
            return "Usuário ou senha incorretos. Tente novamente."

    # Página de login HTML básica
    return render_template_string('''
        <form method="POST">
            <label>Usuário: <input type="text" name="username"></label><br>
            <label>Senha: <input type="password" name="password"></label><br>
            <button type="submit">Entrar</button>
        </form>
        <p>Tentativas restantes: {{ restante }}</p>
    ''', restante=LIMITE_TENTATIVAS - session['tentativas'])

# Página de boas-vindas personalizada
@app.route('/bem_vindo')
def bem_vindo():
    # Gera a mensagem de boas-vindas com base no horário atual
    hora_atual = datetime.now().hour
    if 5 <= hora_atual < 12:
        saudacao = "Bom dia"
    elif 12 <= hora_atual < 18:
        saudacao = "Boa tarde"
    else:
        saudacao = "Boa noite"

    return f"{saudacao}! Bem-vindo ao sistema."

# Roda a aplicação Flask
if __name__ == '__main__':
    app.run(debug=True)
