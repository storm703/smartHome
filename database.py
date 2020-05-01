from app import app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)

class ComponentDB(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(200), nullable = False)
    type = db.Column(db.String(200), nullable = False)

    def __repr__(self):
        return '<Component %r>' % self.id


def create():
    for i in range(10):
        comp = ComponentDB(name = "Rolladen in Zimmer %r" % i, type = "Shutter")
        db.session.add(comp)

    db.session.commit()


if __name__ == "__main__":
    create()
