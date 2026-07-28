"""
DiskArchive Pro v2
Chart Widget
"""

from PySide6.QtCharts import (
    QBarCategoryAxis,
    QBarSeries,
    QBarSet,
    QChart,
    QChartView,
    QPieSeries,
    QValueAxis,
)

from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QVBoxLayout, QWidget


class ChartWidget(QWidget):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.chart = QChart()

        self.chart_view = QChartView(self.chart)

        self.chart_view.setRenderHint(
            QPainter.Antialiasing
        )

        layout = QVBoxLayout(self)

        layout.setContentsMargins(0, 0, 0, 0)

        layout.addWidget(self.chart_view)

    # -------------------------------------------------
    # CLEAR
    # -------------------------------------------------

    def clear(self):

        self.chart.removeAllSeries()

        for axis in self.chart.axes():

            self.chart.removeAxis(axis)

    # -------------------------------------------------
    # TITLE
    # -------------------------------------------------

    def set_title(self, title):

        self.chart.setTitle(title)

    # -------------------------------------------------
    # BAR CHART
    # -------------------------------------------------

    def show_bar_chart(self, title, labels, values):

        self.clear()

        self.chart.setTitle(title)

        bar_set = QBarSet(title)

        for value in values:

            bar_set.append(value)

        series = QBarSeries()

        series.append(bar_set)

        self.chart.addSeries(series)

        axis_x = QBarCategoryAxis()

        axis_x.append(labels)

        axis_y = QValueAxis()

        self.chart.addAxis(axis_x, Qt.AlignBottom)

        self.chart.addAxis(axis_y, Qt.AlignLeft)

        series.attachAxis(axis_x)

        series.attachAxis(axis_y)

    # -------------------------------------------------
    # PIE CHART
    # -------------------------------------------------

    def show_pie_chart(self, title, data):

        self.clear()

        self.chart.setTitle(title)

        series = QPieSeries()

        for name, value in data.items():

            series.append(name, value)

        self.chart.addSeries(series)

    # -------------------------------------------------
    # FILE EXTENSIONS
    # -------------------------------------------------

    def show_extensions(self, rows):

        labels = []

        values = []

        for row in rows:

            labels.append(row["extension"])

            values.append(row["file_count"])

        self.show_bar_chart(

            "Dosya Türleri",

            labels,

            values,

        )

    # -------------------------------------------------
    # LARGEST FOLDERS
    # -------------------------------------------------

    def show_largest_folders(self, folders):

        labels = []

        values = []

        for folder in folders:

            labels.append(folder.name)

            values.append(folder.size)

        self.show_bar_chart(

            "En Büyük Klasörler",

            labels,

            values,

        )