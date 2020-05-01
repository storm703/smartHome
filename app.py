from flask import Flask, render_template, redirect, request
from components import *
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)

class ComponentDB(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(200), nullable = False)
    type = db.Column(db.String(200), nullable = False)

    def __repr__(self):
        return '<Component %r>' % self.id

class System():
    def __init__(self, can_addr):
        self.list = []
        self.dict = {}
        comps = ComponentDB.query.order_by(ComponentDB.id).all()

        for comp in comps:
            print(comp.name + " " + comp.type)

            obj = None
            if comp.type == "Shutter":
                obj = Shutter(comp.id, comp.name)


            if obj is not None:
                self.list.append(obj)

                try:
                    self.dict[comp.type].append(obj)
                except KeyError:
                    self.dict[comp.type] = []

        print(list)
        print(dict)

    def updateAll(self):
        for c in self.list:
            c.update()


    def getByType(self, type):
        return self.dict[type]


    def getByID(self, id):
        for c in list:
            if c.ID == id:
                return c

        return None







s = System(("0.0.0.0", 700000))


@app.route('/')
def index():
    s.updateAll()
    return render_template('index.html', s = s)


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
