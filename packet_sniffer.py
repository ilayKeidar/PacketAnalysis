from collections import defaultdict
from scapy.all import sniff, DNS, DNSQR

from db_handler import insert_packet, insert_frame
from Objects.packet import Packet
from Objects.frame import Frame

count = 0
dns_queries = defaultdict(int) # domain : instances
snis = defaultdict(int)

def dns_analysis(packet):
    if packet[DNS].opcode == 0:
        if packet.haslayer(DNSQR):
            dns_query = packet[DNSQR].qname.decode('utf-8')
            dns_queries[dns_query] += 1
    else:
        dns_queries["None"] += 1


def create_packet_objects(packet, ip_address, mac_address):
    global count 

    if packet.haslayer(DNS):
        dns_analysis(packet)  

    size = len(packet)

    if packet.haslayer('IP') and (packet.haslayer('TCP') or packet.haslayer('UDP')):        
        src_ip = packet['IP'].src
        dst_ip = packet['IP'].dst
        protocol = packet['IP'].proto
        timestamp = packet['IP'].time

        if packet.haslayer('TCP'):
            src_port = packet['TCP'].sport
            dst_port = packet['TCP'].dport
        elif packet.haslayer('UDP'):
            src_port = packet['UDP'].sport
            dst_port = packet['UDP'].dport
        

        # insert only the packets that are related to the current device
        if src_ip == ip_address or dst_ip == ip_address:
            packet_obj = Packet(src_ip, dst_ip, src_port, dst_port, protocol, size, timestamp)
            insert_packet(packet_obj)
            count += 1
            print(f"{count}. {packet_obj.display()}")
    
    
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


def start_sniffer(interface, sniff_time, ip_address, mac_address):

    def sniffer_wrapper(packet):
        create_packet_objects(packet, ip_address, mac_address)

    sniff(iface=interface, prn=sniffer_wrapper, timeout=sniff_time, store=False)


def return_dns():
    return dict(sorted(dns_queries.items(), key=lambda item: item[1], reverse=True))

def return_count():
    return count

def return_snis():
    return dict(snis)
