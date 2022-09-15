from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route('/')
def index():
    return("")

@app.route('/cheat/seat/<int:id>')
def cheat_host(id):
    return(render_template('cheat.html', id=id))


if __name__ == '__main__':
    app.run(port = 6789, debug = True)