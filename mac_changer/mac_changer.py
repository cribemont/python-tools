#!/usr/bin/env python
import subprocess
import optparse

# func to get the arguments passed to the command line
def get_arguments():
    parser = optparse.OptionParser
    parser.add_option("-i", "--interface", dest="interface", help="Interface you want to change")
    parser.add_option("-m", "--mac", dest="destination_mac_address", help="Value of the new MAC")
    # parse arguments passed to the command line
    (options, arguments) = parser.parse_args()
    # do we have an interface ?
    if not options.interface:
        # : display error
        parser.error("[-] Please specify an interface with -i or --interface")
    # do we have a new MAC ?
    elif not options.destination_mac_address:
        # : display error
        parser.error("[-] Please specify a MAC address with -m or --mac")
    # proceed
    return options

# main function to update MAC address
def change_mac_address(interface, destination_mac_address):
    print("[+] Changing MAC address to " + destination_mac_address + " for interface " + interface)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", destination_mac_address])
    subprocess.call(["ifconfig", interface, "up"])

# check and get options
options = get_arguments()
# proceed with updating the MAC
change_mac_address(options.interface, options.destination_mac_address)