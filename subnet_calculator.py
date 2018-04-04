import sys
import random

'''ip_address = raw_input("Enter valid IP address: ")
ip_octets = ip_address.split(".")

if (len(ip_octets) == 4) and (1 <= int(ip_octets[0]) <= 223) and (int(ip_octets[0]) != 127) and (int(ip_octets[0]) != 169 or int(ip_octets[1]) != 254) and ((0 <= int(ip_octets[1]) <=255) and (0 <= int(ip_octets[2]) <=255) and (0 <= int(ip_octets[3]) <=255)):
    print "IP address is valid"


else:
    print "IP address is invalid"'''

subnet_mask = raw_input("Enter valid subnet mask: ")
subnet_octets = subnet_mask.split(".")

possible_subnets = [255, 254, 252, 248, 240, 224, 192, 128, 0]

if (len(subnet_octets) == 4) and (int(subnet_octets[0]) == 255) and ((int(subnet_octets[1]) in possible_subnets) and (int(subnet_octets[2]) in possible_subnets) and (int(subnet_octets[3]) in possible_subnets)) and (int(subnet_octets[0]) >= int(subnet_octets[1]) >= int(subnet_octets[2]) >= int(subnet_octets[3])):
    print "Subnet mask is valid"

else:
    print "Subnet mask is invalid"

# To convert subnet mask into binary

final_bin_mask = []
dec_mask = subnet_mask.split(".")

for index in range(0, len(dec_mask)):
    bin_mask = bin(int(dec_mask[index])).split('b')[1]

    if len(bin_mask) == 8:
        final_bin_mask.append(bin_mask)

    elif len(bin_mask) < 8:
        padded_octet = bin_mask.zfill(8)
        final_bin_mask.append(padded_octet)

complete_bin_mask = "".join(final_bin_mask)
print complete_bin_mask

# Calculate number of hosts per subnet

no_of_zeros = complete_bin_mask.count("0")
no_of_hosts = (2 ** (no_of_zeros) - 2)

print no_of_hosts

# Calculate wild card mask
wild_card_mask = []

for index in range(0, len(dec_mask)):
    wild_card_octet = 255 - int(dec_mask[index])
    wild_card_mask.append(str(wild_card_octet))

final_wild_card_mask = ".".join(wild_card_mask)

print final_wild_card_mask