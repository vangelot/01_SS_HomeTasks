import msvcrt as m
import os
# import keyboard
import sys
class Bespilotnik:
    def __init__(self, model = 'unknown', engine_amount = 1, camera_type = None, height = 0):
        self._model = model
        self._engine_amount = engine_amount
        self._camera_type = camera_type
        self._height = height

    pass

a = m.getch()
# char = sys.stdin.read(1)
# print(char)
print('asdf')
# m.getch()
# print(a)

# while True:
#     if msvcrt.kbhit():
#         ch = msvcrt.getch()
#         if ch in '\x00\xe0':  # arrow or function key prefix?
#             ch = msvcrt.getch()  # second call returns the scan code
#         if ch == 'q':
#            print ("Q was pressed")
#         elif ch == 'x':
#            sys.exit()
#         else:
#            print ("Key Pressed:", ch)
os.system('cls')
print('hello')
