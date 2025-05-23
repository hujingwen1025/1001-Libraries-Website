from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/libraries')
def libraries():
    return render_template('libraries.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/join')
def join():
    return render_template('join.html')

@app.route('/fund')
def fund():
    return render_template('fund.html')

@app.route('/founding')
def founding():
    return render_template('founding.html')

@app.route('/nextlibrary')
def nextlibrary():
    return render_template('nextlibrary.html')

if __name__ == '__main__':
    app.run(debug=True, port=8085, host="0.0.0.0")