from scapy.all import sniff
from db_handler import insert_packet, insert_frame

import constants
from packet import Packet
from frame import Frame


def create_packet_objects(packet):

    if packet.haslayer('IP') and packet.haslayer('TCP'):
        src_ip = packet['IP'].src
        dst_ip = packet['IP'].dst
        src_port = packet['TCP'].sport
        dst_port = packet['TCP'].dport
        protocol = packet['IP'].proto
        timestamp = packet['IP'].time

        packet_obj = Packet(src_ip, dst_ip, src_port, dst_port, protocol, timestamp)
        insert_packet(packet_obj)
        print(packet_obj.display())

    
    elif packet.haslayer("Ether"):
        src_mac = packet["Ether"].src  
        dst_mac = packet["Ether"].dst 
        timestamp = packet["Ether"].time
        protocol = packet["Ether"].type

        frame_obj = Frame(src_mac, dst_mac, protocol, timestamp)
        insert_frame(frame_obj)
        print(frame_obj.display())

sniff(iface=constants.interface, prn=create_packet_objects, timeout=constants.sniff_time) 
