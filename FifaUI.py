import PyQt6
import sys
from PyQt6.QtCore import Qt
from FifaBLL import players
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QWidget, QComboBox
from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer
from PyQt6 import QtGui,QtCore
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import *
import sqlite3
from FifaDataModel import Datamodel

class form(QWidget):
    # ui of form
    def __init__(self):
        QWidget.__init__(self)
        self.resize(500, 500)    
        self.players = players()
        self.flag = True
        self.overall = 30
        self.labeloverall = QLabel(self)
        self.labeloverall.move(250, 70)
        # layout for button
        self.layoutList = []
        mainLayout = QGridLayout()
        for i in range(3):
            layout = QGridLayout()
            mainLayout.addLayout(layout, i, 0, 1, 1)
            self.layoutList.append(layout)
        self.setLayout(mainLayout)

        # layout1
        labeList = ["FirstName","Overall", "Position", "Nation"]
        for i, txt in enumerate(labeList):
            label = QLabel()
            label.setText(f"{txt}: ")
            self.layoutList[0].addWidget(label, i, 0, 1, 1)
        #name
        self.playername = QLineEdit()
        self.playername.setStyleSheet(
            'QLineEdit {border: 1px solid purple;border-radius:2;background-color: #F4E3FF;padding:4}')
        self.playername.setPlaceholderText("Please Enter Player's First Name")
        self.layoutList[0].addWidget(self.playername, 0, 1, 1, 1)
        # overalls
        self.minOverall = QSlider(Qt.Orientation.Horizontal, self)
        self.minOverall.setMinimum(30)
        self.minOverall.setMaximum(99)
        self.minOverall.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.minOverall.setTickInterval(5)
        self.minOverall.valueChanged.connect(self.values)
        self.layoutList[0].addWidget(self.minOverall, 1, 1, 1, 1)
        # posts
        self.playerpost = QLineEdit()
        self.playerpost.setStyleSheet(
            'QLineEdit {border: 1px solid purple;border-radius:2;background-color: #F4E3FF;padding:4}')
        self.playerpost.setPlaceholderText("Please Enter Player's Position")
        self.layoutList[0].addWidget(self.playerpost, 2, 1, 1, 1)
        # nations
        self.playerNation = QComboBox(self)
        self.playerNation.addItems(["Any", "Argentine", "Austria", "Belgium", "Brazil", "Croatia", "England",
                                    "France", "Germany", "Iran", "Italy", "Norway", "Portugal", "Spain"])
        self.playerNation.setStyleSheet('QComboBox {border: 1px solid purple;border-radius:2;background-color: #F4E3FF;padding:4} QComboBox QAbstractItemView {background-color:#e8bcf0;color:purple}')
        self.layoutList[0].addWidget(self.playerNation, 3, 1, 1, 1)

        # layout2
        # button CREATE
        button = QPushButton()
        button.setText("CREATE")
        button.clicked.connect(self.Create)
        button.setStyleSheet(
            'QPushButton {background-color: purple; color: white;border-radius:6;padding:4;font-weight:bold}')
        self.layoutList[1].addWidget(button, 0, 0, 1, 1)
        # button SEARCH
        button = QPushButton()
        button.setText("SEARCH")
        button.clicked.connect(self.select)
        button.setStyleSheet(
            'QPushButton {background-color: purple; color: white;border-radius:6;padding:4;font-weight:bold}')
        self.layoutList[1].addWidget(button, 0, 1, 1, 1)
        #button UPDATE
        button = QPushButton()
        button.setText("UPDATE")
        button.clicked.connect(self.updateForm)
        button.setStyleSheet(
            'QPushButton {background-color: purple; color: white;border-radius:6;padding:4;font-weight:bold}')
        self.layoutList[1].addWidget(button, 0, 2, 1, 1)
        #button DELETE
        button = QPushButton()
        button.setText("DELETE")
        button.clicked.connect(self.deleteForm)
        button.setStyleSheet(
            'QPushButton {background-color: purple; color: white;border-radius:6;padding:4;font-weight:bold}')
        self.layoutList[1].addWidget(button, 0, 3, 1, 1)
        # button CLOSE
        button = QPushButton()
        button.setText("CLOSE")
        button.clicked.connect(self.closeForm)
        button.setStyleSheet(
            'QPushButton {background-color: purple; color: white;border-radius:6;padding:4;font-weight:bold}')
        self.layoutList[1].addWidget(button, 0, 4, 1, 1)


        # layout3
        self.table = QTableView()
        self.table.setStyleSheet(
            'QTableView {background-color: #F4E3FF;border:2px solid purple;border-radius:6}')
        self.table.resize(500, 300)
        self.layoutList[2].addWidget(self.table)

    # button function

    def Create(self):
        if self.flag:
            self.players.createData()
            self.flag = False

    def select(self):
        overall = self.overall
        post = self.playerpost.text()
        nation = self.playerNation.currentText()
        playername = self.playername.text()
        rows = self.players.searchData(playername,overall, post, nation)
        if len(rows):
            self.datamodel = Datamodel(rows)
            self.table.setModel(self.datamodel)

    def values(self):
        self.labeloverall.setText("Value: "+str(self.sender().value()))
        self.labeloverall.adjustSize()
        self.overall = self.sender().value()
    def updateForm(self):
        overall = self.overall
        post = self.playerpost.text()
        nation = self.playerNation.currentText()
        playername = self.playername.text()
        if playername!="" and nation !="Any" and overall and post!="":
            self.players.updateData(playername,overall, post, nation)

    def deleteForm(self):
        overall = self.overall
        post = self.playerpost.text()
        nation = self.playerNation.currentText()
        playername = self.playername.text()
        if playername!="" and nation !="Any" and overall and post!="":
            self.players.deletesData(playername,overall, post, nation)

    def closeForm(self):
        self.players.deleteData()
        self.close()


app = QApplication(sys.argv)
# Name
app.setApplicationName("Football Bartar")
#Icon
app.setWindowIcon(QIcon('icon.webp'))
# Music
filename = "music.mp3"
player = QMediaPlayer()
audio_output = QAudioOutput()
player.setAudioOutput(audio_output)
player.setSource(QUrl.fromLocalFile(filename))
audio_output.setVolume(50)
player.play()

form = form()
# form.setStyleSheet('QApplication {background-image:url("./1.jfif");width:100%}')
form.show()
sys.exit(app.exec())
