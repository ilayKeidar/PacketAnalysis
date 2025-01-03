import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
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
        try:
            self.sniff_duration = float(duration) 
            self.network_interface = interface

            self.central_widget.setCurrentIndex(1)
            self.loading_screen.start_progress(self.sniff_duration)

            sniffing_thread = threading.Thread(target=self.start_sniffing_thread)
            sniffing_thread.start()
            
        except ValueError:
            # Handle invalid duration input
            print("Please enter a valid number for duration")
            return

    def start_sniffing_thread(self):
        # Clear and create the database
        clear_db()
        create_db()

        # Start sniffing in the background
        start_sniffer(self.network_interface, self.sniff_duration, IP_ADDRESS, MAC_ADDRESS)

        # Once sniffing is done, switch to the analysis screen
        self.switch_to_analysis()

    def switch_to_analysis(self, data=None):
        self.central_widget.setCurrentIndex(2)

        protocol_counts, transport_counts = protocol_count()
        dns_queries = return_dns()
        sent, received = get_total_size()

        self.analysis_screen.update_data({
            'total_packets': return_count(),
            'ip_address': IP_ADDRESS,
            'mac_address': MAC_ADDRESS,
            'tcp_packets': transport_counts['TCP'],
            'udp_packets': transport_counts['UDP']
        })

def main():
    app = QApplication(sys.argv)
    window = PacketSnifferGUI()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()