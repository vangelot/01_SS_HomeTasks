import msvcrt as m
import os
import time
import sys
class Bespilotnik:
    def __init__(self, model = 'unknown', engine_amount = 1, camera_type = None, height = 0):
        self._model = model
        self._engine_amount = engine_amount
        self._camera_type = camera_type
        self._height = height
        self._BF = 0
        self._currentstaus = ''
    def print_intro(self):
        os.system('cls')
        print('Hello captain, your ship is under control, USE KEYS:\n\n' \
              '"q" - quit     "w" - move forward    "s" - move back   "l" - auto land   "h" - take height\n')
        print('YOUR CURRENT POSITION: ' + str(self.get_BF()) + "     HEIGHT = " + str(self.get_height()) + \
              self._currentstaus)
    def move_forward(self):
        if self._height > 0:
            self._BF += 1
        else:
            print("!!! we can't move, we are on the ground !!!")
    def move_back(self):
        if self._height > 0:
            self._BF -= 1
        else:
            print("!!! we can't move, we are on the ground !!!")
    def get_BF(self):
        return self._BF
    def get_height(self):
        return self._height

    def takeoff(self):
        if self.get_height() == 0:
            for i in range(5):
                self._height += 1
                print("!!! WAIT , taking height !!!")
                time.sleep(1)
                self.print_intro()
                print("!!! WAIT , taking height !!!")
            self.print_intro()
        else:
            print("!!! we can't takeoff, we are in the air !!!")
    def land(self):
        if self.get_height() > 0:
            for i in range(5):
                self._height -= 1
                print("!!! WAIT , landing !!!")
                time.sleep(1)
                self.print_intro()
                print("!!! WAIT , landing !!!")
            self.print_intro()
        else:
            print("!!! we can't land, we are on the ground !!!")

a = Bespilotnik()
a.print_intro()

while True:
    c = m.getch()
    a.print_intro()
    # print(ord(c))
    if ord(c) == 119:
        a.move_forward()
    elif ord(c) == 115:
        a.move_back()
    elif ord(c) == 108:
        a.land()
    elif ord(c) == 104:
        a.takeoff()
    elif ord(c) == 113:
        sys.exit()

