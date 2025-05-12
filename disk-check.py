# This script can be use to check the available disk for your system

import shutil

total,used,free = shutil.disk_usage("/")
threshold = 80

used_percent = (used /total) * 100
if used_percent > threshold :
    print(f"Disk usgae is critical:{used_percent:.2f}% used!")
else:
    print(f"Disk usage is ok: {used_percent:.2f}% used!")