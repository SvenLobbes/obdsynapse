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

        # === LINKE SEITE: Plots ===
        plot_col = QVBoxLayout()
        self.plot_widgets = []
        for i in range(6):
            plot = pg.PlotWidget()
            plot.setYRange(0, 8000)
            curve = plot.plot(pen='g')
            plot_col.addWidget(plot)
            self.plot_widgets.append((plot, curve, np.zeros(100), 0))  # (widget, curve, data, index)

        h_layout.addLayout(plot_col, stretch=3)

        # === MITTE: DTC-Liste mit Scroll ===
        dtc_layout = QVBoxLayout()
        for i in range(20):  # Beispielcodes
            dtc_button = QPushButton(f"DTC {i+1}: P0{i:03}")
            dtc_layout.addWidget(dtc_button)

        dtc_widget = QWidget()
        dtc_widget.setLayout(dtc_layout)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(dtc_widget)
        h_layout.addWidget(scroll_area, stretch=1)

        # === RECHTE SEITE: Buttons ===
        button_col = QVBoxLayout()
        btn_connection = QPushButton("Connect OBD")
        btn_shutdown = QPushButton("SHUTDOWN")
        btn_update = QPushButton("UPDATE")
        btn_exit = QPushButton("EXIT APP")
        for btn in [btn_shutdown, btn_update, btn_exit]:
            btn.setMinimumHeight(60)
            button_col.addWidget(btn)

        h_layout.addLayout(button_col, stretch=1)

        # Verbinde Buttons
        btn_shutdown.clicked.connect(self.shutdown)
        btn_update.clicked.connect(self.update_system)
        btn_exit.clicked.connect(self.close)
        btn_connection.clicked(self.)

        # Timer für Dummy-Daten
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plots)
        self.timer.start(200)

    def update_plots(self):
        for plot, curve, data, idx in self.plot_widgets:
            value = np.random.randint(1000, 7000)
            data[idx] = value
            idx = (idx + 1) % 100
            curve.setData(data)
            # Update intern speichern
            self.plot_widgets[self.plot_widgets.index((plot, curve, data, idx - 1))] = (plot, curve, data, idx)

    def shutdown(self):
        print("Shutdown sysmt")
        # os.system("sudo shutdown now")

    def update_system(self):
        print("update OBD Synapse")
        # subprocess.call(["bash", "/pfad/zum/update.sh"])

def main():
    
    #startup of GUI
    app = QApplication(sys.argv)
    dashboard = Dashboard()
    dashboard.show()


    #receive Connection





    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
