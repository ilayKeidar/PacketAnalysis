from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())  # Display a one-line summary of each packet

# Start sniffing packets
print("Sniffing packets... Press Ctrl+C to stop.")
sniff(prn=packet_callback, timeout=20)  # Capture 10 packets
