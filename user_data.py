import socket
import uuid
from scapy.arch.windows import get_windows_if_list

def getUserIP():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(("8.8.8.8", 80)) 
        return s.getsockname()[0]   


def getUserMAC():
    return ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0, 48, 8)][::-1])

IP_ADDRESS = getUserIP()
MAC_ADDRESS = getUserMAC()


# Filter out only the active interfaces (those with an IP address assigned)

def getActiveInterfaces():
    interfaces = get_windows_if_list()

    active_interfaces = [
        iface['name'] for iface in interfaces if iface.get('ips')  
    ]

    return active_interfaces

INTERFACES = getActiveInterfaces()