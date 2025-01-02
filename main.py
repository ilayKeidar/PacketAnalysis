from packet_sniffer import start_sniffer, return_dns, return_count
from db_handler import create_db, clear_db
from user_data import IP_ADDRESS, MAC_ADDRESS
from constants import sniff_time, interface
from Analysis.size_analysis import get_total_size
from Analysis.protocol_analysis import protocol_count

clear_db()
create_db()

start_sniffer(interface, sniff_time, IP_ADDRESS, MAC_ADDRESS)

print("Device monitored:")
print(f"IP address: {IP_ADDRESS}")
print(f"MAC address: {MAC_ADDRESS}")
print("======================")
print(f"Sniffing duration: {sniff_time} seconds")
print(f"Interface sniffed: {interface}")
print(f"Total packets captured: {return_count()}")
print("======================")

sent, received = get_total_size()
protocol_counts, transport_counts = protocol_count()

print("Total Data Transferred:")
print(f"Sent: {sent}")
print(f"Received: {received}")    
print("======================")

print("Active Protocols:")
print(protocol_counts)
print("Transport Counts:", transport_counts)

#print(return_dns())
