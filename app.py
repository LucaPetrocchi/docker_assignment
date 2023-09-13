from flask import (Flask, render_template)

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)