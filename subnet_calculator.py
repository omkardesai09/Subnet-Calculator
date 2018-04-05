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
#print complete_bin_mask

# Calculate number of hosts per subnet

no_of_zeros = complete_bin_mask.count("0")
no_of_hosts = (2 ** (no_of_zeros) - 2)

#print no_of_hosts

# Calculate wild card mask
wild_card_mask = []

for index in range(0, len(dec_mask)):
    wild_card_octet = 255 - int(dec_mask[index])
    wild_card_mask.append(str(wild_card_octet))

final_wild_card_mask = ".".join(wild_card_mask)

#print final_wild_card_mask

# Convert IP address in binary

final_bin_ip = []

for index in range(0, len(ip_octets)):
    bin_ip = bin(int(ip_octets[index])).split("b")[1]

    if len(bin_ip) == 8:
        final_bin_ip.append(bin_ip)

    elif len(bin_ip) < 8:
        padded_ip = bin_ip.zfill(8)
        final_bin_ip.append(padded_ip)

complete_bin_ip = "".join(final_bin_ip)

#print "IP address in binary: " + complete_bin_ip

# Get Network IP address

network_bin_octets = []
no_of_ones = 32 - no_of_zeros

network_addr = complete_bin_ip[0:no_of_ones] + "0" * no_of_zeros

for i in range(0, len(network_addr), 8):
    bin_octet = network_addr[i:i+8]
    network_bin_octets.append(bin_octet)

#print network_bin_octets

network_dec_octets = []
for i in range(0, len(network_bin_octets)):
    dec_ip = str(int(network_bin_octets[i],2))
    network_dec_octets.append(dec_ip)

final_network_addr = ".".join(network_dec_octets)

#print final_network_addr

# Get Broadcast IP address

broadcast_bin_octets = []

broadcast_addr = complete_bin_ip[0:no_of_ones] + "1" * no_of_zeros

for i in range(0, len(broadcast_addr), 8):
    b_bin_octet = broadcast_addr[i:i+8]
    broadcast_bin_octets.append(b_bin_octet)

#print broadcast_bin_octets

broadcast_dec_octets = []
for i in range(0, len(broadcast_bin_octets)):
    dec_broadcast_ip = str(int(broadcast_bin_octets[i],2))
    broadcast_dec_octets.append(dec_broadcast_ip)

final_broadcast_addr = ".".join(broadcast_dec_octets)

#print final_broadcast_addr

# Print Final result

print "IP address: " + ip_address
print "Subnet mask: " + subnet_mask
print "Wild card mask: " + final_wild_card_mask
print "Network address: " + final_network_addr
print "Broadcast address: " + final_broadcast_addr
print "Number of hosts per subnet: " + str(no_of_hosts)

# Generate random IP addresses in same subnet

choice = raw_input("Do you want to generate random IP address in same subnet(y/n): ")

random_ip_range = []
if choice == 'y':

    for obj_nw_index, obj_nw_value in enumerate(network_dec_octets):
        for obj_br_index, obj_br_value in enumerate(broadcast_dec_octets):
            if obj_nw_index == obj_br_index:
                if obj_nw_value == obj_br_value:
                    random_ip_range.append(obj_nw_value)

                else:
                    random_ip_range.append(str(random.randint(int(obj_nw_value), int(obj_br_value))))

print "Random IP address is: " + str(".".join(random_ip_range))


