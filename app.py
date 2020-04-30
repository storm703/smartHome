from flask import Flask, render_template
from arduino import Arduino_Rolladen

app = Flask(__name__)

ard = [Arduino_Rolladen(0, "Wohnzimmer 1")]

@app.route('/')
def index():

    return render_template('index.html', array = ard)

if __name__ == "__main__":
    app.run(debug= True)
