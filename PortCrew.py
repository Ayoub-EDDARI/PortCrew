#!/usr/bin/env python

# -*- coding: utf-8 -*-
###########################################################################
#           ____  _____  ____  ____  ___  ____  ____  _    _              #
#          (  _ \(  _  )(  _ \(_  _)/ __)(  _ \( ___)( \/\/ )             #
#           )___/ )(_)(  )   /  )( ( (__  )   / )__)  )    (              #
#          (__)  (_____)(_)\_) (__) \___)(_)\_)(____)(__/\__)             #
#              Basic Port Scanner       By Ayoub EDDARI                   #
#                                                                         #
###########################################################################

# Disclaimer: Do Not Use this program for illegal purposes ;)

import os # File management
import sys # Command-line
import socket
import subprocess
import getopt
import time,datetime
# Configuration
from color import bcolors # Console colors
from header import Header #Header

start = time.time()

subprocess.call("clear",shell=True) # Clear

Header().first_title() # Print the title
def usage():
    print """ 
Targets:
     -t, --target    target IP address (e.g. '192.168.0.1')
Others:
     -v, --version   show version
     -h, --help      show this help
Examples:"""
    print "     "+ os.path.basename(sys.argv[0]) +" -t 192.168.0.1"

def version():
    print "PortCrew tool v0.2 - Simple Port Scanner\n\nAuthor: Ayoub EDDARI a.eddari@mail.com\n\nUsage: " + os.path.basename(sys.argv[0]) + " -t <IP>"  

if __name__ == "__main__":
    # command line arguments
    
    if sys.argv[1:]:
        try:
            optlist, args = getopt.getopt(sys.argv[1:], 'v:h:t', ["version","help","target"])
        except getopt.GetoptError as err:
            # print help information and exit:
            print bcolors.R
            print (err) # print something like "option -a not recognized"
            print bcolors.W
            usage()
            sys.exit()  
        for o, a in optlist:
            if o in ("-v", "--version"):
                version()
                sys.exit()
            elif o in ("-h", "--help"):
                usage()
                sys.exit()
            elif o in("-t", "--target"):
                add = args[0]
            else:
                usage()
                sys.exit()
    else:
        usage()
        sys.exit(0)

ip=0
# Print Date & Time
print bcolors.YL + "[+] " + bcolors.B +"Date & Time: "+ time.strftime('%d/%m/%Y %H:%M:%S') 
try:

    print bcolors.YL + "[+] " + bcolors.R + "Scaning " + bcolors.G + add + bcolors.R + " ..."
    for port in range(0,65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex( (add, port) )
        try:
            if result == 0:
                print bcolors.YL + "[+] " + bcolors.W +"Port " + bcolors.R + str(port) + bcolors.G + " Open in " + bcolors.R + add
                ip = ip+1
            sock.close()
        except KeyboardInterrupt:
            print bcolors.YL + "[+] " +"Bye! Quitting.."
    if ip==0:
       print bcolors.G + " No Port open in " + bcolors.R + add
    elif ip==1:
       print bcolors.G + " One Port open in " + bcolors.R + add
    else :
       print bcolors.YL + " [" + str(ip) + "]" + bcolors.G + " Pors open " 
    end = time.time()
    diffTime = end - start
    print bcolors.B + "Completed in: " + bcolors.G +str(datetime.timedelta(seconds=diffTime)).split(".")[0]
except KeyboardInterrupt:
    print bcolors.YL +"\nBye! Quitting.."
    end = time.time()
    diffTime = end - start
    print bcolors.B + "Completed in: " + bcolors.G +str(datetime.timedelta(seconds=diffTime)).split(".")[0]
sys.exit(0)
