from scapy.all import sniff

from db_handler import insert_packet, insert_frame
import Sniffing.constants as constants
from Objects.packet import Packet
from Objects.frame import Frame
from Sniffing.user_data import IP_ADDRESS, MAC_ADDRESS


def create_packet_objects(packet, ip_address, mac_address):

    size = len(packet)

    if packet.haslayer('IP') and packet.haslayer('TCP'):
        src_ip = packet['IP'].src
        dst_ip = packet['IP'].dst
        src_port = packet['TCP'].sport
        dst_port = packet['TCP'].dport
        protocol = packet['IP'].proto
        timestamp = packet['IP'].time

        # insert only the packets that are related to the current device
        if src_ip == ip_address or dst_ip == ip_address:
            packet_obj = Packet(src_ip, dst_ip, src_port, dst_port, protocol, size, timestamp)
            insert_packet(packet_obj)
            print(packet_obj.display())
    
    
    elif packet.haslayer("Ether"):
        src_mac = packet["Ether"].src  
        dst_mac = packet["Ether"].dst 
        timestamp = packet["Ether"].time
        protocol = packet["Ether"].type

        if src_mac == mac_address or dst_mac == mac_address:
            frame_obj = Frame(src_mac, dst_mac, protocol, size, timestamp)
            insert_frame(frame_obj)
            print(frame_obj.display())

    return create_packet_objects

def sniffer_wrapper(packet):
    create_packet_objects(packet, IP_ADDRESS, MAC_ADDRESS)   

# sniffer = create_sniffer(IP_ADDRESS, MAC_ADDRESS)
print(IP_ADDRESS)  
print(MAC_ADDRESS)

sniff(iface=constants.interface, prn=sniffer_wrapper, timeout=constants.sniff_time) 

