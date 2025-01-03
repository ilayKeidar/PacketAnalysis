from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

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
                padding: 10px 30px;
                border: none;
                color: white;
                font-size: 16px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {self.MINT_GREEN}DD;
            }}
        """
        
        self.INPUT_STYLE = """
            QLineEdit {
                padding: 8px;
                border: 1px solid #DDD;
                border-radius: 4px;
                background: white;
            }
        """

        # Title
        title = QLabel("Packet Analysis")
        title.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Subtitle
        subtitle = QLabel("Sniff and analyze your device's network traffic")
        subtitle.setFont(QFont("Arial", 12))
        subtitle.setStyleSheet("color: #666")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Input fields
        sniff_duration_label = QLabel("Sniff duration:")
        sniff_duration_label.setFont(QFont("Arial", 11))
        self.sniff_duration_input = QLineEdit()
        self.sniff_duration_input.setStyleSheet(self.INPUT_STYLE)
        
        interface_label = QLabel("Network Interface:")
        interface_label.setFont(QFont("Arial", 11))
        self.interface_input = QLineEdit()
        self.interface_input.setStyleSheet(self.INPUT_STYLE)
        
        # Start button
        start_button = QPushButton("Start Sniffing")
        start_button.setStyleSheet(self.BUTTON_STYLE)
        start_button.clicked.connect(self.start_sniffing)
        
        # Add widgets to layout
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addStretch(1)
        layout.addWidget(sniff_duration_label)
        layout.addWidget(self.sniff_duration_input)
        layout.addWidget(interface_label)
        layout.addWidget(self.interface_input)
        layout.addStretch(1)
        layout.addWidget(start_button)
        
        self.setLayout(layout)

    def start_sniffing(self):
        duration = self.sniff_duration_input.text()
        interface = self.interface_input.text()
        self.on_start_callback(duration, interface)