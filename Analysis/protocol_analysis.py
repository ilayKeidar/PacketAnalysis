from collections import defaultdict
import sqlite3

# based on port
port_to_protocol = {
    20: 'FTP',
    21: 'FTP',
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP',
    53: 'DNS',
    67: 'DHCP (Server)',
    68: 'DHCP (Client)',
    80: 'HTTP',
    110: 'POP3',
    143: 'IMAP',
    443: 'HTTPS',
    445: 'SMB',
    3389: 'RDP',
    8080: 'HTTP',
    8443: 'HTTPS',
    8888: 'HTTP',
}

# based on scapy protocol numbering
type_to_protocol = {
    2054: 'ARP',
    2048: 'IPv4',
    1: 'ICMP',
    6: 'TCP',
    17: 'UDP'
}

# count the amount of packets per protocol, as well as how many UDP and TCP packets
def protocol_count():
    conn = sqlite3.connect('packets.db')
    c = conn.cursor()

    c.execute('SELECT src_port, dst_port, protocol FROM packets')
    packets = c.fetchall()

    protocolCountMap = defaultdict(int) # protocol number : count
    
    transport_counter = {
        'TCP': 0,
        'UDP': 0
    }

    for packet in packets:
        src_port = packet[0]
        dst_port = packet[1]
        transport_protocol =  packet[2]
        if src_port in port_to_protocol:
            protocolCountMap[port_to_protocol[src_port]] += 1

        if dst_port in port_to_protocol:
            protocolCountMap[port_to_protocol[dst_port]] += 1

        if transport_protocol in type_to_protocol:
            transport_counter[type_to_protocol[transport_protocol]] += 1        
    
    conn.close()

    return dict(protocolCountMap), transport_counter

