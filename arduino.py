import arduino_interface

class Arduino_Rolladen:

    def __init__(self, id,name ):
        self.ID = id
        self.NAME = name
        self.closed = 0 # 0 -> open, # 100 -> closed


    def update(self):
        self.closed = ardunino_interface.get(self.ID)

    def set_closed(self, p):
        ardunino_interface.set(self.ID, p)
        # ??? self.update()
