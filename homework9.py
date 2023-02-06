class Car:
    def __init__(self, model="unknown model", color="unknown color", engine=0, distBF = 0):
        self._model = model
        self._color = color
        self._engine = engine
        self._distBF = distBF #початкова дистанція по осі Вперед-Назад. 0 - вихідна точка, точка створення всесвіту
    def move_forward(self, dist=1):
        '''
        За замовченням рухаємось на 1 (одна одиниця відстані) вперед
        Але можемо вказати дистанцію яку треба проїхати вперед
        '''
        self._distBF += dist
    def move_back(self, dist=1):
        # опис як в попередньому методі
        self._distBF -= dist

    def get_distance(self):
        '''
        :return: Вертає рядок де вказано Попереду чи позаду ми від центру координат та пройдену дистанцію
        '''
        i = 1
        if self._distBF >= 0:
            position = "AHEAD"
        else:
            position = "BACK"
            i = -1
        return "We are "+position+" for: "+str(self._distBF*i)+' units'

class ExtendedCar(Car):
    def __init__(self, model="unknown model", color="unknown color", engine=0, distBF=0, distLR=0):
        Car.__init__(self, model, color, engine, distBF)
        self._distLR = distLR #опціонально можна вказати початкову дистанцію Ліво-Право. Плюсове число - право, мінусове - ліво
    def move_left(self, dist=1):
        #вліво -
        self._distLR -= dist
    def move_right(self, dist=1):
        #вправо +
        self._distLR += dist
    def get_distance(self):
        '''
        варінт реалізації з доповненням функції, викликаючи в унаслідуваному класі метод батьківського
        return: вертає  КООРДИНАТИ відносно центру координат, але в зрозумілому користувачу форматі
        '''
        j = 1
        if self._distLR >= 0:
            posLR = "RIGHT" #position LeftRight
        else:
            posLR = "LEFT"
            j = -1
        #Car.get_distance(self)
        return Car.get_distance(self)+"\n"\
                 "   and "+posLR+" for: "+str(self._distLR*j)+' units'


newcar = Car("4", "3", 3)
newcar1 = ExtendedCar("5","2",3)
newcar1.move_back(2)
newcar1.move_left(3)
newcar1.move_forward(3)
newcar1.move_back(5)

print(newcar1.get_distance())
