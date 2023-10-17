from flask import Flask, render_template,url_for

app = Flask(__name__)


@app.route('/home')
@app.route('/')
def index():
    return render_template('index.html')   #С помощью render template у нас файл     будет скаться в index.html, который мы создали ранее


@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return f'User page: {name} - {str(id)}'


@app.route('/user2/<string:name>')
def user2(name):
    return f'User: {name}'


if __name__ == '__main__':
    app.run(debug = True)