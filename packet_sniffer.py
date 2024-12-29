from scapy.all import sniff
from packet import Packet
from frame import Frame

sniff_time = 30
packet_objects = []

def create_packet_objects(packet):
    if packet.haslayer('IP') and packet.haslayer('TCP'):
        src_ip = packet['IP'].src
        dst_ip = packet['IP'].src
        src_port = packet['TCP'].sport
        dst_port = packet['TCP'].dport
        protocol = packet['IP'].proto
        timestamp = packet['IP'].time

        packet_obj = Packet(src_ip, dst_ip, src_port, dst_port, protocol, timestamp)
        packet_objects.append(packet_obj)
    
    elif packet.haslayer("Ether"):
        src_mac = packet["Ether"].src  # Source MAC address
        dst_mac = packet["Ether"].dst 
        protocol = packet['IP'].proto
        
        frame_obj = Frame(src_mac, dst_mac, protocol)
        packet_objects.append(frame_obj)

sniff(iface="Wi-Fi", prn=create_packet_objects, timeout=sniff_time) 
    
for packet in packet_objects:
    print(packet.display())