# весь файл - Тимофей
from PyQt5.QtGui import QImage


class Item:
    def __init__(self, title, price, description, icon):
        self.price = price
        self.title = title
        self.description = description
        self.icon = QImage(icon).scaled(110, 110)

    def __eq__(self, other):
        return self.title == other.title


peoplePack = Item('Группа наёмников', 75, 'Несколько наёмников, которых можно вызвать, когда понадобятся.',
                  "картинки/группа_людей.png")
knife = Item('Чёртов боевой нож', 40, 'Боевой нож будет давать вам небольшой бонус в бою.', "картинки/нож.png")
machineGun = Item('Чёртов пулемёт', 80, 'Пулемёт будет давать вам бонус в бою.', "картинки/пулемет.png")
tank = Item('Чёртов танк', 150, 'Танк будет давать вам большой бонус в бою.', "картинки/танк.png")
megaSword = Item('Величайший меч убиения всего и вся.', 250,
                 'Могущественнейший артефакт, из всех, что были когда-либо созданы. Возможности неизвестны.',
                 "картинки/величайший_меч.png")
radio = Item('Радио', 40, 'Обычное, не самое новое радио.', "картинки/радио.png")
flareGun = Item('Сигнальная ракетница', 30,
                'Сигнальная ракетница с несколькими ракетами разных цветов, ничего необычного.',
                "картинки/сигнальная_ракетница.png")

goods = [peoplePack, tank, machineGun, radio, flareGun, knife, megaSword]