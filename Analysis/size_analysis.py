import sqlite3
from user_data import IP_ADDRESS

MAC_ADDRESS = '9a:22:ef:fa:fa:b7'

# convert the bytes to the relevant unit
def convert_bytes(bytes):
    units = ["B", "KB", "MB", "GB"]

    unit_index = 0
    while bytes >= 1024:
        bytes /= 1024
        unit_index += 1
    
    bytes = round(bytes, 2)
    
    return f"{bytes} {units[unit_index]}"


def get_total_size():

    conn = sqlite3.connect('packets.db')
    c = conn.cursor()

    received = 0
    sent = 0

    c.execute('SELECT src_ip, dst_ip, size FROM packets')
    packets = c.fetchall()

    for packet in packets:
        if packet[0] == IP_ADDRESS:
            sent += packet[2]
        elif packet[1] == IP_ADDRESS:
            received += packet[2]
            
    conn.close()

    sent = convert_bytes(sent)
    received = convert_bytes(received)

    return sent, received
