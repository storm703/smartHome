from flask import Flask, render_template, redirect, request


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'



@app.route('/')
def index():
    return "Hallo World"
    """
    for a in ards:
        pass
        #a.update()
    return render_template('index.html', ards = ards)
    """

"""
@app.route('/open/<int:id>')
def open(id):
    #arduino_interface.set(id, 0)
    return redirect('/')

@app.route('/close/<int:id>')
def close(id):
    #arduino_interface.set(id, 100)
    return redirect('/')

@app.route('/set/<int:id>')
def set(id):
    p = int(request.args['p'])
    #arduino_inteface.set(id, p)
    return redirect('/')



"""


if __name__ == "__main__":
    app.run(debug= True)
