from config.libs import *

#file imports
import globals




def getConnections(): 
    print("Scanning for ports")
    ports = obd.scan_serial()

    return ports


class PortSelectorDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.selected_port = None
        ports = getConnections()


        layout = QVBoxLayout()
        layout.addWidget(QLabel("Please select port:"))

        self.combo = QComboBox()
        for port in ports: 
            self.combo.addItem(port)
        layout.addWidget(self.combo)
        