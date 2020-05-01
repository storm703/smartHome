class Component():
    def __init__(self, ID, NAME):
        self.ID = ID
        self.NAME = NAME

    def toString(self):
        return self.ID + " " + self.NAME

    def update(self):
        pass



class Shutter(Component):
    def __init__(self, ID, NAME):
        self.ID = ID
        self.NAME = NAME
        self.closed = 0

    def update(self):
        # Get Status from Componetn
        self.closed = 0 #

    def set(self, c):
        # Set Shutter to c
        self.update()


class TempSensor(Component):
    pass

class RainSensor(Component):
    pass
