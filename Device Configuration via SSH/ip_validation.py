import os.path
import sys
import subprocess

#Checking IP address file 
def ip_file_valid():
    # Prompting the user to enter the IP file path and name
    ip_file = input("\n>> Enter IP file path and name (e.g. D:\Networking\ip_address.txt)\n>> ")

    print("\n>> checking adrress....\n")
    # Checking if the specified file exists
    if not os.path.isfile(ip_file):
        print("\n>> File {} does not exist :(\n".format(ip_file))
        sys.exit(1)
    
    # Opening the file in read mode using a context manager
    with open(ip_file, 'r') as selected_ip_file:
        # Reading all the lines (IP addresses) in the file
        ip_list = selected_ip_file.readlines()
        
    return ip_list



#Checking octets
def ip_addr_valid(list):
    # looping all the ip and check them
    for ip in list:
        ip = ip.rstrip("\n")
        octet_list = ip.split('.')
        # check if ip is valid unicast addres
        if (len(octet_list) == 4) and (1 <= int(octet_list[0]) <= 223) and (int(octet_list[0]) != 127) and (int(octet_list[0]) != 169 or int(octet_list[1]) != 254) and (0 <= int(octet_list[1]) <= 255 and 0 <= int(octet_list[2]) <= 255 and 0 <= int(octet_list[3]) <= 255):
            continue
        # giving indecators about the error
        else:
            print('\n>> There was an invalid IP address in the file: {} :(\n'.format(ip))
            sys.exit(1)



#Checking IP reachability
def ip_reach(list):

    # looping all the ip and check them
    for ip in list:
        ip = ip.rstrip("\n")
        
        # Executing the ping command
        ping_reply = subprocess.call('ping %s -n 2' % (ip,), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        if ping_reply == 0:
            print("\n>> {} is reachable :)\n".format(ip))
            continue
        
        else:
            print('\n>> {} not reachable check connectivity and try again :( \n'.format(ip))
            sys.exit(1)