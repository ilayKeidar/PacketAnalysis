from packet_sniffer import start_sniffer, return_dns, return_count, return_snis
from db_handler import create_db, clear_db
from user_data import IP_ADDRESS, MAC_ADDRESS
from constants import sniff_time, interface
from Analysis.size_analysis import get_total_size
from Analysis.protocol_analysis import protocol_count

clear_db()
create_db()

start_sniffer(interface, sniff_time, IP_ADDRESS, MAC_ADDRESS)

print("\n======================")
print("SNIFFING DONE")
print("======================")

print("\nDevice monitored:")
print(f"IP address: {IP_ADDRESS}")
print(f"MAC address: {MAC_ADDRESS}")

print(f"\nSniffing duration: {sniff_time} seconds")
print(f"Interface sniffed: {interface}")
print(f"Total packets captured: {return_count()}")
print("======================")

sent, received = get_total_size()
protocol_counts, transport_counts = protocol_count()
dns_queries = return_dns()


print("Total Data Transferred:")
print(f"Sent: {sent}")
print(f"Received: {received}")    


print("\nActive Protocols:")
for protocol in protocol_counts:
    print(f"{protocol}: {protocol_counts[protocol]} packets")

print("\nTransport Counts:")
for protocol in transport_counts:
    print(f"{protocol}: {transport_counts[protocol]} packets")



print("\nDNS queries: ")
for query in dns_queries:
    print(f"{query[:-1]} ({dns_queries[query]} queries)")

