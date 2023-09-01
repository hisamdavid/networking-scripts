import paramiko
import os.path
import time
import sys
import re


#Verifying the validity of the USERNAME/PASSWORD file
user_file = input("\n>> Enter user file path and name (e.g. D:\\Networking\\admin.txt)\n>> ")

if not os.path.isfile(user_file):
    print("\n>> File {} does not exist :(\n".format(user_file))
    sys.exit(1)

#Verifying the validity of the COMMANDS FILE
cmd_file = input("\n>> Enter commands file path and name (e.g. D:\\Networking\\commands.txt)\n>> ")

if not os.path.isfile(cmd_file):
    print("\n* File {} does not exist :(\n".format(cmd_file))
    sys.exit(1)

#Open SSHv2 connection to the device
def ssh_connection(ip):
    
    global user_file
    global cmd_file
    
    #Creating SSH CONNECTION
    try:
        
        #Reading the username/password from the file
        with open(user_file, 'r') as selected_user_file:
            cardnitals = selected_user_file.readlines()[0]
            username =cardnitals.split(',')[0].rstrip("\n")
            password = cardnitals.split(',')[1].rstrip("\n")
        
        #Logging into device
        session = paramiko.SSHClient()
        
        #Do not use in production! this allows auto-accepting unknown host keys some security problems may ocors plz test more a batter parameter would be reject policy
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        session.connect(ip.rstrip("\n"), username = username, password = password)
        connection = session.invoke_shell()	
        
        #Setting terminal length for entire output - disable pagination
        connection.send("enable\n")
        connection.send("terminal length 0\n")
        time.sleep(1)
        
        #Entering global config mode
        connection.send("\n")
        connection.send("configure terminal\n")
        time.sleep(1)
        
        #Open user selected file for reading
        with open(cmd_file, 'r') as selected_cmd_file:
            for each_line in selected_cmd_file.readlines():
                connection.send(each_line + '\n')
                time.sleep(2)

        #Checking command output for IOS syntax errors
        router_output = connection.recv(65535)
        
        if re.search(b"% Invalid input", router_output):
            print(">> There was at least one IOS syntax error on device {} :(\n".format(ip))
            
        else:
            print(">> DONE for device {} :)\n".format(ip))

        #Test for reading command output
        print(str(router_output) + "\n")
        
        #Closing the connection
        session.close()

    except paramiko.AuthenticationException:
        print(">> Invalid username or password :( \n>> Please check the username/password file or the device configuration.")
        print(">> Closing program....")