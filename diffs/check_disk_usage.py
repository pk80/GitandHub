#!/usr/bin/env python3

import shutil
import sys


def check_disk_usage(disk, min_absolute, min_percent):
    """Returns True if there is enough free disk space, false otherwise."""
    disk_usage = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * disk_usage.free / disk_usage.total
    # Calculate how many free gigabytes
    gb_free = disk_usage.free / 2 ** 30

    if percent_free < min_percent or gb_free < min_absolute:
        return False
    return True

# Check for at least 2 GB and 10% free
if not check_disk_usage('/',2,10):
    print('ERROR: Not enough disk space')
    sys.exit(1)

print('Everything OK!')
sys.exit(0)
