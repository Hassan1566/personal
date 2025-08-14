#!/usr/bin/env python3
import os
import sys

def check_reboot():
    """Check if a reboot is required."""    
    return os.path.exists('/run/reboot-required') or os.path.exists('/var/run/reboot-required')


def main():
    if check_reboot():
        print("pending reboot")
        sys.exit(1)
    if disk_full():
        print("disk full")
        sys.exit(1)
    print("no pending reboot")
    sys.exit(0)

main()