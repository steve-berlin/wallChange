import time  # import sleep
import subprocess
import os

# Access environment variables
USER = os.getenv("USER")

# Use absolute path, expanding ~
script_path = os.path.expanduser(f"/home/{USER}/wallChange/wallchange.sh")

wallnum = 0
while True:
    minute_in_secs = 60
    minutes = 0.25
    time.sleep(minutes * minute_in_secs)
    wallnum += 1
    if wallnum > 11:
        wallnum = 1
    # Prefer running with bash; don't pass the "~"
    subprocess.run(["bash", script_path, str(wallnum)])
