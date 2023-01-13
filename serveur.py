from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/createur')
def createur():
    return render_template('createur.html')


if __name__ == "__main__":
    app.run(debug=True)