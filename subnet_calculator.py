import sys
import random

ip_address = raw_input("Enter valid IP address: ")
ip_octets = ip_address.split(".")

if (len(ip_octets) == 4) and (1 <= int(ip_octets[0]) <= 223) and (int(ip_octets[0]) != 127) and (int(ip_octets[0]) != 169 or int(ip_octets[1]) != 254) and ((0 <= int(ip_octets[1]) <=255) and (0 <= int(ip_octets[2]) <=255) and (0 <= int(ip_octets[3]) <=255)):
    print "IP address is valid"


else:
    print "IP address is invalid"
