from collections import defaultdict
from scapy.all import sniff, DNS

from db_handler import insert_packet, insert_frame
from Objects.packet import Packet
from Objects.frame import Frame

count = 0
dns_packets = defaultdict(int) # domain : instances

def dns_analysis(packet):
    dns_packet = packet['DNS']

    if dns_packet.qr == 0:
        dns_info = dns_packet.qd.qname.decode()
        dns_packets[dns_info] += 1


def create_packet_objects(packet, ip_address, mac_address):

    if packet.haslayer('DNS'):
        dns_analysis(packet)  

    global count 
    size = len(packet)

    # if packet.haslayer(TCP) and packet[TCP].dport == 443:  # HTTPS traffic
    # raw_data = bytes(packet[TCP].payload)
    # if b'\x00\x00' in raw_data:  # Check for TLS handshake
    #     sni_offset = raw_data.find(b'\x00\x00') + 5
    #     sni_length = int.from_bytes(raw_data[sni_offset:sni_offset+2], 'big')
    #     sni = raw_data[sni_offset+2:sni_offset+2+sni_length].decode()
    #     print(f"SNI (Domain): {sni}")


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
    print("SNIFFING ENDED\n")

def return_dns():
    return dict(dns_packets)

def return_count():
    return count