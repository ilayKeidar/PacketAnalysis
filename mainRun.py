import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from GUI.HomeScreen import HomeScreen
from GUI.LoadingScreen import LoadingScreen
from GUI.AnalysisScreen import AnalysisScreen
from user_data import IP_ADDRESS, MAC_ADDRESS


class PacketSnifferGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Packet Analysis")
        self.setFixedSize(500, 400)
        
        # Set up the stacked widget to manage different screens
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        
        # Create and add screens
        self.home_screen = HomeScreen(self.switch_to_loading)
        self.loading_screen = LoadingScreen(self.switch_to_analysis)
        self.analysis_screen = AnalysisScreen()
        
        self.central_widget.addWidget(self.home_screen)
        self.central_widget.addWidget(self.loading_screen)
        self.central_widget.addWidget(self.analysis_screen)

    def switch_to_loading(self, duration, interface):
        self.central_widget.setCurrentIndex(1)
        self.loading_screen.start_progress()

    def switch_to_analysis(self, data=None):
        self.central_widget.setCurrentIndex(2)
        # In real implementation, pass the actual packet data here
        self.analysis_screen.update_data({
            'total_packets': 1512,
            'ip_address': IP_ADDRESS,
            'mac_address': MAC_ADDRESS,
            'tcp_packets': 1024,
            'udp_packets': 486
        })

def main():
    app = QApplication(sys.argv)
    window = PacketSnifferGUI()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()