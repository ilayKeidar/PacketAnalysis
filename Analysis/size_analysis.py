import sqlite3
from Sniffing.user_data import IP_ADDRESS, MAC_ADDRESS


def get_total_size():

    conn = sqlite3.connect('packets.db')
    c = conn.cursor()

    received = 0
    sent = 0

    c.execute('SELECT * FROM packets')
    packets = c.fetchall()

    for src_ip, dst_ip, size in packets:
        if src_ip == IP_ADDRESS:
            sent += size
        elif dst_ip == IP_ADDRESS:
            received += size
            
    conn.close()

    print(f"sent: {sent} bytes")
    print(f"received: {received} bytes")    


get_total_size()
