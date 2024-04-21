from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas as pd


class Graphs:
    def __init__(self):
        self.Figure = Figure()
        self.plot_canvas = FigureCanvas(self.Figure)
        self.plot = self.Figure.add_subplot(111)   # Ensure the plot uses a 111 subplot grid

    def company_cloud_breaches_data(self):
        company_data = pd.read_csv('CompanyData.csv')
        bar_colors = ['tab:purple', 'tab:red', 'tab:blue', 'tab:pink', 'tab:green', 'tab:orange']

        self.plot.bar(company_data['Company Name'], company_data['Amount of Users Affected'],
                 label=company_data['Company Name'],
                 color=bar_colors)
        self.plot.set_title('Major company cloud breaches')
        self.plot.set_xlabel('Company Name')
        self.plot.set_ylabel('Amount of Users Affected')
        self.plot.legend()

        # return canvas and to be added to the stacked widget
        return self.plot_canvas


