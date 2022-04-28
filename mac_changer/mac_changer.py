#!/usr/bin/env python
import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser
    parser.add_option("-i", "--interface", dest="interface", help="Value of the interface you want to change")
    parser.add_option("-m", "--mac", dest="destination_mac_address", help="Value of the new MAC")
    return parser.parse_args()


def change_mac_address(interface, destination_mac_address):
    print("[+] Changing MAC address to " + destination_mac_address + " for interface " + interface)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", destination_mac_address])
    subprocess.call(["ifconfig", interface, "up"])


(options, arguments) = get_arguments()
change_mac_address(options.interface, options.destination_mac_address)