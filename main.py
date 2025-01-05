import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt6.QtCore import QTimer
from GUI.HomeScreen import HomeScreen
from GUI.LoadingScreen import LoadingScreen
from GUI.AnalysisScreen import AnalysisScreen
from user_data import IP_ADDRESS, MAC_ADDRESS
from packet_sniffer import start_sniffer, return_dns, return_count
from Analysis.protocol_analysis import protocol_count
from db_handler import create_db, clear_db
from Analysis.size_analysis import get_total_size
import threading

class PacketSnifferGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Packet Analysis")
        self.setFixedSize(600, 700)
        
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
        
        # Initialize thread-related variables
        self.sniffing_thread = None
        self.sniffing_complete = False

    def switch_to_loading(self, duration, interface):
        try:
            self.sniff_duration = float(duration) 
            self.network_interface = interface
            self.sniffing_complete = False

            self.central_widget.setCurrentIndex(1)
            self.loading_screen.start_progress(self.sniff_duration)

            # Create and start the sniffing thread
            self.sniffing_thread = threading.Thread(target=self.start_sniffing_thread)
            self.sniffing_thread.daemon = True  # Make thread daemon so it closes with main app
            self.sniffing_thread.start()

            # Start a timer to check when sniffing is complete
            self.check_timer = QTimer()
            self.check_timer.timeout.connect(self.check_sniffing_complete)
            self.check_timer.start(100)  # Check every 100ms

        except ValueError:
            print("Please enter a valid number for duration")
            return

    def start_sniffing_thread(self):
        try:
            # Clear and create the database
            clear_db()
            create_db()

            # Start sniffing in the background
            start_sniffer(self.network_interface, self.sniff_duration, IP_ADDRESS, MAC_ADDRESS)
            
            # Set flag when complete
            self.sniffing_complete = True
        except Exception as e:
            print(f"Error in sniffing thread: {e}")
            self.sniffing_complete = True  # Set to True to exit loading screen

    def check_sniffing_complete(self):
        if self.sniffing_complete:
            self.check_timer.stop()
            self.switch_to_analysis()

    def switch_to_analysis(self):
        try:
            # Ensure we're on the main thread for GUI updates
            self.central_widget.setCurrentIndex(2)

            protocol_counts, transport_counts = protocol_count()
            dns_queries = return_dns()
            sent, received = get_total_size()

            self.analysis_screen.update_data({
                'total_packets': return_count(),
                'ip_address': IP_ADDRESS,
                'mac_address': MAC_ADDRESS.upper(),
                'tcp_packets': transport_counts.get('TCP', 0),
                'udp_packets': transport_counts.get('UDP', 0),
                'data_sent': sent,
                'data_received': received,
                'dns_queries': dns_queries,
                'protocols': protocol_counts
            })
        except Exception as e:
            print(f"Error in switch_to_analysis: {e}")

    def closeEvent(self, event):
        # Clean up before closing
        if self.sniffing_thread and self.sniffing_thread.is_alive():
            self.sniffing_complete = True
            self.sniffing_thread.join(timeout=1.0)
        event.accept()

def main():
    app = QApplication(sys.argv)
    window = PacketSnifferGUI()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()