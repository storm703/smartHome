from flask import Flask, render_template, redirect
from arduino import Arduino_Rolladen
import arduino_interface

app = Flask(__name__)

ards = [Arduino_Rolladen(0, "Wohnzimmer 1")]

@app.route('/')
def index():
    for a in ards:
        pass
        #a.update()
    return render_template('index.html', ards = ards)

@app.route('/open/<int:id>')
def open(id):
    #arduino_interface.set(id, 0)
    return redirect('/')

@app.route('/close/<int:id>')
def close(id):
    #arduino_interface.set(id, 100)
    return redirect('/')





if __name__ == "__main__":
    app.run(debug= True)
