from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from constants import button_color, hover_button_color


class AnalysisScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        
    def setup_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(40, 40, 40, 40)

        # Style constants
        self.MINT_GREEN = button_color
        self.BUTTON_STYLE = f"""
            QPushButton {{
                background-color: {self.MINT_GREEN};
                border-radius: 8px;
                padding: 8px;
                border: none;
                color: white;
                font-weight: bold;
                font-size: 14px;
            }}
            QPushButton:hover {{
                background-color: {hover_button_color};
            }}
        """

        # Header layout with title and download button
        header_layout = QHBoxLayout()
        
        # Title
        title = QLabel("Analysis")
        title.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        
        # Download button
        # download_button = QPushButton()
        # download_button.setFixedSize(40, 40)
        # download_button.setIcon(icons.DOWNLOAD)
        # download_button.setIconSize(Qt.QSize(20, 20))
        # download_button.setStyleSheet(self.BUTTON_STYLE)
        # download_button.clicked.connect(self.download_packets)

        download_button = QPushButton("Download")
        download_button.setStyleSheet(self.BUTTON_STYLE)
        download_button.clicked.connect(self.download_packets)
        
        header_layout.addWidget(title)
        header_layout.addStretch()
        header_layout.addWidget(download_button)
        
        self.captured_info = QLabel("Captured a total of 0 packets")
        self.captured_info.setFont(QFont("Arial", 11))
        self.captured_info.setStyleSheet("color: #666")
        
        # Create two columns layout
        columns_layout = QHBoxLayout()
        left_column = QVBoxLayout()
        right_column = QVBoxLayout()
        
        # Left Column - Device Info Section
        device_title = QLabel("Device Monitored:")
        device_title.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        self.ip_address = QLabel("IP address: -")
        self.mac_address = QLabel("MAC address: -")
        left_column.addWidget(device_title)
        left_column.addWidget(self.ip_address)
        left_column.addWidget(self.mac_address)
        left_column.addSpacing(20)
        
        # Left Column - Active Protocols section
        protocols_title = QLabel("Active Protocols:")
        protocols_title.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        left_column.addWidget(protocols_title)
        self.protocols_labels = QVBoxLayout()
        left_column.addLayout(self.protocols_labels)
        left_column.addSpacing(20)
        
        # Left Column - Transport Count section
        transport_title = QLabel("Transports Count:")
        transport_title.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        self.tcp_count = QLabel("TCP: 0 packets")
        self.udp_count = QLabel("UDP: 0 packets")
        left_column.addWidget(transport_title)
        left_column.addWidget(self.tcp_count)
        left_column.addWidget(self.udp_count)
        
        # Right Column - Data transfer section
        transfer_title = QLabel("Total Data Transferred:")
        transfer_title.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        self.data_sent = QLabel("Sent: -")
        self.data_received = QLabel("Received: -")
        right_column.addWidget(transfer_title)
        right_column.addWidget(self.data_sent)
        right_column.addWidget(self.data_received)
        right_column.addSpacing(20)
        
        # Right Column - DNS Queries section
        self.dns_section = QWidget()
        dns_layout = QVBoxLayout(self.dns_section)
        dns_title = QLabel("DNS Queries:")
        dns_title.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        dns_layout.addWidget(dns_title)
        self.dns_queries = QVBoxLayout()
        dns_layout.addLayout(self.dns_queries)
        self.dns_section.hide()  # Hidden by default
        right_column.addWidget(self.dns_section)
        
        # Add stretch to both columns
        left_column.addStretch(1)
        right_column.addStretch(1)
        
        # Add columns to the columns layout
        columns_layout.addLayout(left_column)
        columns_layout.addSpacing(40)  # Add space between columns
        columns_layout.addLayout(right_column)
        
        # Add all elements to main layout
        main_layout.addLayout(header_layout)
        main_layout.addWidget(self.captured_info)
        main_layout.addSpacing(20)
        main_layout.addLayout(columns_layout)
        
        self.setLayout(main_layout)

    def clear_dynamic_labels(self, layout):
        """Helper function to clear all widgets from a layout"""
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

    def update_data(self, data):
        self.captured_info.setText(f"Captured a total of {data['total_packets']} packets")
        self.ip_address.setText(f"IP address: {data['ip_address']}")
        self.mac_address.setText(f"MAC address: {data['mac_address']}")
        self.tcp_count.setText(f"TCP: {data['tcp_packets']} packets")
        self.udp_count.setText(f"UDP: {data['udp_packets']} packets")
        self.data_sent.setText(f"Sent: {data['data_sent']}")
        self.data_received.setText(f"Received: {data['data_received']}")
        
        # Clear and update protocols
        self.clear_dynamic_labels(self.protocols_labels)
        for protocol, count in data['protocols'].items():
            protocol_label = QLabel(f"{protocol}: {count} packets")
            self.protocols_labels.addWidget(protocol_label)
        
        # Clear and update DNS queries
        self.clear_dynamic_labels(self.dns_queries)
        
        # Show DNS section only if there are queries
        if data['dns_queries']:
            for domain, count in data['dns_queries'].items():
                query_label = QLabel(f"{domain} ({count} queries)")
                self.dns_queries.addWidget(query_label)
            self.dns_section.show()
        else:
            self.dns_section.hide()

    def download_packets(self):
        print("Downloaded")