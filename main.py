from packet_sniffer import start_sniffer
from db_handler import create_db
from user_data import IP_ADDRESS, MAC_ADDRESS
from constants import sniff_time, interface

create_db()

start_sniffer(interface, sniff_time, IP_ADDRESS, MAC_ADDRESS)
