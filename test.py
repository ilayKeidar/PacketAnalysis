from scapy.all import sniff, DNS

def packet_callback(packet):
    if packet.haslayer(DNS):  # Check if the packet contains a DNS layer
        print(packet.summary())  # Print a summary of the DNS packet

# Start sniffing packets
print("Sniffing DNS packets... Press Ctrl+C to stop.")
sniff(filter="udp port 53", prn=packet_callback, store=False)
