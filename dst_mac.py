
def modify_destiny_mac(packet):
    if packet['ARP']['src.proto_ipv4'] == '172.31.0.164':
        packet['ARP']['dst.hw_mac'] = '02:01:ee:be:47:19'
        return packet