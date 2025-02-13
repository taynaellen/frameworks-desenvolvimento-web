import os
from flask import Flask
from routes import index, class_list, aula1, aula2, aula3, aula4, aula5, aula6, aula7, aula8, aula9, aula10, aula11, aula12, aula13, aula14, aula15

app = Flask(__name__)
app.secret_key = os.urandom(24)

app.register_blueprint(index.bp)  
app.register_blueprint(class_list.class_list_bp) 
app.register_blueprint(aula1.aula1_bp)
app.register_blueprint(aula2.aula2_bp)
app.register_blueprint(aula3.aula3_bp)
app.register_blueprint(aula4.aula4_bp)
app.register_blueprint(aula5.aula5_bp)
app.register_blueprint(aula6.aula6_bp)
app.register_blueprint(aula7.aula7_bp)
app.register_blueprint(aula8.aula8_bp)
app.register_blueprint(aula9.aula9_bp)
app.register_blueprint(aula10.aula10_bp)
app.register_blueprint(aula11.aula11_bp)
app.register_blueprint(aula12.aula12_bp)
app.register_blueprint(aula13.aula13_bp)
app.register_blueprint(aula14.aula14_bp)
app.register_blueprint(aula15.aula15_bp)

if __name__ == '__main__':
    app.run(debug=True)
