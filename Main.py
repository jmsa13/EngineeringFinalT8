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

        self.initialize_buttons()  # initializes all buttons in the GUI to be used

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

    """
    Function initialize_buttons() is the most important function,
    it initializes the buttons in a dictionary with values corresponding
    to their function; it also executes a for loop to set the buttons check-able
    and to wait for a click signal to execute the action of the value desired.    
    """
    def initialize_buttons(self):
        buttons_actions = {
            self.ui.restore_window_button: self.toggle_window,
            self.ui.minimize_window_button: self.minimize_window,
            self.ui.close_window_button: self.close,
            self.ui.percent_bar_chart_button: lambda: self.change_widget(0),
            self.ui.temperature_chart_button: lambda: self.change_widget(1),
            self.ui.nested_donuts_button: lambda: self.change_widget(2),
            self.ui.line_chart_button: lambda: self.change_widget(3),
            self.ui.bar_chart_button: lambda: self.change_widget(4),
            self.ui.menu_button: self.toggle_menu
        }

        for button, action in buttons_actions.items():
            button.setCheckable(True)
            button.clicked.connect(action)

    """
    Function toggle_window checks the maximize/minimize window button,
    it will change the size of the GUI to fit the screen or return to
    the default size based on the status of the check boolean.
    """
    def toggle_window(self):
        if self.ui.restore_window_button.isChecked():
            self.showMaximized()
            if self.ui.restore_window_button.isMaximized():  # if it is already maximized, return to normal state
                self.showNormal()
        else:
            self.showNormal()
            self.ui.restore_window_button.setChecked(False)

    """
    Function minimize_window simply hides the whole GUI, 
    just need to click on the app icon again to bring it up
    """
    def minimize_window(self):
        self.showMinimized()
        self.ui.minimize_window_button.setChecked(False)

    """
    Function toggle_menu() is called when the menu button is clicked, 
    it sends the signal to show or hide the menu depending on
    the state of the menu when clicked.
    """
    def toggle_menu(self):
        if not self.ui.left_menu_widget.isHidden():
            self.ui.left_menu_widget.hide()
        else:
            self.ui.left_menu_widget.show()
        self.ui.menu_button.setChecked(False)

    """
    Function change_widget() takes the index of the widget and sets it to the current index
    of the page shown in the menu.
        - when clicked, the widget calls change_widget and sends the index as a parameter.
            the function then changes all buttons to false after the designated widget is 
            shown after this function is called.
    """
    def change_widget(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)

        # Reset all the chart buttons to unchecked
        chart_buttons = [
            self.ui.percent_bar_chart_button,
            self.ui.temperature_chart_button,
            self.ui.nested_donuts_button,
            self.ui.line_chart_button,
            self.ui.bar_chart_button
        ]

        # goes through buttons in the list to set too false to change the index of the tab when clicked again
        for button in chart_buttons:
            button.setChecked(False)


if __name__ == "__main__":
    executable = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(executable.exec())
