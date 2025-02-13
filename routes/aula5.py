from flask import Flask, Blueprint, render_template, request, redirect, url_for, session, jsonify
import json
import os
from datetime import datetime
import secrets

app = Flask(__name__)
app.secret_key = 'e6b4d9f7e3a243e9c5f8a1b0d3e2f7c8a4b6c1d2e5f9b3a7e8d1f2c6a5b4e9f0'

aula5_bp = Blueprint('aula5', __name__)

aula5_users = {'usuario': 'senha123'}

@aula5_bp.route('/aula5')
def aula5():
    return render_template('aula5.html')

@aula5_bp.route('/aula5/login', methods=['GET', 'POST'])
def aula5_login():
    if 'tentativas' not in session:
        session['tentativas'] = 0

    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        
        if usuario in aula5_users and aula5_users[usuario] == senha:
            hora_atual = datetime.now().hour
            saudacao = "Bom dia" if hora_atual < 12 else "Boa tarde" if hora_atual < 18 else "Boa noite"
            return f"{saudacao}, {usuario}! Login realizado com sucesso."
        
        session['tentativas'] += 1
        if session['tentativas'] >= 2:
            return "Erro! Você excedeu o número de tentativas."
        return "Usuário ou senha incorretos."
    
    return render_template('aula5_login.html', tentativas=session['tentativas'])

form_fields = ['nome', 'email', 'idade', 'telefone']

def gerar_template():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Formulário</title>
    </head>
    <body>
        <h1>Formulário</h1>
        <form action="/aula5/processar" method="POST">
    """
    for field in form_fields:
        html_content += f'<label for="{field}">{field.capitalize()}:</label> <input type="text" name="{field}" required><br>'
    html_content += '<input type="submit" value="Enviar"></form></body></html>'
    
    with open('templates/aula5_formulario.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

gerar_template()

@aula5_bp.route('/aula5/formulario')
def aula5_formulario():
    return render_template('aula5_formulario.html')

@aula5_bp.route('/aula5/processar', methods=['POST'])
def processar_formulario():
    dados = request.form.to_dict()
    return jsonify(list(dados.values()))


class Usuario:
    def __init__(self, nome, email, idade, telefone, senha):
        self.nome = nome
        self.email = email
        self.idade = idade
        self.telefone = telefone
        self.senha = senha

usuarios_registrados = {'admin': Usuario('Admin', 'admin@mail.com', 30, '99999999', 'admin123')}

@aula5_bp.route('/aula5/autenticar', methods=['GET', 'POST'])
def autenticar():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        if usuario in usuarios_registrados and usuarios_registrados[usuario].senha == senha:
            session['usuario'] = usuario
            return "Usuário autenticado com sucesso!"
        return "Falha na autenticação."
    return render_template('aula5_autenticar.html')

app.register_blueprint(aula5_bp)

if __name__ == '__main__':
    app.run(debug=True)
