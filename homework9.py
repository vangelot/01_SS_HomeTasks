class Car:
    def __init__(self, model="BMW", color="Blue", engine=2.5):
        self._model = model
        self._color = color
        self._engine = engine


newcar = Car("1", "3", 3)
newcar1 = Car()

newcar._model = "asd"

print(newcar._color)

newcar._color = 'white'

print(newcar._color)