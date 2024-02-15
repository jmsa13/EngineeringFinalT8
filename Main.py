from PySide6.QtGui import QDragMoveEvent
from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import *
from PySide6.QtCharts import QChart

from ui_interface import *

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Calls the ui_interface.py file and makes that the main window
        # then hides the window title as well as setup the Ui widgets
        self.ui = Ui_MainWindow()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.setupUi(self)

        # move window by clicking on the title bar, calls move_window function to initiate
        self.ui.title_bar.mouseMoveEvent = self.mouseMoveEvent = self.move_window

    # Function will check if maximized and if not, will wait for left click to move the window from the click_position
    def move_window(self, e):
        if not (self.isMaximized()):
            if e.buttons() == Qt.LeftButton:
                self.move(self.pos() + e.globalPos() - self.click_position)
            self.click_position = e.globalPos()
            e.accept()

    # this function is for the move mouse event that updates it's global position
    def mousePressEvent(self, event):
        self.click_position = event.globalPos()

    # function for the 3 minimize/maximize and close buttons
    def header_buttons_style(self):
        # exit button
        self.ui.close_window_button.clicked.connect(self.close)

        # restore button for the window to minimize/maximize the window
        self.ui.restore_window_button.setCheckable(True)
        self.ui.restore_window_button.clicked.connect(self.buttons_connected)

        # minimize window button
        self.ui.minimize_window_button.setCheckable(True)
        self.ui.minimize_window_button.clicked.connect(self.buttons_connected)

    def menu_buttons_style(self):
        # calls the menu buttons function to change the widget to the button clicked
        self.ui.percent_bar_chart_button.setCheckable(True)
        self.ui.percent_bar_chart_button.clicked.connect(self.menu_buttons)

        self.ui.temperature_chart_button.setCheckable(True)
        self.ui.temperature_chart_button.clicked.connect(self.menu_buttons)

        self.ui.nested_donuts_button.setCheckable(True)
        self.ui.nested_donuts_button.clicked.connect(self.menu_buttons)

        self.ui.line_chart_button.setCheckable(True)
        self.ui.line_chart_button.clicked.connect(self.menu_buttons)

        self.ui.bar_chart_button.setCheckable(True)
        self.ui.bar_chart_button.clicked.connect(self.menu_buttons)

        self.ui.menu_button.setCheckable(True)
        self.ui.menu_button.clicked.connect(self.menu_buttons)

    # determines if the buttons have been clicked to initiate the required closing or opening/minimizing of the window
    def buttons_connected(self):
        # will maximize the window or minimize when clicked
        if self.ui.restore_window_button.isChecked():
            self.showMaximized()
        else:
            self.showNormal()

        # will minimize the window then reset the button to false
        if self.ui.minimize_window_button.isChecked():
            self.showMinimized()
            self.ui.minimize_window_button.setChecked(False)

    # will change the widgets based on the button clicked in the menu then resets the check
    def menu_buttons(self):
        # this will hide the menu when the menu button is clicked and show when it is hidden
        if self.ui.menu_button.isChecked():
            if not (self.ui.left_menu_widget.isHidden()):
                self.ui.left_menu_widget.hide()
            else:
                self.ui.left_menu_widget.show()
            self.ui.menu_button.setChecked(False)

        # these if statements will change the stacked widget to show what button is clicked in the menu
        if self.ui.percent_bar_chart_button.isChecked():
            self.ui.stackedWidget.setCurrentIndex(0)
            self.ui.percent_bar_chart_button.setChecked(False)

        if self.ui.temperature_chart_button.isChecked():
            self.ui.stackedWidget.setCurrentIndex(1)
            self.ui.temperature_chart_button.setChecked(False)

        if self.ui.nested_donuts_button.isChecked():
            self.ui.stackedWidget.setCurrentIndex(2)
            self.ui.nested_donuts_button.setChecked(False)

        if self.ui.line_chart_button.isChecked():
            self.ui.stackedWidget.setCurrentIndex(3)
            self.ui.line_chart_button.setChecked(False)

        if self.ui.bar_chart_button.isChecked():
            self.ui.stackedWidget.setCurrentIndex(4)
            self.ui.bar_chart_button.setChecked(False)


if __name__ == "__main__":
    executable = QApplication(sys.argv)
    window = MainWindow()
    window.header_buttons_style()
    window.menu_buttons_style()
    window.show()
    executable.exec()
