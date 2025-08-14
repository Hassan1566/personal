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

main()