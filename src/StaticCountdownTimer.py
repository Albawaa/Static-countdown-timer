"""
StaticCountdownTimer.py

A simple little timer that counts down to zero just for you ^^

Arguments:
    name: The title of the timer to display.
    time_sec: Initial timer starting time in secconds, without spaces.

Note:
    For more timer customization see the css file in the config folder.
"""
import sys
import argparse
from PySide6 import QtCore, QtWidgets

POPUP_COORD_X_PX = 0
POPUP_COORD_Y_PX = 0


def convert_seconds(seconds):
    minutes, remaining_seconds = divmod(seconds, 60)
    return f"{minutes:02d}:{remaining_seconds:02d}"

class StaticCountdownTimer(QtWidgets.QWidget):
    def __init__(self, name: str, time_sec: int):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint, True)

        self.move(POPUP_COORD_X_PX, POPUP_COORD_Y_PX)

        self.timer_label = QtWidgets.QLabel(name, alignment=QtCore.Qt.AlignCenter)
        self.timer_label.setObjectName("timerTitle")
        self.time_label = QtWidgets.QLabel(convert_seconds(time_sec), alignment=QtCore.Qt.AlignCenter)
        self.time_label.setObjectName("timerCountdown")
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setSpacing(0)
        self.main_layout.addWidget(self.timer_label)
        self.main_layout.addWidget(self.time_label)
        self.setLayout(self.main_layout)

        self.time_left = time_sec
        self.qt_timer = QtCore.QTimer(self)
        self.qt_timer.timeout.connect(self._update_label)
        self.qt_timer.start(1000)

    def _update_label(self):
        self.time_left = self.time_left - 1

        if self.time_left > 0:
            self.time_label.setText(convert_seconds(self.time_left))
        elif self.time_left == 0:
            self.time_label.setText(convert_seconds(0))
        else:
            sys.exit(0)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='StaticCountdownTimer',
                    description='A little timer that counts down just for you ^^')
    parser.add_argument('name')
    parser.add_argument('time_sec')
    args = parser.parse_args()

    app = QtWidgets.QApplication([])
    with open("config/styles.css", "r") as f:
        stylesheet = f.read()

    app.setStyleSheet(stylesheet)

    widget = StaticCountdownTimer(name=args.name, time_sec=int(args.time_sec))
    widget.resize(400, 150)
    widget.show()

    sys.exit(app.exec())