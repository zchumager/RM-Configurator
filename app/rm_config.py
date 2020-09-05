#!/usr/bin/python3

import broadlink
import argparse
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


def main():
    parser = argparse.ArgumentParser(
        description='RM Mini Configurator Python CLI Tool'
    )

    parser.add_argument('-s', help="WiFi SSID")
    parser.add_argument('-p', help="WiFi Password")
    parser.add_argument('-m', help="WiFi Security Mode")

    args = parser.parse_args()

    if args.s and args.p and args.m:
        setup_rm(args.s, args.p, int(args.m))
        devices = broadlink.discover(timeout=5)
        if not devices:
            input("WAIT!!! PRESS ENTER JUST WHEN YOUR COMPUTER CONNECTS TO YOUR HOME NETWORK AGAIN...")

        discover_devices()


if __name__ == '__main__':
    main()
