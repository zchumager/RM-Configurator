#!/usr/bin/python3


import argparse
import nmap
import broadlink
from errno import ENETUNREACH


def setup_rm(ssid, password, sec_mode):
    """
    :param ssid: WiFi SSID
    :param password: WiFi Password
    :param sec_mode: WiFi Security Mode
    :return:
    """
    try:
        broadlink.setup(ssid, password, sec_mode)
    except IOError as e:
        if e.errno == ENETUNREACH:
            print("sending packages")


def get_rm_info(devices):
    """
    :param devices: A List of broadlink objects
    :return: a dict with the first broadlink object found
    """
    print("RM INFO")

    model = devices[0].model
    ip_address = devices[0].host[0]
    bin_mac = devices[0].mac
    mac_address = ':'.join(format(e, '02x').upper() for e in bin_mac)
    raw_mac = mac_address.replace(":", "").lower()

    return {
        "model": model,
        "ip_address": ip_address,
        "binary_mac": bin_mac,
        "mac_address": mac_address,
        "raw_mac": raw_mac
    }


def discover_devices():
    devices = broadlink.discover(timeout=5)
    if len(devices) > 0:
        rm_info = get_rm_info(devices)
        print(f"Device Information: {rm_info}")
    else:
        print("No device was found on the network")


def get_used_ips(network_mask):
    '''
        :param network_mask: the valid network mask where computer is connected like 192.168.x.y/24
    '''
    nm = nmap.PortScanner()

    host_dict = nm.scan(hosts=network_mask, arguments='-n -sP -PE').get('scan')
    host_list = host_dict.keys()

    for host in host_list:
        print(host)


def main():
    parser = argparse.ArgumentParser(description='RM Mini Configurator Python CLI Tool')

    parser.add_argument('--ssid', help="WiFi SSID")
    parser.add_argument('--password', help="WiFi Password")
    parser.add_argument('--mode', help="WiFi Security Mode")
    parser.add_argument('--get', help="Get details for an already configured RM Mini", action="store_true")
    parser.add_argument('--mask', help='Get Used IPs to use as static according a network mask')

    args = parser.parse_args()

    if args.ssid and args.password and args.mode:
        setup_rm(args.ssid, args.password, int(args.mode))
        devices = broadlink.discover(timeout=5)
        if not devices:
            input("WAIT!!! PRESS ENTER JUST WHEN YOUR COMPUTER CONNECTS TO YOUR HOME NETWORK AGAIN...")
        discover_devices()
    elif args.get:
        discover_devices()
    elif args.mask:
        get_used_ips(args.mask)
    else:
        print("PLEASE USE THE FLAG --get TO GET RM MINI ALREADY CONFIGURED")


if __name__ == '__main__':
    main()
