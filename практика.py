from random import randint


class Man:
    def __init__(self,name):
        self.name = name
        self.fullness = 50
        self.food = 50
        self.money = 0

    def __str__(self):
        return ('я - {}, сытость {}, еды осталось {}, денег осталось {}'.format(
            self.name,self.fullness, self.food,  self.money ))

    def eat(self):
        if self.food > 10:
            print('{} поел'.format(self.name))
            self.fullness += 10
            self.food -= 10

        else:
            print('{} нет еды'.format(self.name))

    def work(self):
        print('{} сходил на работу '.format(self.name))
        self.money += 50
        self.fullness -= 20

    def plat_Dota(self):
        print('{}  играл в доту целый день '.format(self.name))
        self.fullness -= 10


    def act(self):
        dice = randint(1, 6)
        if dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.plat_Dota()

vasya = Man(name='Вася')
for day in range (1, 21):
    print('============= день ============'.format(day))
    vasya.act()
    print(vasya)