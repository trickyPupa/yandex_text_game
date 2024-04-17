# весь файл - Тимофей
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Inventory(object):
    def setupUi(self, Inventory):
        Inventory.setObjectName("Inventory")
        Inventory.resize(400, 400)
        Inventory.setMinimumSize(QtCore.QSize(400, 400))
        Inventory.setMaximumSize(QtCore.QSize(400, 400))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(189, 216, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(189, 216, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(189, 216, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(189, 216, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Inventory.setPalette(palette)

        self.retranslateUi(Inventory)
        QtCore.QMetaObject.connectSlotsByName(Inventory)

    def retranslateUi(self, Inventory):
        _translate = QtCore.QCoreApplication.translate
        Inventory.setWindowTitle(_translate("Inventory", "Инвентарь", "0"))


class Ui_GameWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 700))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 700))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainQuestion = QtWidgets.QTextEdit(self.centralwidget)
        self.mainQuestion.setGeometry(QtCore.QRect(159, 79, 671, 351))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        self.mainQuestion.setFont(font)
        self.mainQuestion.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mainQuestion.setReadOnly(True)
        self.mainQuestion.setObjectName("mainQuestion")
        self.leftAnswer = QtWidgets.QPushButton(self.centralwidget)
        self.leftAnswer.setGeometry(QtCore.QRect(49, 460, 221, 131))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        self.leftAnswer.setFont(font)
        self.leftAnswer.setObjectName("leftAnswer")
        self.centralAnswer = QtWidgets.QPushButton(self.centralwidget)
        self.centralAnswer.setGeometry(QtCore.QRect(389, 480, 221, 131))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        self.centralAnswer.setFont(font)
        self.centralAnswer.setObjectName("centralAnswer")
        self.rightAnswer = QtWidgets.QPushButton(self.centralwidget)
        self.rightAnswer.setGeometry(QtCore.QRect(729, 460, 221, 131))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        self.rightAnswer.setFont(font)
        self.rightAnswer.setObjectName("rightAnswer")
        self.number3 = QtWidgets.QLabel(self.centralwidget)
        self.number3.setGeometry(QtCore.QRect(880, 640, 60, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.number3.setFont(font)
        self.number3.setFrameShape(QtWidgets.QFrame.Box)
        self.number3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.number3.setLineWidth(3)
        self.number3.setAlignment(QtCore.Qt.AlignCenter)
        self.number3.setObjectName("number3")
        self.number2 = QtWidgets.QLabel(self.centralwidget)
        self.number2.setGeometry(QtCore.QRect(510, 640, 60, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.number2.setFont(font)
        self.number2.setFrameShape(QtWidgets.QFrame.Box)
        self.number2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.number2.setLineWidth(3)
        self.number2.setAlignment(QtCore.Qt.AlignCenter)
        self.number2.setObjectName("number2")
        self.number1 = QtWidgets.QLabel(self.centralwidget)
        self.number1.setGeometry(QtCore.QRect(120, 640, 60, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.number1.setFont(font)
        self.number1.setFrameShape(QtWidgets.QFrame.Box)
        self.number1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.number1.setLineWidth(3)
        self.number1.setAlignment(QtCore.Qt.AlignCenter)
        self.number1.setObjectName("number1")
        self.icon1 = QtWidgets.QLabel(self.centralwidget)
        self.icon1.setGeometry(QtCore.QRect(50, 635, 71, 60))
        self.icon1.setText("")
        self.icon1.setPixmap(QtGui.QPixmap("картинки/чббургер60.png"))
        self.icon1.setAlignment(QtCore.Qt.AlignCenter)
        self.icon1.setObjectName("icon1")
        self.icon2 = QtWidgets.QLabel(self.centralwidget)
        self.icon2.setGeometry(QtCore.QRect(430, 635, 70, 61))
        self.icon2.setText("")
        self.icon2.setPixmap(QtGui.QPixmap("картинки/чблюди60.png"))
        self.icon2.setAlignment(QtCore.Qt.AlignCenter)
        self.icon2.setObjectName("icon2")
        self.icon3 = QtWidgets.QLabel(self.centralwidget)
        self.icon3.setGeometry(QtCore.QRect(810, 635, 71, 61))
        self.icon3.setText("")
        self.icon3.setPixmap(QtGui.QPixmap("картинки/чбденьги60.png"))
        self.icon3.setAlignment(QtCore.Qt.AlignCenter)
        self.icon3.setObjectName("icon3")
        tip1 = 'Это показатель еды.\nЕда тратится каждый день в зависимости от ' \
               'количества жителей.\nИгра закончится, если показатель станет равен 0.'
        self.icon1.setToolTip(tip1)
        self.number1.setToolTip(tip1)
        tip2 = 'Это показатель жителей.\nКоличество жителей влияет на многие важные показатели, ' \
               'а также на развитие сюжета.\nИгра закончится, если показатель станет равен 0.'
        self.icon2.setToolTip(tip2)
        self.number2.setToolTip(tip2)
        tip3 = 'Это показатель денег.\nЗа деньги возможно купить разнообразные предметы, ' \
               'которые могут пригодиться позже.'
        self.icon3.setToolTip(tip3)
        self.number3.setToolTip(tip3)
        self.menuButton = QtWidgets.QPushButton(self.centralwidget)
        self.menuButton.setGeometry(QtCore.QRect(20, 20, 51, 51))
        self.menuButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("картинки/меню60.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuButton.setIcon(icon)
        self.menuButton.setIconSize(QtCore.QSize(41, 41))
        self.menuButton.setObjectName("menuButton")
        self.menuButton.setToolTip('Меню')
        self.currentDay = QtWidgets.QLabel(self.centralwidget)
        self.currentDay.setGeometry(QtCore.QRect(380, 10, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.currentDay.setFont(font)
        self.currentDay.setAlignment(QtCore.Qt.AlignCenter)
        self.currentDay.setObjectName("currentDay")
        self.inventoryButton = QtWidgets.QPushButton(self.centralwidget)
        self.inventoryButton.setGeometry(QtCore.QRect(860, 20, 120, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        self.inventoryButton.setFont(font)
        self.inventoryButton.setObjectName("inventoryButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Igra 0"))
        self.mainQuestion.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Bahnschrift\',\'Bahnschrift\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Bahnschrift\';\">Начать игру?</span></p></body></html>"))
        self.leftAnswer.setText(_translate("MainWindow", "Начать"))
        self.centralAnswer.setText(_translate("MainWindow", "Начать"))
        self.rightAnswer.setText(_translate("MainWindow", "Начать"))
        self.number3.setText(_translate("MainWindow", "10"))
        self.number2.setText(_translate("MainWindow", "20"))
        self.number1.setText(_translate("MainWindow", "100"))
        self.currentDay.setText(_translate("MainWindow", "День 0"))
        self.inventoryButton.setText(_translate("MainWindow", "Инвентарь"))


class Ui_MenuWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.newGameButton = QtWidgets.QPushButton(self.centralwidget)
        self.newGameButton.setGeometry(QtCore.QRect(20, 270, 160, 40))
        self.newGameButton.setObjectName("newGameButton")
        self.gameExit = QtWidgets.QPushButton(self.centralwidget)
        self.gameExit.setGeometry(QtCore.QRect(20, 340, 160, 40))
        self.gameExit.setObjectName("gameExit")
        self.continueButton = QtWidgets.QPushButton(self.centralwidget)
        self.continueButton.setEnabled(False)
        self.continueButton.setGeometry(QtCore.QRect(20, 200, 160, 40))
        self.continueButton.setObjectName("continueButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Igra Главное меню"))
        self.newGameButton.setText(_translate("MainWindow", "Новая игра"))
        self.gameExit.setText(_translate("MainWindow", "Выйти из игры"))
        self.continueButton.setText(_translate("MainWindow", "Продолжить игру"))


class Ui_PauseMenu(object):
    def setupUi(self, PauseMenu):
        PauseMenu.setObjectName("PauseMenu")
        PauseMenu.resize(400, 400)
        PauseMenu.setMinimumSize(QtCore.QSize(400, 400))
        PauseMenu.setMaximumSize(QtCore.QSize(400, 400))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(189, 216, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(189, 216, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(189, 216, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(189, 216, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        PauseMenu.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        PauseMenu.setFont(font)
        self.continueButton = QtWidgets.QPushButton(PauseMenu)
        self.continueButton.setGeometry(QtCore.QRect(60, 40, 281, 51))
        self.continueButton.setObjectName("continueButton")
        self.newGameButton = QtWidgets.QPushButton(PauseMenu)
        self.newGameButton.setGeometry(QtCore.QRect(60, 120, 281, 51))
        self.newGameButton.setObjectName("newGameButton")
        self.mainMenuExit = QtWidgets.QPushButton(PauseMenu)
        self.mainMenuExit.setGeometry(QtCore.QRect(60, 200, 281, 51))
        self.mainMenuExit.setObjectName("mainMenuExit")
        self.gameExitButton = QtWidgets.QPushButton(PauseMenu)
        self.gameExitButton.setGeometry(QtCore.QRect(60, 280, 281, 51))
        self.gameExitButton.setObjectName("gameExitButton")

        self.retranslateUi(PauseMenu)
        QtCore.QMetaObject.connectSlotsByName(PauseMenu)

    def retranslateUi(self, PauseMenu):
        _translate = QtCore.QCoreApplication.translate
        PauseMenu.setWindowTitle(_translate("PauseMenu", "Игровое меню"))
        self.continueButton.setText(_translate("PauseMenu", "Продолжить"))
        self.newGameButton.setText(_translate("PauseMenu", "Новая игра"))
        self.mainMenuExit.setText(_translate("PauseMenu", "Выйти в главное меню"))
        self.gameExitButton.setText(_translate("PauseMenu", "Выйти из игры"))
