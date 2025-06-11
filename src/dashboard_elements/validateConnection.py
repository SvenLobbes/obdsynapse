from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QComboBox, QPushButton, QHBoxLayout
import obd

class PortSelectorDialog(QDialog):
    def __init__(self, ports):
        super().__init__()
        self.setWindowTitle("OBD-Port auswählen")
        self.selected_port = None
        self.ports = ports

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Bitte wähle einen Port:"))

        self.combo = QComboBox()
        for port in ports:
            self.combo.addItem(port)
        layout.addWidget(self.combo)

        button_layout = QHBoxLayout()
        ok_button = QPushButton("OK")
        cancel_button = QPushButton("Abbrechen")
        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)
        layout.addLayout(button_layout)

        ok_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)

        self.setLayout(layout)

    def get_selected_port(self):
        if self.exec_() == QDialog.Accepted:
            return self.combo.currentText()
        else:
            return None

def open_connection_dialog():
    ports = obd.scan_serial()
    if not ports:
        print("Keine Ports gefunden.")
        return None

    dialog = PortSelectorDialog(ports)
    selected = dialog.get_selected_port()

    if selected:
        conn = obd.OBD(portstr=selected)
        if conn.is_connected():
            return conn
    return None
