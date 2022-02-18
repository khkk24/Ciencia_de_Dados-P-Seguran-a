#!/usr/bin/python
from scapy.all import *


def conta(filename):
    nb_t = 0
    nb_IP =0
    nb_TCP=0
    nb_UDP=0
    nb_sessoesTCP=0
    nb_sessoesUDP=0
    print( "O arquivo" " trace.pcap" " possui: ")
    for pkt in file:
        if pkt.haslayer(IP):
            nb_t +=1
            if pkt.haslayer(UDP):
                nb_UDP +=1
            if pkt.haslayer(TCP):
                nb_TCP +=1

    print("  pacote no total")
    print(nb_IP, "  pacote IP")
    print(nb_TCP, "  pacotes TCP")
    print("  sessões TCP")
    print( nb_UDP , " sessões UDP")
    print(" pacotes não-IP")


file = rdpcap("trace.pcap")
 
conta(file)


