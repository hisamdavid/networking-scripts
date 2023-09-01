import sys
import time
from ip_validation import ip_file_valid , ip_addr_valid , ip_reach
from ssh_connection import ssh_connection
from create_threads import create_threads

#Saving the list of IP addresses in ip.txt to a variable
ip_list = ip_file_valid()

#Verifying the validity of each IP address in the list
try:
    ip_addr_valid(ip_list)
    
except KeyboardInterrupt:
    print("\n\n>> Program aborted by user. Exiting....\n")
    sys.exit(1)

#Verifying the reachability of each IP address in the list
try:
    ip_reach(ip_list)
    
except KeyboardInterrupt:
    print("\n\n>> Program aborted by user. Exiting....\n")
    sys.exit(1)

#Calling threads creation function for one or multiple SSH connections
while True:
    create_threads(ip_list, ssh_connection)
    time.sleep(8)

