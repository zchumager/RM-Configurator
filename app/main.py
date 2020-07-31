#!/usr/bin/python3

import broadlink
from errno import ENETUNREACH


def setup_rm():
    try:
        broadlink.setup('INFINITUM0201_2.4', 'FcoChiquete#10', 4)
    except IOError as e:
        if e.errno == ENETUNREACH:
            print("sending packages")


def get_rm_info(devices):
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


def main():
    setup_rm()
    devices = broadlink.discover(timeout=5)
    if not devices:
        input("Press Enter when your computer connects to your home network...")

    devices = broadlink.discover(timeout=5)
    if len(devices) > 0:
        rm_info = get_rm_info(devices)
        print(f"Device Information: {rm_info}")


if __name__ == '__main__':
    main()
