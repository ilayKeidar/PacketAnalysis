# packets - dst IP
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
# Frame Protocols 
type_to_protocol = {
    2054: 'ARP',
    2048: 'IPv4',
    1: 'ICMP'
}
