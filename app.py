from flask import Flask

app = Flask(__name__)

@app.route("/")
def curso():
    return "Ai zé da manga"

@app.route('/produtos')
def produto():
    return 'Minha página de produtos'