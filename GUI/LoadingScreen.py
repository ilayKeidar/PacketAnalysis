from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QProgressBar
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont
from constants import button_color


class LoadingScreen(QWidget):
    def __init__(self, on_complete_callback):
        super().__init__()
        self.on_complete_callback = on_complete_callback
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(40, 40, 40, 40)

        # Style constants
        self.MINT_GREEN = button_color

        # Title
        title = QLabel("Sniffing...")
        title.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setStyleSheet(f"""
            QProgressBar {{
                border: none;
                background: #DDD;
                height: 8px;
                border-radius: 4px;
            }}
            QProgressBar::chunk {{
                background: {self.MINT_GREEN};
                border-radius: 4px;
            }}
        """)
        self.progress_bar.setTextVisible(False)
        
        layout.addStretch(1)
        layout.addWidget(title)
        layout.addWidget(self.progress_bar)
        layout.addStretch(1)
        
        self.setLayout(layout)

    def start_progress(self, duration_seconds):
        self.progress = 0
        self.progress_bar.setValue(0)
        
        # Calculate timer interval to have 100 steps over the duration
        self.step_count = 100
        self.timer_interval = int((duration_seconds * 1000) / self.step_count)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(self.timer_interval)  # Convert seconds to milliseconds

    def update_progress(self):
        self.progress += 1
        self.progress_bar.setValue(self.progress)
        if self.progress >= 100:
            self.timer.stop()
            self.on_complete_callback()