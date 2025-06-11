import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QScrollArea
)
from PyQt5.QtCore import QTimer, Qt
import pyqtgraph as pg
import numpy as np


#file imports
import globals
from dashboard_elements.validateConnection import open_connection_dialog

class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OBD Dashboard")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.showFullScreen()

        main = QWidget()
        self.setCentralWidget(main)
        h_layout = QHBoxLayout()
        main.setLayout(h_layout)

        # Plots
        plot_col = QVBoxLayout()
        self.plot_widgets = []
        for _ in range(6):
            plot = pg.PlotWidget()
            plot.setYRange(0, 8000)
            curve = plot.plot(pen='g')
            plot_col.addWidget(plot)
            self.plot_widgets.append((plot, curve, np.zeros(100), 0))
        h_layout.addLayout(plot_col, stretch=3)

        # DTC-Liste
        dtc_layout = QVBoxLayout()
        for i in range(20):
            dtc_button = QPushButton(f"DTC {i+1}: P0{i:03}")
            dtc_layout.addWidget(dtc_button)

        dtc_widget = QWidget()
        dtc_widget.setLayout(dtc_layout)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(dtc_widget)
        h_layout.addWidget(scroll_area, stretch=1)

        # Buttons
        button_col = QVBoxLayout()
        btn_connect = QPushButton("Connect OBD")
        btn_shutdown = QPushButton("SHUTDOWN")
        btn_update = QPushButton("UPDATE")
        btn_exit = QPushButton("EXIT APP")

        for btn in [btn_connect, btn_shutdown, btn_update, btn_exit]:
            btn.setMinimumHeight(60)
            button_col.addWidget(btn)

        h_layout.addLayout(button_col, stretch=1)

        # Button-Verbindungen
        btn_connect.clicked.connect(self.connect_obd)
        btn_shutdown.clicked.connect(self.shutdown)
        btn_update.clicked.connect(self.update_system)
        btn_exit.clicked.connect(self.close)

        # Timer für Plots
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plots)
        self.timer.start(200)

    def connect_obd(self):
        conn = open_connection_dialog()
        if conn:
            globals.obd_connection = conn
            print("OBD verbunden")
        else:
            print("OBD nicht verbunden")

    def update_plots(self):
        for i, (plot, curve, data, idx) in enumerate(self.plot_widgets):
            value = np.random.randint(1000, 7000)
            data[idx] = value
            idx = (idx + 1) % 100
            curve.setData(data)
            self.plot_widgets[i] = (plot, curve, data, idx)

    def shutdown(self):
        print("System wird heruntergefahren…")

    def update_system(self):
        print("Update-Funktion ausgeführt")

def main():
    app = QApplication(sys.argv)
    dashboard = Dashboard()
    dashboard.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
