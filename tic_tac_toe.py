# type: ignore

import os
import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog

player = ""
tie = False

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        """Initializes the Tic Tac Toe game board and sets up the user interface."""
        super(Ui, self).__init__()
        self.ui_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "ui"))
        starting_ui_path = self.ui_path + "/tictactoe.ui"
        uic.loadUi(starting_ui_path, self) 
        self.firstPlayer = True
        self.moves = 1
        self.label = self.findChild(QtWidgets.QLabel, "playerLabel")
        self.label.setStyleSheet("color: blue")
        self.label.setText("X")

        for num in range(1,10):
            self.button = self.findChild(QtWidgets.QPushButton, f"pushButton_{num}")
            self.button.clicked.connect(self.buttonPressed)

        self.show()


    def buttonPressed(self):
        """Handles the button press event and updates the game board accordingly."""
        button = self.sender()
        if not button.text():
            if self.firstPlayer:
                button.setText("X")
                self.label.setText("O")
                self.label.setStyleSheet("color: red")
                button.setStyleSheet("color: blue")
                self.checkWinCondition()
            else:
                button.setText("O")
                self.label.setText("X")
                self.label.setStyleSheet("color: blue")
                button.setStyleSheet("color: red")
                self.checkWinCondition()
            self.moves += 1
            self.firstPlayer = not self.firstPlayer


    def checkWinCondition(self):
        """Checks if the game has been won or tied and updates the game board accordingly."""
        global player
        global tie
        winning_tris = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
        self.counter = 0
        self.winning_tiles = []
        button = self.sender()
        sender_text = button.text()
        for tris in winning_tris:
            for element in tris:
                self.tile = self.findChild(QtWidgets.QPushButton, f"pushButton_{element}")
                if button.text() in self.tile.text():
                    self.counter += 1
                    self.winning_tiles.append(element)
                    if self.counter == 3:
                        for element in self.winning_tiles:
                            self.selected_button = self.findChild(QtWidgets.QPushButton, f"pushButton_{element}")
                            self.selected_button.setStyleSheet("border: 2px solid red; color: green")
                        player = sender_text
                        self.endgamewindow = EndGameWindow()
                        self.endgamewindow.exec_()
                        return
            self.counter = 0
            self.winning_tiles = []
        if self.moves == 9:
            tie = True
            self.showEndGameDialog()


    def showEndGameDialog(self):
        "Shows the end game pop-up window."
        self.endgamewindow = EndGameWindow()
        self.endgamewindow.exec_()

    
    def clearBoard(self):
        "Clears the board."
        global tie
        for num in range(1,10):
            self.button = self.findChild(QtWidgets.QPushButton, f"pushButton_{num}")
            self.button.setText("")
            self.button.setStyleSheet("background-color: white;border-style: inset;border-color: gray")
        self.counter = 0
        self.moves = 0
        self.winning_tiles = []
        tie = False


class EndGameWindow(QDialog):
    def __init__(self):
        """Initializes the end game window and sets up the user interface."""
        super().__init__()
        global player
        global tie
        self.ui_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "ui"))
        starting_ui_path = self.ui_path + "/endgame.ui" 
        uic.loadUi(starting_ui_path, self)
        if not tie:
            self.label.setText(f"{player} Won!")
        else:
            self.label.setText("Draw!")
        self.button = self.findChild(QtWidgets.QPushButton, "restartButton")
        self.button.clicked.connect(self.buttonPressed)


    def buttonPressed(self):
        """Handles the clear button press event."""
        window.clearBoard()
        self.close()



app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()