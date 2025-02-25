from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index/<title>')
def index(title='Заголовок страницы'):
    return render_template('base.html', title=title)

@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)

if __name__ == '__main__':
    app.run('127.0.0.1', 8080)
