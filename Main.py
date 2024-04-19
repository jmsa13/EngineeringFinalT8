from ui_interface import *
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Calls the ui_interface.py file and makes that the main window
        # then hides the window title as well as set up the Ui widgets
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
            self.ui.company_cloud_breaches_button: lambda: self.change_widget(0),
            self.ui.us_cloud_breaches_button: lambda: self.change_widget(1),
            self.ui.russian_cloud_breaches_button: lambda: self.change_widget(2),
            self.ui.china_cloud_breaches_button: lambda: self.change_widget(3),
            self.ui.uk_cloud_breaches_button: lambda: self.change_widget(4),
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
        if self.ui.stackedWidget.currentIndex() == 0:
            self.company_cloud_breaches_data()
        # Reset all the chart buttons to unchecked
        chart_buttons = [
            self.ui.company_cloud_breaches_button,
            self.ui.us_cloud_breaches_button,
            self.ui.russian_cloud_breaches_button,
            self.ui.china_cloud_breaches_button,
            self.ui.uk_cloud_breaches_button
        ]

        # goes through buttons in the list to set too false to change the index of the tab when clicked again
        for button in chart_buttons:
            button.setChecked(False)

    def company_cloud_breaches_data(self):
        company_data = pd.read_csv('CompanyData.csv')
        bar_colors = ['tab:purple', 'tab:red', 'tab:blue', 'tab:pink', 'tab:green', 'tab:orange']

        fig = Figure()
        plot = fig.add_subplot(111)  # Ensure the plot uses a 111 subplot grid

        plot.bar(company_data['Company Name'], company_data['Amount of Users Affected'],
                 label=company_data['Company Name'],
                 color=bar_colors)
        plot.set_title('Major company cloud breaches')
        plot.set_xlabel('Company Name')
        plot.set_ylabel('Amount of Users Affected')
        plot.legend()

        # Create canvas and add to the stacked widget, 
        # if widget count is higher than 0 remove old widget and insert new one
        self.plot_canvas = FigureCanvas(fig)
        if self.ui.stackedWidget.count() > 0:
            self.ui.stackedWidget.removeWidget(self.ui.stackedWidget.widget(0))
        self.ui.stackedWidget.insertWidget(0, self.plot_canvas)

        self.ui.stackedWidget.setCurrentIndex(0)  # Ensure the widget is visible


if __name__ == "__main__":
    executable = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(executable.exec())
