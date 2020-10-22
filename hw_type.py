def modify_hw_type(packet):
    if packet['ARP']['src.proto_ipv4'] == '172.31.0.164':
        packet['ARP']['hw_type'] = '2'
        return packet                      