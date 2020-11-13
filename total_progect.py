import random
import sys
import sqlite3
from itertools import cycle
from PyQt5.QtWidgets import QWidget, QPushButton, QComboBox, QTabWidget, QLineEdit, QLCDNumber, QPlainTextEdit, \
    QButtonGroup
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer, QSize
from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def __init__(self):
        self._button_group = QButtonGroup()
        self.COLOR = {'Красный': 'red.jpg', 'Синий': 'dark_blue.jpg', 'Зелёный': 'green.jpg',
                      'Фиолетовый': 'purple.jpg', 'Чёрный': 'black.jpg', 'Розовый': 'pink.jpg',
                      'Оранжевый': 'orange.jpg', 'Коричневый': 'brovn.jpg', 'Голубой': 'blue.jpg',
                      'Жёлтый': 'yellow.jpg'}
        self.widget_main = QTabWidget(Form)
        self.widget_game = QWidget()
        self.widget_top10 = QWidget()
        self.play_button = QPushButton(self.widget_game)
        self.choose_color_2 = QComboBox(self.widget_game)
        self.choose_color_1 = QComboBox(self.widget_game)
        self.name_team_2 = QLineEdit(self.widget_game)
        self.name_team_1 = QLineEdit(self.widget_game)
        self.button_south = QPushButton(self.widget_game)
        self.button_west = QPushButton(self.widget_game)
        self.button_noth = QPushButton(self.widget_game)
        self.button_east = QPushButton(self.widget_game)
        self.game_over_sec = QLCDNumber(self.widget_game)
        self.info_tab = QPlainTextEdit(self.widget_game)
        self.top_tab = QPlainTextEdit(self.widget_top10)
        self.matrix = list()
        self.time_game = 300
        self.kol_move = 0
        self.x, self.y = 6, 6
        self.con = sqlite3.connect("football.db")
        self.cur = self.con.cursor()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.widget_main.setGeometry(QtCore.QRect(0, 0, 641, 481))
        self.widget_main.setMouseTracking(False)
        self.widget_main.setTabletTracking(False)
        self.widget_main.setAcceptDrops(False)
        self.widget_main.setAutoFillBackground(False)
        self.widget_main.setTabPosition(QtWidgets.QTabWidget.South)
        self.widget_main.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.widget_main.setTabsClosable(False)
        self.widget_main.setMovable(False)
        self.widget_main.setTabBarAutoHide(False)
        self.widget_main.setObjectName("widget_main")
        self.widget_game.setObjectName("widget_game")
        self.info_tab.setGeometry(QtCore.QRect(470, 50, 160, 90))
        self.info_tab.setEnabled(False)
        self.top_tab.setGeometry(QtCore.QRect(120, 50, 400, 360))
        self.top_tab.setEnabled(False)
        self.game_over_sec.setGeometry(QtCore.QRect(520, 160, 110, 60))
        self.game_over_sec.setObjectName("game_over_sec")
        self.button_east.setGeometry(QtCore.QRect(580, 320, 40, 30))
        self.button_east.setObjectName("button_east")
        self.button_noth.setGeometry(QtCore.QRect(540, 290, 40, 30))
        self.button_noth.setObjectName("button_noth")
        self.button_west.setGeometry(QtCore.QRect(500, 320, 40, 30))
        self.button_west.setObjectName("button_west")
        self.button_south.setGeometry(QtCore.QRect(540, 350, 40, 30))
        self.button_south.setMinimumSize(QtCore.QSize(41, 31))
        self.button_south.setObjectName("button_south")
        self.name_team_1.setGeometry(QtCore.QRect(0, 0, 110, 30))
        self.name_team_1.setObjectName("name_team_1")
        self.name_team_2.setGeometry(QtCore.QRect(240, 0, 110, 30))
        self.name_team_2.setObjectName("name_team_2")
        self.choose_color_1.setGeometry(QtCore.QRect(120, 0, 110, 30))
        self.choose_color_1.setObjectName("choose_color_1")
        self.choose_color_1.addItem("")
        self.choose_color_1.addItem("")
        self.choose_color_1.addItem("")
        self.choose_color_1.addItem("")
        self.choose_color_1.addItem("")
        self.choose_color_2.setGeometry(QtCore.QRect(360, 0, 110, 30))
        self.choose_color_2.setObjectName("choose_color_2")
        self.choose_color_2.addItem("")
        self.choose_color_2.addItem("")
        self.choose_color_2.addItem("")
        self.choose_color_2.addItem("")
        self.choose_color_2.addItem("")
        self.play_button.setGeometry(QtCore.QRect(500, 0, 110, 40))
        self.play_button.setText("ИГРАТЬ")
        self.play_button.setIconSize(QtCore.QSize(16, 16))
        self.play_button.setShortcut("")
        self.play_button.setObjectName("play_button")
        self.play_button.clicked.connect(self._play_button_clicked)
        self.widget_main.addTab(self.widget_game, "")
        self.widget_top10.setObjectName("widget_top10")
        self.widget_main.addTab(self.widget_top10, "")
        for i in range(13):
            self.matrix.append(list())
            for j in range(13):
                btn = QPushButton('', self.widget_game)
                btn.setGeometry((i + 2) * 30, j * 30 + 50, 30, 30)
                btn.setStyleSheet('QPushButton {background-color: white}')
                self.matrix[-1].append(btn)
        self._update_tad_top()
        self.retranslateUi(Form)
        self.widget_main.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.button_east.setText("˃")
        self.button_noth.setText("˄")
        self.button_west.setText("˂")
        self.button_south.setText("˅")
        self._button_group.addButton(self.button_south)
        self._button_group.addButton(self.button_east)
        self._button_group.addButton(self.button_noth)
        self._button_group.addButton(self.button_west)
        self._button_group.buttonClicked.connect(self._button_move)
        self.choose_color_1.setItemText(0, _translate("Form", "Синий"))
        self.choose_color_1.setItemText(1, _translate("Form", "Оранжевый"))
        self.choose_color_1.setItemText(2, _translate("Form", "Зелёный"))
        self.choose_color_1.setItemText(3, _translate("Form", "Фиолетовый"))
        self.choose_color_1.setItemText(4, _translate("Form", "Чёрный"))
        self.choose_color_2.setItemText(0, _translate("Form", "Красный"))
        self.choose_color_2.setItemText(1, _translate("Form", "Розовый"))
        self.choose_color_2.setItemText(2, _translate("Form", "Коричневый"))
        self.choose_color_2.setItemText(3, _translate("Form", "Голубой"))
        self.choose_color_2.setItemText(4, _translate("Form", "Жёлтый"))
        self.widget_main.setTabText(self.widget_main.indexOf(self.widget_game), _translate("Form", "Игра"))
        self.widget_main.setTabText(self.widget_main.indexOf(self.widget_top10), _translate("Form", "Топ команд"))

    def _play_button_clicked(self):
        if self.name_team_1.text() == self.name_team_2.text() == '':
            self.all_teams = ('Зенит', 'Локомотив', self.choose_color_1.currentText(),
                              self.choose_color_2.currentText(), 0)
        else:
            self.all_teams = (self.name_team_1.text(), self.name_team_2.text(), self.choose_color_1.currentText(),
                              self.choose_color_2.currentText(), 0)
        self.cur.execute("""INSERT INTO players(name_team1,name_team2,color_team1,color_team2, time_win) 
                            VALUES(?, ?, ?, ?, ?);""",
                            self.all_teams)
        self.con.commit()
        self.color1, self.color2 = self.COLOR[self._return_znach(key=('color_team1',))[0]],\
                                   self.COLOR[self._return_znach(key=('color_team2',))[0]]
        for i in range(13):
            for j in range(13):
                if 5 <= i <= 7 and j == 0:
                    self.matrix[i][j].setIcon(QIcon(self.color1))
                    self.matrix[i][j].setIconSize(QSize(20, 20))
                    self.matrix[i][j].setText('-')
                elif 5 <= i <= 7 and j == 12:
                    self.matrix[i][j].setIcon(QIcon(self.color2))
                    self.matrix[i][j].setIconSize(QSize(20, 20))
                    self.matrix[i][j].setText('-')
                else:
                    self.matrix[i][j].setText('')
                    self.matrix[i][j].setIcon(QIcon())
        self.matrix[6][6].setIcon(QIcon('football_ball.jpg'))
        self.matrix[6][6].setIconSize(QSize(25, 25))
        self._teams = [self._return_znach(key=("name_team1",))[0], self._return_znach(key=("name_team2",))[0]]
        first_move = random.randint(0, 1)
        self._teams_cycle = cycle([self._teams[first_move], self._teams[abs(first_move - 1)]])
        self.time_game = 300
        self.game_over_sec.display(self.time_game)
        self.player_now = next(self._teams_cycle)
        self.info_tab.setPlaceholderText(f'Ход команды\n{self.player_now}')
        QTimer.singleShot(1000, self._update)
        self.button_south.setEnabled(True)
        self.button_west.setEnabled(True)
        self.button_noth.setEnabled(True)
        self.button_east.setEnabled(True)
        self.x, self.y, self.kol_move = 6, 6, 0


    def _update(self):
        try:
            k = -1
            self.time_game -= 1
            k /= self.time_game
            self.game_over_sec.display(self.time_game)
            QTimer.singleShot(1000, self._update)
        except ZeroDivisionError:
            self.game_over_sec.display(0)
            name_win = self._return_znach(key=("win_team",))[0]
            if name_win == 'Ничья':
                self.info_tab.setPlaceholderText(f'Игра окончена!\n{name_win}')
                return
            self.info_tab.setPlaceholderText(f'Игра окончена!\n'
                                             f'Победила команда {self._return_znach(key=("win_team",))[0]}')

    def _return_znach(self, key=('name',)):
        result = self.cur.execute(f"""SELECT {key[0]} FROM players
                                WHERE number_of_play=(SELECT MAX(number_of_play) 
                                FROM players)""").fetchone()
        return result

    def _button_move(self, button):
        text = button.text()
        if text == "˃":
            self._move_right()
        elif text == "˂":
            self._move_left()
        elif text == "˄":
            self._move_up()
        elif text == "˅":
            self._move_down()
        if self.matrix[self.x][self.y].text() == '-':
            if self.y == 12:
                self.cur.execute("""UPDATE players SET win_team = (SELECT name_team1 FROM players 
                                                WHERE number_of_play=(SELECT MAX(number_of_play) FROM players))
                                                WHERE number_of_play=(SELECT MAX(number_of_play) FROM players)""")
                self.cur.execute(f"""UPDATE players SET time_win = ?
                                                    WHERE number_of_play=(SELECT MAX(number_of_play) 
                                                    FROM players);""", (self.time_game,))
                self.con.commit()
                self.time_game = 1
                self.button_south.setEnabled(False)
                self.button_west.setEnabled(False)
                self.button_noth.setEnabled(False)
                self.button_east.setEnabled(False)
                self._update_tad_top()
                return

            else:
                self.cur.execute("""UPDATE players SET win_team = (SELECT name_team2 FROM players 
                                WHERE number_of_play=(SELECT MAX(number_of_play) FROM players))
                                WHERE number_of_play=(SELECT MAX(number_of_play) FROM players)""")
                self.cur.execute(f"""UPDATE players SET time_win = ?
                                    WHERE number_of_play=(SELECT MAX(number_of_play) 
                                    FROM players);""", (self.time_game,))
                self.time_game = 1
                self.con.commit()
                self.button_south.setEnabled(False)
                self.button_west.setEnabled(False)
                self.button_noth.setEnabled(False)
                self.button_east.setEnabled(False)
                self._update_tad_top()
                return
        if self.kol_move == 3:
            self.player_now = next(self._teams_cycle)
            self.info_tab.setPlaceholderText(f'Ход команды\n{self.player_now}')
            self.kol_move = 0

    def _move_right(self):
        if self.x + 1 < 13:
            if self.matrix[self.x + 1][self.y].text() != "." and self.matrix[self.x][self.y].text() != '-':
                if self.player_now == self._teams[0]:
                    self.matrix[self.x][self.y].setIcon(QIcon(self.color1))
                    self.matrix[self.x][self.y].setIconSize(QSize(20, 20))
                    self.matrix[self.x][self.y].setText('.')
                    self.x += 1
                    self.matrix[self.x][self.y].setIcon(QIcon('football_ball.jpg'))
                    self.matrix[self.x][self.y].setIconSize(QSize(25, 25))
                    self.kol_move += 1
                elif self.player_now == self._teams[1]:
                    self.matrix[self.x][self.y].setIcon(QIcon(self.color2))
                    self.matrix[self.x][self.y].setIconSize(QSize(20, 20))
                    self.matrix[self.x][self.y].setText('.')
                    self.x += 1
                    self.matrix[self.x][self.y].setIcon(QIcon('football_ball.jpg'))
                    self.matrix[self.x][self.y].setIconSize(QSize(25, 25))
                    self.kol_move += 1
            if (self.matrix[self.x][self.y].text() == "." and self.matrix[self.x - 1][self.y].text() == "."
                  and self.matrix[self.x][self.y + 1].text() == "." and
                  self.matrix[self.x][self.y - 1].text() == "."):
                self._strake()

    def _move_left(self):
        if self.x - 1 > -1:
            if self.matrix[self.x - 1][self.y].text() != "." and self.matrix[self.x][self.y].text() != '-':
                if self.player_now == self._teams[0]:
                    self.matrix[self.x][self.y].setIcon(QIcon(self.color1))
                    self.matrix[self.x][self.y].setIconSize(QSize(20, 20))
                    self.matrix[self.x][self.y].setText('.')
                    self.x -= 1
                    self.matrix[self.x][self.y].setIcon(QIcon('football_ball.jpg'))
                    self.matrix[self.x][self.y].setIconSize(QSize(25, 25))
                    self.kol_move += 1
                if self.player_now == self._teams[1]:
                    self.matrix[self.x][self.y].setIcon(QIcon(self.color2))
                    self.matrix[self.x][self.y].setIconSize(QSize(20, 20))
                    self.matrix[self.x][self.y].setText('.')
                    self.x -= 1
                    self.matrix[self.x][self.y].setIcon(QIcon('football_ball.jpg'))
                    self.matrix[self.x][self.y].setIconSize(QSize(25, 25))
                    self.kol_move += 1
            if (self.matrix[self.x + 1][self.y].text() == "." and self.matrix[self.x - 1][self.y].text() == "."
                  and self.matrix[self.x][self.y + 1].text() == "." and
                  self.matrix[self.x][self.y - 1].text() == "."):
                self._strake()

    def _move_down(self):
        if self.y + 1 < 13:
            if self.matrix[self.x][self.y + 1].text() != "." and self.matrix[self.x][self.y].text() != '-':
                if self.player_now == self._teams[0]:
                    self.matrix[self.x][self.y].setIcon(QIcon(self.color1))
                    self.matrix[self.x][self.y].setIconSize(QSize(20, 20))
                    self.matrix[self.x][self.y].setText('.')
                    self.y += 1
                    self.matrix[self.x][self.y].setIcon(QIcon('football_ball.jpg'))
                    self.matrix[self.x][self.y].setIconSize(QSize(25, 25))
                    self.kol_move += 1
                elif self.player_now == self._teams[1]:
                    self.matrix[self.x][self.y].setIcon(QIcon(self.color2))
                    self.matrix[self.x][self.y].setIconSize(QSize(20, 20))
                    self.matrix[self.x][self.y].setText('.')
                    self.y += 1
                    self.matrix[self.x][self.y].setIcon(QIcon('football_ball.jpg'))
                    self.matrix[self.x][self.y].setIconSize(QSize(25, 25))
                    self.kol_move += 1
            if (self.matrix[self.x + 1][self.y].text() == "." and self.matrix[self.x - 1][self.y].text() == "."
                  and self.matrix[self.x][self.y + 1].text() == "." and
                  self.matrix[self.x][self.y - 1].text() == "."):
                self._strake()

    def _move_up(self):
        if self.y - 1 > -1:
            if self.matrix[self.x][self.y - 1].text() != "." and self.matrix[self.x][self.y].text() != '-':
                if self.player_now == self._teams[0]:
                    self.matrix[self.x][self.y].setIcon(QIcon(self.color1))
                    self.matrix[self.x][self.y].setIconSize(QSize(20, 20))
                    self.matrix[self.x][self.y].setText('.')
                    self.y -= 1
                    self.matrix[self.x][self.y].setIcon(QIcon('football_ball.jpg'))
                    self.matrix[self.x][self.y].setIconSize(QSize(25, 25))
                    self.kol_move += 1
                elif self.player_now == self._teams[1]:
                    self.matrix[self.x][self.y].setIcon(QIcon(self.color2))
                    self.matrix[self.x][self.y].setIconSize(QSize(20, 20))
                    self.matrix[self.x][self.y].setText('.')
                    self.y -= 1
                    self.matrix[self.x][self.y].setIcon(QIcon('football_ball.jpg'))
                    self.matrix[self.x][self.y].setIconSize(QSize(25, 25))
                    self.kol_move += 1
            if (self.matrix[self.x + 1][self.y].text() == "." and self.matrix[self.x - 1][self.y].text() == "."
                and self.matrix[self.x][self.y + 1].text() == "." and self.matrix[self.x][self.y - 1].text() == "."):
                self._strake()

    def _strake(self):
        i, k = 0, 3
        if self.player_now == self._teams[0]:
            self.info_tab.setPlaceholderText(f'Штрафной\nКоманды {self._teams[0]}')
            while i < k:
                if self.y + 1 < 13:
                    if self.matrix[self.x][self.y - 1].text() != "." and self.matrix[self.x][self.y].text() != '-':
                        self.matrix[self.x][self.y].setIcon(QIcon(self.color1))
                        self.matrix[self.x][self.y].setIconSize(QSize(20, 20))
                        self.matrix[self.x][self.y].setText('.')
                        self.y += 1
                        self.matrix[self.x][self.y].setIcon(QIcon('football_ball.jpg'))
                        self.matrix[self.x][self.y].setIconSize(QSize(25, 25))
                        i += 1
                    elif self.matrix[self.x][self.y].text() == '-':
                        self.cur.execute("""UPDATE players SET win_team = (SELECT name_team1 FROM players 
                                            WHERE number_of_play=(SELECT MAX(number_of_play) FROM players))
                                            WHERE number_of_play=(SELECT MAX(number_of_play) FROM players)""")
                        self.cur.execute(f"""UPDATE players SET time_win = ?
                                             WHERE number_of_play=(SELECT MAX(number_of_play) 
                                             FROM players);""", (self.time_game - 300,))
                        self.con.commit()
                        self.time_game = 1
                        self.info_tab.setPlaceholderText(f'Игра окончена!\nПобедила команда {self._teams[0]}')
                        self.button_south.setEnabled(False)
                        self.button_west.setEnabled(False)
                        self.button_noth.setEnabled(False)
                        self.button_east.setEnabled(False)
                        self._update_tad_top()
                        return
                    elif self.matrix[self.x][self.y + 1].text() == '.':
                        self.matrix[self.x][self.y].setIcon(QIcon(self.color1))
                        self.matrix[self.x][self.y].setIconSize(QSize(20, 20))
                        self.matrix[self.x][self.y].setText('.')
                        self.y += 1
                        self.matrix[self.x][self.y].setIcon(QIcon('football_ball.jpg'))
                        self.matrix[self.x][self.y].setIconSize(QSize(25, 25))
                        i += 1
                        k += 1
        elif self.player_now == self._teams[1]:
            self.info_tab.setPlaceholderText(f'Штрафной\nКоманды {self._teams[1]}')
            while i < k:
                if self.y - 1 > -1:
                    if self.matrix[self.x + 1][self.y].text() != "." and self.matrix[self.x][self.y].text() != "-":
                        self.matrix[self.x][self.y].setIcon(QIcon(self.color2))
                        self.matrix[self.x][self.y].setIconSize(QSize(20, 20))
                        self.matrix[self.x][self.y].setText('.')
                        self.y -= 1
                        self.matrix[self.x][self.y].setIcon(QIcon('football_ball.jpg'))
                        self.matrix[self.x][self.y].setIconSize(QSize(25, 25))
                        i += 1
                    elif self.matrix[self.x][self.y].text() == '-':
                        self.cur.execute("""UPDATE players SET win_team = (SELECT name_team2 FROM players 
                                                WHERE number_of_play=(SELECT MAX(number_of_play) FROM players))
                                                WHERE number_of_play=(SELECT MAX(number_of_play) FROM players)""")
                        self.cur.execute(f"""UPDATE players SET time_win = ?
                                                    WHERE number_of_play=(SELECT MAX(number_of_play) 
                                                    FROM players);""", (self.time_game,))
                        self.con.commit()
                        self.time_game = 1
                        self.info_tab.setPlaceholderText(f'Игра окончена!\nПобедила команда {self._teams[0]}')
                        self.button_south.setEnabled(False)
                        self.button_west.setEnabled(False)
                        self.button_noth.setEnabled(False)
                        self.button_east.setEnabled(False)
                        self._update_tad_top()
                        return
                    elif self.matrix[self.x][self.y - 1].text() == '.':
                        self.matrix[self.x][self.y].setIcon(QIcon(self.color1))
                        self.matrix[self.x][self.y].setIconSize(QSize(20, 20))
                        self.matrix[self.x][self.y].setText('.')
                        self.y -= 1
                        self.matrix[self.x][self.y].setIcon(QIcon('football_ball.jpg'))
                        self.matrix[self.x][self.y].setIconSize(QSize(25, 25))
                        i += 1
                        k += 1

    def _update_tad_top(self):
        result = self.cur.execute("""SELECT time_win 
                                       FROM players""").fetchall()
        result.sort(reverse=True)
        with open('text_for_top.txt', mode='w') as out_file:
            if len(result) > 20:
                for i in range(10):
                    total = self.cur.execute("SELECT win_team FROM players WHERE time_win=?;", result[i]).fetchone()
                    print('', i + 1, total[0], abs(result[i][0] - 300), file=out_file, sep='\t')
            else:
                for i in range(len(result)):
                    total = self.cur.execute("SELECT win_team FROM players WHERE time_win=?;", result[i]).fetchone()
                    print('', i + 1, total[0], abs(result[i][0] - 300), file=out_file, sep='\t')
        with open('text_for_top.txt', mode='r') as file:
            self.top_tab.setPlainText(file.read())
        self.con.commit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
