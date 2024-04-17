import sys
from random import choice as random
from random import random as chis
from random import randint as rand
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QErrorMessage, QPushButton
from PyQt5.QtGui import QPalette, QBrush, QIcon, QPixmap, QImage, QColor
from items import *
from guis import *


# Тимофей
class InventoryWindow(QWidget, Ui_Inventory):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # uic.loadUi('inventory.ui', self)
        self.content = []
        self.notShown = 1
        self.slots = []
        for i in range(3):
            for j in range(3):
                btn = QPushButton(self)
                btn.setFlat(True)
                btn.resize(120, 120)
                btn.move(10 + j * 120, 10 + i * 120)
                btn.setIconSize(QSize(110, 110))
                btn.setEnabled(False)
                self.slots.append(btn)

    def new(self):
        self.content = []
        self.notShown = 1
        for i in range(9):
            self.slots[i].setIcon(QIcon(QPixmap(110, 110).fill(QColor(225, 225, 225, 225))))

    def call(self):
        if self.notShown:
            self.show()
            self.notShown = 0
        else:
            self.notShown = 1
            self.close()

    def remake(self):
        for i in range(len(self.content)):
            self.slots[i].setIcon(QIcon(QPixmap(self.content[i].icon)))
            self.slots[i].setToolTip(self.content[i].title + '\n' + self.content[i].description)

    def remove(self, item):
        del self.content[self.content.index(item)]
        self.remake()

    def closeEvent(self, event):
        self.notShown = 1


# Тимофей
class PauseMenuWindow(QWidget, Ui_PauseMenu):
    def __init__(self, par):
        super().__init__()
        self.setupUi(self)
        # uic.loadUi('pause_menu.ui', self)
        self.par = par
        self.continueButton.clicked.connect(self.cont)
        self.gameExitButton.clicked.connect(self.closing)
        self.mainMenuExit.clicked.connect(self.exit_menu)
        self.newGameButton.clicked.connect(self.new_game)

    def cont(self):
        self.close()

    def new_game(self):
        self.close()
        self.par.start_resources()
        self.par.start()

    def exit_menu(self):
        self.par.par.show()
        self.par.close()
        self.close()

    def closing(self):
        self.par.close()
        self.close()

    def closeEvent(self, event):
        self.par.setEnabled(True)


# Тимофей
class MainMenuWindow(QMainWindow, Ui_MenuWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # uic.loadUi('menu_window.ui', self)
        image1 = QImage("картинки/бункер3.jpg").scaled(1000, 700)
        image2 = QImage("картинки/бункер4.jpg").scaled(1000, 700)
        image3 = QImage("картинки/бункер5.jpg").scaled(1000, 700)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(random([image1, image2, image3])))
        self.setPalette(palette)

        self.move(400, 150)
        self.gameExit.clicked.connect(self.close)
        self.continueButton.clicked.connect(self.continue_call)
        self.continueButton.hide()
        self.newGameButton.clicked.connect(self.new_game)

    def continue_call(self):
        pass

    def new_game(self):
        gameWindow = GameWindow(self)
        gameWindow.show()
        self.hide()

    def showEvent(self, event):
        self.move(400, 150)


