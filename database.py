

from app import ComponentDB



def create():
    for i in range(10):
        comp = ComponentDB(name = "Rolladen in Zimmer %r" % i, type = "Shutter")
        db.session.add(comp)

    db.session.commit()


if __name__ == "__main__":
    create()
