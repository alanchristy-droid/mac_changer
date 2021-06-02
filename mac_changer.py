#!/usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():

    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-a", "--address", dest="new_mac", help="New MAC address value")
    (option, arguments) = parser.parse_args()
    if not option.interface:
        parser.error("[-]Did not enter the interface value\n")
    elif not option.new_mac:
        parser.error("[-]Did not enter the MAC value\n")
    return option



def change_mac(interface, new_mac):

    print("[+] Changing MAC address for " + interface + " to " + new_mac + "\n")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
  #  subprocess.call(["ifconfig", interface])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])

    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-]Enter valid interface with MAC address\n")


option = get_arguments()
current_mac = get_current_mac(option.interface)
print("[+]Current MAC = " + str(current_mac) + "\n")

change_mac(option.interface, option.new_mac)

current_mac = get_current_mac(option.interface)
if current_mac == option.new_mac:
    print("[+]MAC address successfully changed to " + str(current_mac) + "\n")
else :
    print("[-]MAC changing unsuccessfull\n")
