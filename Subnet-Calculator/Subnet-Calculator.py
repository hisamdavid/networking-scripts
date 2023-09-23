import sys

def subnet_calc():
    try:

        #Checking IP address validity
        while True:
            ip_address = input(">> Enter an IP address \n>> ")
            
            #Checking octets            
            ip_octets = ip_address.split('.')
                        
            if (len(ip_octets) == 4) and (1 <= int(ip_octets[0]) <= 223) and (int(ip_octets[0]) != 127) and (int(ip_octets[0]) != 169 or int(ip_octets[1]) != 254) and (0 <= int(ip_octets[1]) <= 255 and 0 <= int(ip_octets[2]) <= 255 and 0 <= int(ip_octets[3]) <= 255):
                break
            
            else:
                print("\n>> The IP address is INVALID! Please retry!\n>> ")
                continue
        
        masks = [255, 254, 252, 248, 240, 224, 192, 128, 0]
        
        #Checking Subnet Mask validity
        while True:
            subnet_mask = input(">> Enter a subnet mask \n>> ")
            
            #Checking octets            
            mask_octets = subnet_mask.split('.')
            
            if (len(mask_octets) == 4) and (int(mask_octets[0]) == 255) and (int(mask_octets[1]) in masks) and (int(mask_octets[2]) in masks) and (int(mask_octets[3]) in masks) and (int(mask_octets[0]) >= int(mask_octets[1]) >= int(mask_octets[2]) >= int(mask_octets[3])):
                break
            
            else:
                print("\n>> The subnet mask is INVALID! Please retry!\n")
                continue

        
        #Convert mask to binary string
        mask_octets_binary = []
        for octet in mask_octets:
            binary_octet = bin(int(octet)).lstrip('0b')
            mask_octets_binary.append(binary_octet.zfill(8))
        binary_mask = "".join(mask_octets_binary)  
        
        #Counting host bits in the mask and calculating number of hosts/subnet
        no_of_zeros = binary_mask.count("0")
        no_of_ones = 32 - no_of_zeros
        no_of_hosts = abs(2 ** no_of_zeros - 2)
        
        #Obtaining wildcard mask
        wildcard_octets = []
        for octet in mask_octets:
            wild_octet = 255 - int(octet)
            wildcard_octets.append(str(wild_octet))
        wildcard_mask = ".".join(wildcard_octets)
        
        #Convert IP to binary string
        ip_octets_binary = []
        for octet in ip_octets:
            binary_octet = bin(int(octet)).lstrip('0b')
            ip_octets_binary.append(binary_octet.zfill(8))
        binary_ip = "".join(ip_octets_binary)
    
        #Getting the network address and broadcast address from the binary strings obtained above
        network_address_binary = binary_ip[:(no_of_ones)] + "0" * no_of_zeros
        broadcast_address_binary = binary_ip[:(no_of_ones)] + "1" * no_of_zeros
        
        #Converting everything back to decimal 
        net_ip_octets = []
        
        #range(0, 32, 8) means 0, 8, 16, 24
        for bit in range(0, 32, 8):
            net_ip_octet = network_address_binary[bit: bit + 8]
            net_ip_octets.append(net_ip_octet)
        
        #We will end up with 4 slices of the binary IP address: [0: 8], [8: 16], [16: 24] and [24:31]
        
        net_ip_address = []
        for each_octet in net_ip_octets:
            net_ip_address.append(str(int(each_octet, 2)))
        network_address = ".".join(net_ip_address)
        
        bst_ip_octets = []

        for bit in range(0, 32, 8):
            bst_ip_octet = broadcast_address_binary[bit: bit + 8]
            bst_ip_octets.append(bst_ip_octet)
        
        bst_ip_address = []
        for each_octet in bst_ip_octets:
            bst_ip_address.append(str(int(each_octet, 2)))        
        broadcast_address = ".".join(bst_ip_address)
        
        print("\n")
        print(">> Network address is: %s" % network_address)
        print(">> Broadcast address is: %s" % broadcast_address)
        print(">> Number of valid hosts per subnet: %s" % no_of_hosts)
        print(">> Wildcard mask: %s" % wildcard_mask)
        print(">> Mask bits: %s" % no_of_ones)
        print("\n")
        
        

    except KeyboardInterrupt:
        print("\n\nProgram aborted by user. Exiting...\n")
        sys.exit(1)
        

while True:
    subnet_calc()


