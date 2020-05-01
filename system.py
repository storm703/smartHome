from database import ComponentDB
from components import *

class System():
    def __init__(self, can_addr):
        self.list = []
        self.dict = {}
        comps = ComponentDB.query.order_by(ComponentDB.id).all()
        #dict = ["Shutter":[shutter1 shutter2], "TempSenor": [temp1, temp2]]
        #arr

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
