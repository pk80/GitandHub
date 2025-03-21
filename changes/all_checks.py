#!/usr/bin/env python3

import os
import sys

def main():
    if check_reboot():
        print('Pending Reboot...')
        sys.exit(1)
    print('Everything OK!')
    sys.exit(0)


if __name__ == '__main__':
    main()
