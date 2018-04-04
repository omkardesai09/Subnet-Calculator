import sys
import random

ip_address = raw_input("Enter valid IP address: ")
ip_octets = ip_address.split(".")

if (len(ip_octets) == 4) and (1 <= int(ip_octets[0]) <= 223) and (int(ip_octets[0]) != 127) and (int(ip_octets[0]) != 169 or int(ip_octets[1]) != 254) and ((0 <= int(ip_octets[1]) <=255) and (0 <= int(ip_octets[2]) <=255) and (0 <= int(ip_octets[3]) <=255)):
    print "IP address is valid"


else:
    print "IP address is invalid"

subnet_mask = raw_input("Enter valid subnet mask: ")
subnet_octets = subnet_mask.split(".")

possible_subnets = [255, 254, 252, 248, 240, 224, 192, 128, 0]

if (len(subnet_octets) == 4) and (int(subnet_octets[0]) == 255) and ((int(subnet_octets[1]) in possible_subnets) and (int(subnet_octets[2]) in possible_subnets) and (int(subnet_octets[3]) in possible_subnets)) and (int(subnet_octets[0]) >= int(subnet_octets[1]) >= int(subnet_octets[2]) >= int(subnet_octets[3])):
    print "Subnet mask is valid"

else:
    print "Subnet mask is invalid"
