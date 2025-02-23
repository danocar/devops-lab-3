from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<p>Hello, World!</p><p><a href="/about">Go to About Page</a></p>'

@app.route('/about')
def about():
    return '<p>This is a Flask web app running in a Linux VM.</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
