from scapy.all import sniff, DNS, DNSQR

def process_packet(packet, dns_queries):
    """Process a single packet to extract DNS queries and add them to a dictionary."""
    if packet.haslayer(DNS) and packet[DNS].opcode == 0:  # Check if it's a DNS query
        dns_query = packet[DNSQR].qname.decode('utf-8')
        if dns_query not in dns_queries:
            dns_queries[dns_query] = 1
        else:
            dns_queries[dns_query] += 1


dns_queries = {}
print("Sniffing DNS queries... Press Ctrl+C to stop.")
sniff(filter="udp port 53", prn=lambda pkt: process_packet(pkt, dns_queries), store=False, timeout=20)  # Sniff DNS traffic
print("\nStopping sniffing.")
print("\nDNS Queries:")
for query, count in dns_queries.items():
    print(f"{query}: {count}")