class GameWindow(QMainWindow, Ui_GameWindow):
    # и Артём, и Тимофей
    def __init__(self, par, st=0):
        super().__init__()
        self.setupUi(self)
        self.move(400, 150)
        # uic.loadUi('game_window.ui', self)
        image = QImage("картинки/стена.jpeg").scaled(1000, 700)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(image))
        self.setPalette(palette)

        self.inventory = InventoryWindow()
        self.menu = PauseMenuWindow(self)
        self.par = par
        self.func = None

        self.btn = ''
        self.day = 0
        # список с событиями
        self.custom_events = new_event()
        # список событий из блокнота
        self.st = st
        # Переменная благодаря которой определяется на каком этапе сюжета человек
        self.people = 20
        self.food = 100
        self.money = 10
        self.last_custom_event = ''
        self.names = ["Боб", "Вася", "Алёша", "Петя", "Октовиан", "Богдан", "Гаврила", "Добрыня", "Маурицио",
                      "Ли Сянь", "Даичи", "Ын Дан О"]
        self.place = ['Склад', 'Стройка', 'Заброшенный бункер']
        # Случайные места для действий
        self.prize = ['еда', 'люди', 'деньги']
        # случайные призы
        self.tasks = [self.story, self.raid, self.raid, self.merchant, self.merchant, self.battle, self.strange_ending,
                      self.radio, self.meme_ending]
        self.foodtasks = [self.raid, self.battle, self.events, self.events]
        self.moneytasks = [self.merchant, self.merchant, self.events, self.events, self.story]
        # Шанс победы в битве
        self.chance = 0
        if len(self.custom_events) != 0:
            for i in range(7):
                self.tasks.append(self.events)
        self.menuButton.clicked.connect(self.menu_call)
        self.leftAnswer.clicked.connect(self.run)
        self.centralAnswer.clicked.connect(self.run)
        self.rightAnswer.clicked.connect(self.run)
        self.inventoryButton.clicked.connect(self.inventory.call)

    # Тимофей
    def closeEvent(self, event):
        self.inventory.close()

    # Тимофей
    def showEvent(self, event):
        self.move(400, 150)

    # Тимофей
    def text_changes(self, *txt, txt1='Продолжить', txt2='Продолжить', txt3='Продолжить'):
        self.leftAnswer.setText(txt1)
        self.centralAnswer.setText(txt2)
        self.rightAnswer.setText(txt3)
        if txt:
            self.mainQuestion.setText(txt[0])

    # Тимофей
    def start_resources(self):  # метод для обнуления ресурсов
        self.day = 0
        self.currentDay.setText(f'День {self.day}')
        self.btn = ''
        self.st = 0
        self.people = 20
        self.food = 100
        self.money = 10
        self.chance = 0
        self.names = ["Боб", "Вася", "Алёша", "Петя", "Октовиан", "Богдан", "Гаврила", "Добрыня", "Маурицио",
                      "Ли Сянь", "Даичи", "Ын Дан О"]
        self.tasks = [self.story, self.raid, self.raid, self.merchant, self.merchant, self.battle, self.strange_ending,
                      self.radio, self.meme_ending]
        self.inventory.new()
        if len(self.custom_events) != 0:
            for i in range(7):
                self.tasks.append(self.events)

    # и Артём, и Тимофей
    def run(self):
        self.number1.setText(f'{int(self.food)}')
        self.number2.setText(f'{int(self.people)}')
        self.number3.setText(f'{int(self.money)}')
        self.currentDay.setText(f'День {self.day}')
        if self.sender().text() == 'Начать' or self.sender().text() == 'Новая игра':
            # старт
            self.start()
        elif self.sender().text() == 'Продолжить':
            # промежуточное действие, чтобы продолжить игру
            # Случайный выбор следующего задания и ежедневного отнимания еды и прибавления дней
            if self.st < 4:
                # st от 4 до 12 - это концовки, поэтому нужна проверка на то, есть ли смысл продолжать
                if self.people <= 0:
                    self.peopleie()
                elif self.food <= 0:
                    self.foodie()
                elif self.money < 0:
                    self.moneyie()
                else:
                    if self.people > self.food:
                        self.people = self.food
                        self.food = 0
                    else:
                        self.food -= self.people
                    self.day += 1
                    if self.day < 10 and self.food <= self.people * 2:
                        a = random(self.foodtasks)
                        # print('self.foodtasks')
                    elif self.money >= 200:
                        a = random(self.moneytasks)
                        # print('self.moneytasks')
                    else:
                        a = random(self.tasks)
                        # print('self.tasks')
                    # print(a)
                    a()
            elif self.st >= 4:
                self.text_changes('Игра окончена.', txt1='Новая игра', txt2='Выйти в главное меню',
                                  txt3='Выйти из игры')
        elif self.sender().text() == 'Выйти из игры':
            self.close()
        elif self.sender().text() == 'Выйти в главное меню':
            self.close()
            self.par.show()
        else:
            # запуск проверки действий
            self.btn = self.sender().text()
            # Какая кнопка была нажата, результат
            self.func[0](1)
            # вызов последней функции для обработки результатоа
        self.number1.setText(f'{int(self.food)}')
        self.number2.setText(f'{int(self.people)}')
        self.number3.setText(f'{int(self.money)}')
        self.currentDay.setText(f'День {self.day}')

    # Тимофей
    def menu_call(self):
        self.setEnabled(False)
        self.menu.show()

    # Артём
    def start(self):
        self.start_resources()
        # рассказ истории
        self.text_changes('В тоталитарном государстве, империя Арстоцке, произошло крупное '
                          'восстание. В кои-то веки! Значит людям не так уж и неважно, что с '
                          'ними будет, они ищут лучшую, отличную от их жизнь. Ведь как можно '
                          'назвать это жизнью? Это существование в постоянном страхе, что тебя '
                          'отправят на каторгу, убьют, что ты станешь жертвой беспредела '
                          'корумпированных чиновников, что твои дети и внуки могут не дожить даже'
                          ' до 30. В этой стране безопасно и богато жили только высокопоставленные'
                          ' чиновники и военно-служащие. Рано или поздно всему этому должен был '
                          'наступить конец. Молодой революционер, боец по имени Джозеф Прэнтис '
                          'после двух лет службы в армии Арцтоцке решил прекратить все это безумие.'
                          ' Его лозунги о том, что этой стране нужен новый правитель, быстро '
                          'распространились среди людей. Сопротивление все росло и росло, пока '
                          'количество приверженцев Джозефа не достигло, по некоторым данным, трети '
                          'всего населения. Императору Питеру Хармс не нравилась все, что '
                          'происходило вокруг. О нем вообще мало что известно. Его не видел никто,'
                          ' кроме самых близких. О нем ходили легенды. Семья Хармс со своими '
                          'приближенными правит уже более ста лет! И Питеру не хотелось становиться'
                          ' последним правителем династии. Питер не впервые сталкивался с бунтом, '
                          'но в этот раз все складывалось уж слишком плохо для него. И вот после '
                          'недели мирных выступлений, стычки между двумя сторонами стали крайне '
                          'ожесточёнными. Больше сопротивление не хотело мира. Джозеф жаждал только'
                          ' крови Хармса. Параллельно с этим, оставшаяся часть мирного населения,'
                          ' которая не могла или не хотела бороться, ушла в горы. Беженцы хотели '
                          'спокойной жизни. Их устраивали все варианты, где в конце они оставались'
                          ' в живых. Поэтому они не поддерживали ни протестующих ни имперские силы.'
                          ' И вот вы со своими ближайшими знакомыми спрятались в бункере, который '
                          'вам достался в подарок при получении генеральского чина. Премии от '
                          'правительства здесь хоть и необычные, но зато практичные. Вы решили '
                          'спрятаться в бункере и не принимать до поры до времени ничью сторону. '
                          'Так и начинается ваша история. ')

    # Артем
    def radio(self, q=0):
        if q == 0:
            c = f'Попросить гуманитарную\nпомощь' if radio in self.inventory.content \
                else f'Нет доступных предметов\nдля использования.'
            r = f'Попросить эвакуацию' if radio in self.inventory.content \
                else f'Нет доступных предметов\nдля использования.'
            self.text_changes('Вы поймали радиосигнал из другой страны, вам предложили помощь. '
                              'Если бы у вас был передатчик, можно было бы попросить их о помощи',
                              txt1='Проигнорировать сигнал', txt2=c, txt3=r)
            self.func = [self.radio]
        else:
            if 'гуманитарную' in self.btn:
                self.mainQuestion.setText('Вы попросили помощи и самолет сбросил груз с едой и деньгами для вас')
                self.food += 400
                self.money += 200
                self.inventory.content.remove(radio)
            elif 'эвакуацию' in self.btn:
                self.mainQuestion.setText('Вы послали сигнал помощи и свои координаты отправителям того странного'
                                          ' радиосигнала. К вам прилетела летающая тарелка и забрала весь бункер'
                                          ' целиком. Неизвестно, куда вы летите и зачем...')
                self.st = 14
                self.inventory.content.remove(radio)
            else:
                self.mainQuestion.setText('Вы решили не заморачиваться')
            self.text_changes()

    # Артем
    def battle(self, q=0):
        if q == 0:
            self.chance = rand(20, 100)
            txt = ['У вас нет предмета, который мог бы помочь', 'Использовать наемников?']
            self.mainQuestion.setText(f'К вам в бункер постучался представитель группы рейдеров. Он сказал,'
                                      f' что надеется, на ваше благоразумие и вы предоставите им половину всех ваших '
                                      f'ресурсов, ведь иначе вам не сдобровать. Люди рейдеров - {self.chance}.'
                                      f' Ваши люди - {self.people}. Шанс на успех - '
                                      f'{(self.people / (self.people + self.chance - 5)) // 0.01}%.'
                                      f' Ваши действия?'
                                      f' {txt[1] if peoplePack in self.inventory.content else txt[0]}')
            r = f'Использовать предмет' if peoplePack in self.inventory.content \
                else f'Нет доступных предметов\nдля использования.\nСдаться'
            self.text_changes(txt1='Битва', txt2='Сдаться', txt3=r)
            self.func = [self.battle]
        else:
            if self.btn == 'Битва':
                if self.people >= rand(0, self.people + self.chance - 5):
                    self.mainQuestion.setText('В этот раз победа была на вашей стороне. Вы забрали все ресурсы рейдеров'
                                              ', но потеряли некоторое количество людей')
                    self.people -= self.people // rand(2, 20)
                    self.food += rand(self.chance, self.chance * 2)
                    self.money += rand(self.chance, self.chance * 2)
                else:
                    self.mainQuestion.setText('Вы проиграли и потеряли многое')
                    self.food //= 3
                    self.money //= 3
                    self.people = int(self.people * chis())
            elif 'Сдаться' in self.btn:
                self.mainQuestion.setText('Вы решили, что лучше обойтись без потерь и отдали половину ресурсов')
                self.food //= 2
                self.money //= 2
            else:
                self.mainQuestion.setText(f'Благодаря Группе наемников вы с легкостью победили в этой битве')
                self.food += rand(self.chance, self.chance * 2)
                self.money += rand(self.chance, self.chance * 2)
                self.inventory.content.remove(peoplePack)
            self.people = 0 if self.people < 0 else self.people
            self.food = 0 if self.food < 0 else self.food
            self.text_changes()

    # Артем и немного Тимофей
    def meme_ending(self, q=0):
        check1 = tank in self.inventory.content
        check2 = machineGun in self.inventory.content
        check3 = knife in self.inventory.content
        if q == 0:
            c = f'За повстанцев\nбольше чертовых вещей -\nвыше шанс на победу' if check1 or check2 or check3 \
                else 'У вас нет нужного\nпредмета.\nПропустить'
            r = f'За императора\nбольше чертовых вещей -\nвыше шанс на победу' if check1 or check2 or check3 \
                else 'У вас нет нужного\nпредмета.\nПропустить'
            self.text_changes('Завтра состоится крупнейшая битва повстанцев и империи. Настало ваше время'
                              ' принять чью-то сторону и поучаствовать в битве', txt1='Пропустить', txt2=c, txt3=r)
            self.func = [self.meme_ending]
        else:
            txt = ['С помощью танка вы смогли запросто уничтожить укрепления противника и заставить императора'
                   ' отступить. Враг явно не ожидал танка в вашем арсенале.',
                   'С помощью пулемета ваши люди сдерживали натиск армии Хармса. Никто не мог предсказать, '
                   'что у группировки несогласных с властью экстремистов будет машина для убийства, которая стреляет'
                   ' со скоростью 10000 выстрелов в минуту.',
                   'Вы зашли в кабинет Хармса. Он встретил вас хмурым взглядом в вашу сторону. Вы достали свой нож. '
                   'Нож был достаточно острым, чтобы отрубить голову человеку. Настало время публичной казни '
                   'предводителя. Вы лично убили его. Голова полетела с обрыва на радость публике.', '']
            a = 50
            if check1:
                a += 25
            if check2:
                a += 15
            if check3:
                a += 5
            r = rand(0, 100)
            if 'императора' in self.btn:
                if r < a:
                    self.mainQuestion.setText('Вы приняли сторону императора и победили.'
                                              'Все повстанцы были повешены. Династия Хармс будет править '
                                              'еще долгие века'
                                              'И никто не сможет их остановить. Вы внесли огромный вклад в победу.'
                                              'Повстанцы не считали вас своим противником, и вы, воспользовавшись этим,'
                                              'устроили саботаж. Идеальная координация саботажа и атаки имперцев '
                                              'сделали свое дело. У вас теперь есть привилегии ближайшего друга'
                                              ' императора.')
                    self.st = 12
                else:
                    self.mainQuestion.setText('Бой был изначально проигран. Повстанцы напали с тыла, застав всю армию'
                                              ' врасплох. Нападение имперцев было разбито, и они отступили. '
                                              'Благо вы успели убежать. ')
                if check1:
                    self.inventory.content.remove(tank)
                if check2:
                    self.inventory.content.remove(machineGun)
                if check2:
                    self.inventory.content.remove(knife)

            elif 'повстанцев' in self.btn:
                if r < a:
                    self.mainQuestion.setText('Вы приняли сторону повстанцев. Эта битва была крайне кровопролитной но '
                                              'вы общими усилиями с сопротивлением сумели победили. Ваш вклад в эту '
                                              'битву был колоссальным.  '
                                              f'{txt[1] if check2 else txt[3]}'
                                              f'{txt[0] if check1 else txt[3]}'
                                              'После полного прорыва обороны противника, вы зашли в главный штаб врага,'
                                              ' благодаря преимуществу в численности и огневой мощи.'
                                              ' Вы расстреляли всех неподчинившихся.'
                                              f'{txt[2] if check1 else txt[3]}'
                                              ' Теперь вы диктуете правила.'
                                              ' Теперь ваша очередь быть на высоте. Победу в этой войне одержали вы.'
                                              ' Но какой ценой? Судить об этом потомкам.')
                    self.st = 12
                else:
                    self.mainQuestion.setText('Вы приняли сторону повстанцев но проиграли. Вы успели сбежать и ничего'
                                              ' не потеряли')
                if check1:
                    self.inventory.content.remove(tank)
                if check2:
                    self.inventory.content.remove(machineGun)
                if check2:
                    self.inventory.content.remove(knife)
            else:
                self.mainQuestion.setText('Вы решили не заморачиваться')
            self.text_changes()

    # Артем
    def strange_ending(self, q=0):
        if q == 0:
            c = f'Использовать ракетницу\nдля гуманитарной помощи' if flareGun in self.inventory.content else \
                'У вас нет нужного\nпредмета.\nПропустить'
            r = f'Использовать ракетницу\nдля вызова эвакуации' if flareGun in self.inventory.content else \
                'У вас нет нужного\nпредмета.\nПропустить'
            self.text_changes('Сегодня идеальная ясная погода, если бы была сигнальная ракетница, '
                              'можно было бы вызвать подмогу', txt1='Пропустить', txt2=c, txt3=r)
            self.func = [self.strange_ending]
        else:
            if 'гуманитарной' in self.btn:
                self.mainQuestion.setText('Вы выстрелили из ракетницы и самолет сбросил груз с едой для вас')
                self.food += 500
                self.inventory.content.remove(flareGun)
            elif 'эвакуации' in self.btn:
                self.mainQuestion.setText('Вы выстрелили из ракетницы, когда вертолет пролетал недалеко от вас.'
                                          'Через час после этого к вам выслали несколько спасательных вертолетов и'
                                          ' забрали вас, после чего вас перенесли в пункт для беженцев. '
                                          'Тут вас обеспечивают едой и кровом. Вы будете дожидаться конца войны здесь')
                self.st = 14
            else:
                self.mainQuestion.setText('Вы решили не заморачиваться')
            self.text_changes()

    # Артём
    def foodie(self):
        self.st = 13
        self.text_changes('Еда закончилась, поэтому все люди ушли из убежища. Вы остались один и застрелились...')

    # Артём
    def moneyie(self):
        self.st = 13
        self.text_changes('Вы задолжали слишком многим людям. Как-то посреди ночи за вами пришли нужные люди. '
                          'Теперь у бункера новый хоязин.')

    # Артём
    def peopleie(self):
        self.st = 13
        self.text_changes('Все в бункере мертвы. И вы в том числе.')

    # Артём
    def story(self, q=0):
        # Главный сюжет
        if q == 0:
            # задания
            if self.st == 0:
                self.text_changes('К вам пришел отряд имперских войск и попросил временного убежища, они очень '
                                  'устали и хотят передохнуть. Широко известно, что вы бывший военнослужащий, и '
                                  'командир отряда надеется на вашу благосклонность.', txt1='Сражение',
                                  txt2='Пустить', txt3='Не пускать')

                self.func = [self.story]
            elif self.st == 1:
                self.text_changes('К вам пришли повстанцы и предложили свою помощь, так как узнали, что через день'
                                  ' на вас нападет пехота империи. Что будете делать?', txt1='Сражение',
                                  txt2='Принять помощь', txt3='Отказать')
                self.func = [self.story]
            elif self.st == 2:
                self.text_changes('Вы нашли странное устройство. Похоже оно осталось после того, как солдаты '
                                  'перекантовались у вас. Тут есть несколько кнопок. Но ваше внимание привлекает '
                                  'лишь красная кнопка, расположенная под пластиковой крышкой и зеленая кнопка, с '
                                  'номером телефона и надписью: “только в экстренных ситуациях”.', txt1='Сражение',
                                  txt2='Красная кнопка', txt3='Зеленая кнопка')
                self.func = [self.story]
            elif self.st == 3:
                self.text_changes('Вскоре сопротивление начало сдавать свои позиции и имперские войска перешли от'
                                  ' обороны к активному наступлению. Протестующие начали просить у вас прибежища.',
                                  txt1='Сражение', txt2='Пустить', txt3='Не пускать')
                self.func = [self.story]
        else:
            # Обработка результатов
            if self.st == 0:
                if self.btn == 'Сражение':
                    if self.people > 10:
                        self.mainQuestion.setText('Вы решили, что террор имперцев должен закончиться.'
                                                  ' Вы вступаете в сражение и с легкостью победили уставший отряд.'
                                                  ' Но несколько человек сбежало.'
                                                  ' Возможно в будущем из-за этого будут проблемы')
                        self.people -= 10
                        self.st = 1
                    else:
                        self.mainQuestion.setText('Вы проиграли. Похоже вам "НЕ ХВАТИЛО ЛЮДЕЙ".'
                                                  ' *Агрессивное подмигивание*')
                        self.st = 13
                elif self.btn == 'Пустить':
                    self.mainQuestion.setText('Вы пустили их на одну ночь после чего они ушли, пообещав вам орден.'
                                              ' Теперь повстанцы на вас косо смотрят,'
                                              ' пока вы пьете утренний кофе у входа в бункер.')
                    self.st = 2
                elif self.btn == 'Не пускать':
                    self.mainQuestion.setText('Вы проигнорировали их просьбу и сделали вид будто в бункере никого нет.'
                                              ' Растроенные имперцы пошли дальше искать убежища.'
                                              ' Повстанцы же теперь предлагают присоединиться к ним.'
                                              ' Но вы придерживаетесь нейтралитета и отказываетесь от их предложения.')
                    self.st = 3
            elif self.st == 1:
                if self.btn == 'Сражение':
                    if self.people > 10:
                        self.mainQuestion.setText('Вам были противны повстанцы и вся их идеалогия, неистребимое '
                                                  'упорство. Вы перебили их всех до единого. На следующий день '
                                                  'как и обещали повстанцы к вам пришел большой отряд'
                                                  ' имперцев, а так как вы не были ни под чьей защитой,'
                                                  ' вас всех перебили и забрали бункер, хоть вы и бились как герой.'
                                                  ' Повстанцы же в той войне пали. У них не было и шанса.'
                                                  ' Отчасти благодаря вам. Вам следует сходить к психологу.'
                                                  ' Убивать всех направо и налево не лучшая идея.'
                                                  ' Обдумайте это предложение\nАх да, нужно продолжить историю.'
                                                  ' И восторжествовал флаг Арцтоцке! А вы могли бы это предотвратить!')
                        self.st = 4
                        self.people -= 10
                    else:
                        self.mainQuestion.setText('Вы проиграли. Похоже вам "НЕ ХВАТИЛО ЛЮДЕЙ".'
                                                  ' *Агрессивное подмигивание*')
                        self.st = 13
                elif self.btn == 'Принять помощь':
                    self.mainQuestion.setText('Вы подумали, что отказываться от помощи просто глупо, и приняли помощь.'
                                              ' Через некоторое время и правда пришел большой отряд военных.'
                                              ' Противник явно не ожидал того, что на защиту бункера встанут повстанцы'
                                              ' После чего все узнали, что бункер "Константинополь" присоединился'
                                              ' к сопротивлению!.'
                                              ' Бункер был важной стратегической точкой, и благодаря этому повстанцы '
                                              'смогли выиграть войну.'
                                              ' В живых осталось меньше трети населения.'
                                              ' Но настала новая эра в истории Арцтоцки. Вы стали новым праивтелем.'
                                              ' Теперь гражданам страны не следует опасаться за свои жизни!'
                                              ' Отныне империя Арцтоцке является республикой Арцтоцке!'
                                              ' Да здравствует первый президент новой демократической Арстоцке!')
                    self.st = 5
                elif self.btn == 'Отказать':
                    self.mainQuestion.setText('Через некоторое время к вам заявился большой отряд имперцев,'
                                              ' но вы не смогли противостоять им. Вас всех убили.'
                                              ' Не стоило быть таким вредным. Да ведь?'
                                              ' Вскоре повстанцы из-за численного преимущества всё-таки'
                                              ' смогли уничтожить армию имперцев. Смогли захватить власть в стране,'
                                              ' так и не найдя Питера Хармса. А вы так и не дожили до этого момента,'
                                              ' мистер вредина.'
                                              ' Но в живых осталась лишь крайне небольшая часть населения,'
                                              ' измученная долгой войной. Оставшиеся силы не смогли сопративляться'
                                              ' вторжению других стран. Арстоцке была разделена между соседями,'
                                              ' став марионеточным государством.\n'
                                              ' Как хорошо, что вы умерли задолго до того, как это случилось,'
                                              ' не правда ли?)')
                    self.st = 6
            elif self.st == 2:
                if self.btn == 'Сражение':
                    self.mainQuestion.setText('Я конечно извиняюсь, но то есть вы без'
                                              ' шуток собираетесь сражаться с пультом?'
                                              '\nНу ладно, что ж.....\nРаз уж так хотите...\nЭто была сложная битва.'
                                              'Многие погибли, а пульт был повержен одной точной ногой,'
                                              ' которая наступила на него. А если серьезно,'
                                              ' то вы просто раздавили пульт неизвестно зачем. '
                                              'Вскоре правительство с легкостью подавило сопротивление.'
                                              ' Вы были награждены почетным орденом империи и познакомились с самим'
                                              ' императором Хармсом и стали его приближенным. После чего все люди в'
                                              ' Арцтоцке, запуганные властями, подчинились. Арцтоцке удалось '
                                              'реабилитироваться после смуты и в конце концов захватить весь мир.')
                    self.st = 7
                elif self.btn == 'Красная кнопка':
                    self.mainQuestion.setText('Из устройства раздался голос: “Подтвердите удар, мистер Хармс”.'
                                              ' Вы не задумываясь ответили, что подтверждаете, а зря.'
                                              ' Небо озарилось в рыжий цвет, вы можете отчетливо видеть через камеру'
                                              ' расположенную вне бункера след от ракеты, летящей прямо в вашу сторону.'
                                              ' Вы сразу осознали, что у вас в бункере побывал никто'
                                              ' иной как Питер Хармс! Вы выжили вместе с теми, кто находился в бункере,'
                                              ' но все, кто был снаружи, мертвы.'
                                              ' Покрыты красивым грибком от бомбы в 20 мегатонн!'
                                              ' Этого стоило ожидать. Вы же не думали, что большая красная кнопка,'
                                              ' за пластиковой крышкой на пульте имперцев будет автоматически'
                                              ' выдавать розы?)')
                    self.st = 8
                elif self.btn == 'Зеленая кнопка':
                    self.mainQuestion.setText('Из устройства раздался приятный женский голос:'
                                              ' “Здравствуйте, Мистер Хармс, с вами говорит представитель президента'
                                              ' объединенных островов чего вы хотели?”. Арцтоцке уже более 20 лет ведет'
                                              ' войну с Объединенными островами. Поэтому вы, обрадовавшись,'
                                              ' рассказали о ситуации внутри страны. И острова напали на Арцтоцке '
                                              'менее через неделю. Армия Арстоцке не смогли биться на два фронта,'
                                              ' и вскоре правительство заявило о своей капитуляции. Теперь в '
                                              'стране наступила демократия. Под контролем Объединенных островов, '
                                              'правда, но это же не так важно.\n'
                                              'Вы уехали как можно дальше из Арцтоцке,'
                                              ' чтобы не вспоминать все те ужасы,'
                                              ' что вам пришлось пережить.')
                    self.st = 9
            elif self.st == 3:
                if self.btn == 'Сражение':
                    if self.people > 10:
                        self.mainQuestion.setText(' Вы решили, что раз сопротивление все равно проигрывает,'
                                                  ' почему бы не сразиться, вдруг получите какие-то награды после '
                                                  'победы Империи.\n'
                                                  'Все повстанцы мертвы.'
                                                  ' Поэтому было принято решение вступить в ряды армии империи'
                                                  ' и добить сопротивление.\n'
                                                  'После войны вы стали почетным гражданином Арцтоцке и безмятежно '
                                                  'дожили свои дни в большом особняке на участке в 10 гектаров '
                                                  'недалеко от столицы!')
                        self.people -= 10
                        self.st = 10
                    else:
                        self.mainQuestion.setText('Вы проиграли. Похоже вам "НЕ ХВАТИЛО ЛЮДЕЙ".'
                                                  ' *Агрессивное подмигивание*')
                        self.st = 13
                elif self.btn == 'Пустить':
                    self.mainQuestion.setText('Вы приняли всех, они рассказали вам о том, что планируют сделать рывок'
                                              ' и вырваться за границы, пока не поздно.\n Вы согласились с ними.'
                                              ' Так как основные силы были отвлечены на защиту поместий аристократии'
                                              ' и высокопоставленных чиновников, ваш отряд вместе с теми повстанцами'
                                              ' прорвал оборону на границе и выбрался наружу,'
                                              ' оставив арцтоцке на произвол судьбы.')
                    self.people += 100
                    self.st = 11
                elif self.btn == 'Не пускать':
                    self.mainQuestion.setText('Вы отказали. Сопротивление прорвалось за стены и запросило'
                                              ' подкрепление извне. Битва будет все продолжаться и продолжаться'
                                              ' и вряд ли когда-нибудь закончится.\n Вы тут надолго...')
                    self.st = -1
                    self.tasks.remove(self.story)
            self.people = 0 if self.people < 0 else self.people
            self.food = 0 if self.food < 0 else self.food
            self.text_changes()

    # Артём
    def raid(self, q=0):
        # Задача
        if q == 0:
            self.text_changes(f'Ваши разведчики нашли недалеко от вашего убежища {random(self.place)}, '
                              f'что будете делать?', txt1='Рейд большим отрядом\n(50% людей)',
                              txt2='Рейд маленьким отрядом\n(30% людей)', txt3='Ничего')
            self.func = [self.raid]
            # обработка реакции пользователя
        if q == 1:
            # большой - 70%, маленький - 50% на успех
            if self.btn == 'Рейд большим отрядом\n(50% людей)' \
                    or self.btn == 'Рейд маленьким отрядом\n(30% людей)':
                if chis() > 0.5 if self.btn == 'Рейд большим отрядом\n(50% людей)' else chis() > 0.7:
                    chance = 0.3 if self.btn == 'Рейд маленьким отрядом\n(30% людей)' else 0.5
                    if self.food <= self.people * 2:
                        priz = ['еда', rand(40, 150), int(self.people * chance * chis())]
                    else:
                        priz = [random(self.prize), rand(10, 150), int(self.people * chance * chis())]
                    # обработка того, сколько и чего нашли и скольких потеряли
                    if priz[0] == 'еда':
                        self.food += priz[1]
                    elif priz[0] == 'деньги':
                        self.money += priz[1]
                    elif priz[0] == 'люди':
                        priz[1] = priz[1] // 3
                        self.people += priz[1]
                    # зачисление призов
                    self.people -= priz[2]
                    self.mainQuestion.setText(f'Вы нашли {priz[0]} в количестве {int(priz[1])},'
                                              f' но потеряли {int(priz[2])} человек')
                else:
                    self.mainQuestion.setText('До вас дошли сведения, что там находилась засада, и всех убили')
                    self.people = int(0.5 * self.people) if self.btn == 'Рейд большим отрядом\n(50% людей)' \
                        else int(0.7 * self.people)
                    # При провале
            else:
                self.mainQuestion.setText(f'Вы решили не рисковать')
            self.people = 0 if self.people < 0 else self.people
            self.food = 0 if self.food < 0 else self.food
            self.text_changes()

    # Артём
    def events(self, q=0):
        if q == 0:
            event = random(self.custom_events)
            event[1][0] = event[1][0].replace('\ n', '\n')
            event[2][0] = event[2][0].replace('\ n', '\n')
            event[3][0] = event[3][0].replace('\ n', '\n')
            self.text_changes(event[0], txt1=event[1][0], txt2=event[2][0], txt3=event[3][0])
            self.func = [self.events]
            self.last_custom_event = event
        if q == 1:
            event = self.last_custom_event
            if event[1][0] == self.btn:
                eve = event[1]
            elif event[2][0] == self.btn:
                eve = event[2]
            elif event[3][0] == self.btn:
                eve = event[3]
            event = sorted(eve[1], key=lambda x: x[2])
            number = rand(0, sum([int(i[2]) for i in event]))
            all = 0
            for i in range(len(event)):
                # print(int(event[i][2]) + all, number)
                if int(event[i][2]) + all >= number:
                    self.mainQuestion.setText(event[i][0])
                    self.food += int(event[i][1].split()[0])
                    self.people += int(event[i][1].split()[1])
                    self.money += int(event[i][1].split()[2])
                    break
                else:
                    all += int(event[i][2])
            self.people = 0 if self.people < 0 else self.people
            self.food = 0 if self.food < 0 else self.food
            self.text_changes()

    # Тимофей
    def merchant(self, q=0):
        if q == 0:
            self.name = random(self.names)
            self.item = goods.pop(rand(0, len(goods) - 1))
            self.text_changes(f'К вашему бункеру пришёл торговец {self.name}. '
                              f'{self.name} предлагает "{self.item.title}" за {self.item.price}.',
                              txt1='Купить', txt2='Отказаться', txt3='Напасть')
            self.func = [self.merchant]
        else:
            r = rand(0, 100)
            if self.btn == 'Купить':
                if self.money >= self.item.price:
                    if len(self.inventory.content) < 9:
                        if r < 90:
                            self.inventory.content.append(self.item)
                            self.inventory.remake()
                            self.mainQuestion.setText('Сделка удачно совершена. \nПроверьте инвентарь,'
                                                      ' чтобы узнать о предмете больше.')
                        elif r < 95:
                            del self.names[self.names.index(self.name)]
                            self.mainQuestion.setText('Торговец обманул вас и убежал, забрав деньги. '
                                                      'Теперь вы его вряд ли когда-нибудь увидите.')
                        else:
                            self.inventory.content.append(self.item)
                            self.inventory.remake()
                            self.money += 10
                            self.mainQuestion.setText('Сделка удачно совершена. И торговец двже не заметил,'
                                                      ' что вы дали ему немного меньше, чем нужно было.\n'
                                                      'Проверьте инвентарь, чтобы узнать о предмете больше')
                        self.money -= self.item.price
                        self.text_changes()
                    else:
                        QErrorMessage(self).showMessage('Не хватает места в инвентаре')
                else:
                    QErrorMessage(self).showMessage('Не хватает денег')
            elif self.btn == 'Отказаться':
                if r < 90:
                    self.mainQuestion.setText(f'{self.name} просто ушёл.')
                else:
                    self.mainQuestion.setText(f'{self.name} был так взбешён, что убил одного человека.'
                                              ' Теперь вы его вряд ли когда-нибудь увидите.')
                    self.people -= 1
                    del self.names[self.names.index(self.name)]
                self.text_changes()
            else:
                if r < 50:
                    self.mainQuestion.setText(f'Почуяв что-то неладное, {self.name} сразу убежал. '
                                              f'Вам не удалось ничего получить, но теперь вы его'
                                              f' вряд ли когда-нибудь увидите')
                    del self.names[self.names.index(self.name)]
                elif r < 90:
                    self.mainQuestion.setText('Вам удалось его убить, получить предмет и немного денег, но теперь '
                                              'торговцы будут ходить к вам реже и с опаской.')
                    self.inventory.content.append(self.item)
                    self.inventory.remake()
                    self.money += rand(10, 100)
                    del self.tasks[3]
                else:
                    self.mainQuestion.setText(f'Торговец оказался древним колдуном, и как только вы '
                                              f'напали на него, {self.name} испепелил своим фаерболом вас и весь '
                                              f'бункер заодно.\nМораль: никогда не нападай на невинных '
                                              f'с виду дедушек.')
                    self.people = 0
                self.text_changes()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


# Артем
def new_event():
    a = open("event.txt", encoding="utf8")
    events = [i.split('\n') for i in a.read().split('\n\n')]
    a.close()
    even = []
    for i in range(len(events) - 1):
        eve = []
        eve.append(events[i][0])
        eve.append([events[i][1].split('/')[0], [i.split('!') for i in events[i][2].split('/')]])
        eve.append([events[i][1].split('/')[1], [i.split('!') for i in events[i][3].split('/')]])
        eve.append([events[i][1].split('/')[2], [i.split('!') for i in events[i][4].split('/')]])
        even.append(eve)
        # print(eve)
    return even


if __name__ == '__main__':
    app = QApplication(sys.argv)
    startWindow = MainMenuWindow()
    startWindow.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
