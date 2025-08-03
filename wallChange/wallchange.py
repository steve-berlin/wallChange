from time import sleep
import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

# Access environment variables
USER = os.getenv("USER")

# Use absolute path, expanding ~
script_path = os.path.expanduser(f"/home/{USER}/wallChange/wallchange.sh")

wallnum = 0
while True:
    minute = 60
    sleep(5 * 60)
    wallnum += 1
    if wallnum > 11:
        wallnum = 1
    # Prefer running with bash; don't pass the "~"
    subprocess.run(["bash", script_path, str(wallnum)])
