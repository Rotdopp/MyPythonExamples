import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(800, 200, 500, 500)
        self.setWindowIcon(QIcon("img.png"))
        #QLabel write Hello in the window
        label = QLabel("Hello", self)
        #font and size
        label.setFont(QFont("Arial", 40))
        #loaction
        label.setGeometry(0, 0, 500, 100)
        #you can use RGB to change colors
        label.setStyleSheet("color: blue;"#color of word
                            "background-color: black;"#color of background
                            "font-weight: bold;"# bold or skiny
                            "font-style: italic;"#font_style
                            "text-decoration: underline;")


        label.setAlignment(Qt.AlignTop)#Verticly on top
        label.setAlignment(Qt.AlignBottom)#Verticly on Bottom

def main():
    app=QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
