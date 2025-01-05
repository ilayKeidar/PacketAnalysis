from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                           QLineEdit, QPushButton, QComboBox)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from user_data import INTERFACES


class HomeScreen(QWidget):
    def __init__(self, on_start_callback):
        super().__init__()
        self.on_start_callback = on_start_callback
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(20)
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
                font-size: 18px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: "#6F9C7C";
            }}
        """
        
        self.INPUT_STYLE = """
            QLineEdit {
                padding: 8px;
                border: 1px solid #DDD;
                border-radius: 4px;
                background: white;
                min-width: 80px;
                max-width: 80px;
                color: black;
            }
        """
        
        self.COMBOBOX_STYLE = """
            QComboBox {
                padding: 8px;
                padding-right: 35px;  
                border: 1px solid #DDD;
                border-radius: 4px;
                background: white;
                min-width: 120px;
                max-width: 120px;
                color: black;
                font-size: 12px;
            }
            
            QComboBox::drop-down {
                border: none;
                width: 20px;
            }
            
            QComboBox::down-arrow {
                border: none;
                width: 12px;
                height: 12px;
                image: none;  
                border-left: 2px solid #666;
                border-bottom: 2px solid #666;
                transform: rotate(-45deg);
                margin-right: 8px;
                margin-top: -4px;
            }
            
            QComboBox QAbstractItemView {
                color: black;
                background-color: white;
                selection-background-color: #e0e0e0;
                padding: 4px;
                font-size: 13px;
            }
            
            QComboBox QAbstractItemView::item {
                min-height: 24px;
                padding: 4px;
            }
        """

        # Title container with reduced spacing
        title_container = QVBoxLayout()
        title_container.setSpacing(5)
        
        # Title
        title = QLabel("Packet Analysis")
        title.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Subtitle
        subtitle = QLabel("Sniff and analyze your device's network traffic")
        subtitle.setFont(QFont("Arial", 12))
        subtitle.setStyleSheet("color: #666")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Add title and subtitle to container
        title_container.addWidget(title)
        title_container.addWidget(subtitle)
        
        # Input fields in horizontal layouts
        duration_container = QHBoxLayout()
        interface_container = QHBoxLayout()
        
        # Sniff duration input
        sniff_duration_label = QLabel("Sniff duration (seconds):")
        sniff_duration_label.setFont(QFont("Arial", 14))
        self.sniff_duration_input = QLineEdit()
        self.sniff_duration_input.setStyleSheet(self.INPUT_STYLE)
        
        # Network interface dropdown
        interface_label = QLabel("Network Interface:")
        interface_label.setFont(QFont("Arial", 14, QFont.Weight.Medium))
        self.interface_input = QComboBox()
        self.interface_input.setStyleSheet(self.COMBOBOX_STYLE)
        self.interface_input.setFont(QFont("Arial", 12))  # Base font for the combobox
        
        # Add interfaces and set default
        interfaces = INTERFACES
        self.interface_input.addItems(interfaces)
        self.interface_input.setCurrentText("Wi-Fi")  
        
        # Add fields to their containers with proper alignment
        duration_container.addWidget(sniff_duration_label)
        duration_container.addWidget(self.sniff_duration_input)
        duration_container.addStretch()
        
        interface_container.addWidget(interface_label)
        interface_container.addWidget(self.interface_input)
        interface_container.addStretch()
        
        # Start button
        start_button = QPushButton("Start Sniffing")
        start_button.setStyleSheet(self.BUTTON_STYLE)
        start_button.clicked.connect(self.start_sniffing)
        
        # Input fields container
        fields_container = QVBoxLayout()
        fields_container.setSpacing(10)  # Reduced spacing between input fields
        fields_container.addLayout(duration_container)
        fields_container.addLayout(interface_container)
        
        # Add all elements to main layout
        layout.addLayout(title_container)
        layout.addStretch(1)
        layout.addLayout(fields_container)
        layout.addStretch(1)
        layout.addWidget(start_button)
        
        self.setLayout(layout)

    def start_sniffing(self):
        duration = self.sniff_duration_input.text()
        interface = self.interface_input.currentText()
        self.on_start_callback(duration, interface)