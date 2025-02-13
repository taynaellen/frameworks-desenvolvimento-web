from flask import Blueprint, render_template, request, redirect, url_for, jsonify

aula6_bp = Blueprint('aula6', __name__)

usuarios_mocados = {
    'usuario1': 'senha123',
    'usuario2': 'senha456'
}

tentativas_erradas = 0

@aula6_bp.route('/aula6')
def aula6():
    return render_template('aula6.html')


@aula6_bp.route('/aula6/formulario', methods=['GET', 'POST'])
def autenticar():
    global tentativas_erradas
    if request.method == 'POST':
        nome = request.form.get('nome')
        senha = request.form.get('senha')

        if not nome or not senha:
            return jsonify({'error': 'Nome e senha são obrigatórios'}), 400

        if nome in usuarios_mocados and usuarios_mocados[nome] == senha:
            return jsonify({'success': 'Autenticação bem-sucedida'}), 200
        else:
            tentativas_erradas += 1
            if tentativas_erradas >= 2:
                return jsonify({'error': 'Número máximo de tentativas erradas atingido'}), 401
            return jsonify({'error': 'Nome ou senha incorretos'}), 401

    return render_template('aula6_formulario.html')

