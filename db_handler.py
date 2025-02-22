import sqlite3

def clear_db():
    conn = sqlite3.connect("packets.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM packets")  
    conn.commit()
    conn.close()

def create_db():

    conn = sqlite3.connect('packets.db')
    c = conn.cursor()

    # Create table for packets (IP + TCP)
    c.execute('''CREATE TABLE IF NOT EXISTS packets (
                    id INTEGER PRIMARY KEY,
                    src_ip TEXT,
                    dst_ip TEXT,
                    src_port INTEGER,
                    dst_port INTEGER,
                    protocol INTEGER,
                    size INTEGER,
                    timestamp REAL)''')
    
    # Create table for frames (Ethernet)
    c.execute('''CREATE TABLE IF NOT EXISTS frames (
                    id INTEGER PRIMARY KEY,
                    src_mac TEXT,
                    dst_mac TEXT,
                    protocol INTEGER,
                    size INTEGER,
                    timestamp REAL)''')
    
    conn.commit()
    conn.close()

def insert_packet(packet_obj):
    conn = sqlite3.connect('packets.db')
    c = conn.cursor()
    c.execute('''INSERT INTO packets (src_ip, dst_ip, src_port, dst_port, protocol, size, timestamp) 
                 VALUES (?, ?, ?, ?, ?, ?, ?)''', 
              (packet_obj.src_ip, packet_obj.dst_ip, packet_obj.src_port, 
               packet_obj.dst_port, packet_obj.protocol, packet_obj.size, packet_obj.timestamp))
    conn.commit()
    conn.close()

def insert_frame(frame_obj):
    conn = sqlite3.connect('packets.db')
    c = conn.cursor()
    c.execute('''INSERT INTO frames (src_mac, dst_mac, protocol, size, timestamp) 
                 VALUES (?, ?, ?, ?, ?)''', 
              (frame_obj.src_mac, frame_obj.dst_mac, frame_obj.protocol, frame_obj.size, frame_obj.timestamp))
    conn.commit()
    conn.close()
