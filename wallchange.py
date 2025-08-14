import time  # import sleep
import subprocess
import os
import wallrc

# Access environment variables
USER = os.getenv("USER")

# Use absolute path, expanding ~
script_path = os.path.expanduser(f"/home/{USER}/wallChange/wallchange.sh")
print(wallrc.minutes)
wallnum = 0
while True:
    secs = 60
    mins = wallrc.minutes
    time.sleep(mins * secs)
    wallnum += 1
    if wallnum > 11:
        wallnum = 1
    # Prefer running with bash; don't pass the "~"
    subprocess.run(["bash", script_path, str(wallnum)])
