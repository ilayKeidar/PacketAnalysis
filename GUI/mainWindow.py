import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class ModernGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Packet Analyzer")
        self.setGeometry(100, 100, 500, 300)
        self.setStyleSheet("background-color: #2C3E50;")  # Dark background

        # Title label
        self.title = QLabel("Packet Analyzer", self)
        self.title.setAlignment(Qt.AlignCenter)
        title_font = QFont("Arial", 38, QFont.Bold)
        self.title.setFont(title_font)
        self.title.setStyleSheet("color: white;")

        # Subtitle label
        self.subtitle = QLabel("Sniff and analyze your device's network traffic", self)
        self.subtitle.setAlignment(Qt.AlignCenter)
        subtitle_font = QFont("Arial", 12)
        self.subtitle.setFont(subtitle_font)
        self.subtitle.setStyleSheet("color: white;")
    
        # Button
        self.button = QPushButton("Start sniffing", self)
        self.button.setFixedSize(200, 60)
        button_font = QFont("Arial", 16)
        self.button.setFont(button_font)
        self.button.setStyleSheet("""
            QPushButton {
                background-color: #3498DB;
                color: white;
                font-size: 18px;
                font-weight: bold;
                border-radius: 30px;
                border: none;
            }
            QPushButton:hover {
                background-color: #2980B9;
            }
        """)
        self.button.clicked.connect(self.start_sniffing)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.title, alignment=Qt.AlignCenter)  # Title at the top
        layout.addWidget(self.subtitle, alignment=Qt.AlignCenter)  # Subtitle directly below the title
        
        layout.addWidget(self.button, alignment=Qt.AlignCenter)
        layout.setSpacing(-10)
        self.setLayout(layout)

    def start_sniffing(self):
        print("Started sniffing!")

# Create the application and main window
app = QApplication(sys.argv)
window = ModernGUI()
window.show()

sys.exit(app.exec_())
