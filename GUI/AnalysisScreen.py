from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class AnalysisScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(40, 40, 40, 40)

        # Style constants
        self.MINT_GREEN = "#9AD9AC"
        self.BUTTON_STYLE = f"""
            QPushButton {{
                background-color: {self.MINT_GREEN};
                border-radius: 8px;
                padding: 15px 30px;
                border: none;
                color: white;
                font-size: 16px;
            }}
            QPushButton:hover {{
                background-color: {self.MINT_GREEN}DD;
            }}
        """

        # Title
        title = QLabel("Analysis")
        title.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        
        # Captured packets info
        self.captured_info = QLabel("Captured a total of 0 packets")
        self.captured_info.setFont(QFont("Arial", 11))
        self.captured_info.setStyleSheet("color: #666")
        
        # Create two columns
        device_info = QVBoxLayout()
        transport_info = QVBoxLayout()
        
        # Device Monitored section
        device_title = QLabel("Device Monitored:")
        device_title.setFont(QFont("Arial", 11))
        self.ip_address = QLabel("IP address: -")
        self.mac_address = QLabel("MAC address: -")
        
        # Transport Count section
        transport_title = QLabel("Transports Count:")
        transport_title.setFont(QFont("Arial", 11))
        self.tcp_count = QLabel("TCP: 0 packets")
        self.udp_count = QLabel("UDP: 0 packets")
        
        # Add labels to columns
        device_info.addWidget(device_title)
        device_info.addWidget(self.ip_address)
        device_info.addWidget(self.mac_address)
        
        transport_info.addWidget(transport_title)
        transport_info.addWidget(self.tcp_count)
        transport_info.addWidget(self.udp_count)
        
        # Download button
        download_button = QPushButton("Download packets")
        download_button.setStyleSheet(self.BUTTON_STYLE)
        download_button.clicked.connect(self.download_packets)
        
        # Add all elements to main layout
        layout.addWidget(title)
        layout.addWidget(self.captured_info)
        layout.addLayout(device_info)
        layout.addSpacing(20)
        layout.addLayout(transport_info)
        layout.addStretch(1)
        layout.addWidget(download_button, alignment=Qt.AlignmentFlag.AlignRight)
        
        self.setLayout(layout)

    def update_data(self, data):
        self.captured_info.setText(f"Captured a total of {data['total_packets']} packets")
        self.ip_address.setText(f"IP address: {data['ip_address']}")
        self.mac_address.setText(f"MAC address: {data['mac_address']}")
        self.tcp_count.setText(f"TCP: {data['tcp_packets']} packets")
        self.udp_count.setText(f"UDP: {data['udp_packets']} packets")

    def download_packets(self):
        # To be implemented later
        pass