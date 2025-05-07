# Python PyQt5 Digital Clock
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTime, QTimer, Qt
from PyQt5.QtGui import QFont, QFontDatabase # to work with downloaded fonts
from PyQt5.QtGui import QIcon



class DigitalClock(QWidget):
    def __init__(self):
        super().__init__() # Think of it as saying: "Hey, parent class, do your setup first, and then I'll add my custom stuff. In order to access all the functionalities from the parent class"
        self.time_label = QLabel("14:00:00",self)
        self.timer = QTimer(self)
        self.setWindowIcon(QIcon("digital-clock.png"))
        self.init_ui()


    def init_ui(self):

        self.setWindowTitle("Digital Clock")
        self.setGeometry(700,300,300,100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter) # . AlignCenter is a flag
        self.time_label.setStyleSheet("font-size: 150px;" "color: hsl(200, 100%, 25%)")
        self.setStyleSheet("background: lightgreen")

        # ADDING A NEW FONT

        font_id = QFontDatabase.addApplicationFont("C:\\Users\\arsos\\OneDrive\\Desktop\\Python&Math\\HelloWorld"
                                                   "\\PyQt5 - GUI\\DigitalClock\\font\\DS-DIGIB.TTF")  # For managing and queering fonts available to the application
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]  # returns a list of font names, we pass [0] because we need only the first element from that list
        new_font = QFont(font_family, 150)  # font size and our newly added font
        self.time_label.setFont(new_font)
        # If we want to add a custom font to out program
        # We will need TTF TrueType Font file from Google or anywhere else
        self.timer.timeout.connect(self.update_time) # connecting signal to a slot
        self.timer.start(1000) # This means update our clock every second

        # UPDATING TIME ON THE CLOCK
        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP") # for current time and .text() for setting up time format (AP is for Anti-meridian and P post-meridian this is for AM or PM)
        self.time_label.setText(current_time)
def main():
    app = QApplication(sys.argv)
    window = DigitalClock()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()