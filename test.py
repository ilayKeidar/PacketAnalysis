from scapy.arch.windows import get_windows_if_list

# Filter out only the active interfaces (those with an IP address assigned)
print("Active network interfaces:")
interfaces = get_windows_if_list()

active_interfaces = [
    iface['name'] for iface in interfaces if iface.get('ips')  
]

for iface in active_interfaces:
    print(iface)
