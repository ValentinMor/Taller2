def modify_source_mac(packet):
    if packet['ARP']['src.proto_ipv4'] == '172.31.0.164':
        packet['ARP']['src.hw_mac'] = '02:da:df:ed:63:c4'
        return packet