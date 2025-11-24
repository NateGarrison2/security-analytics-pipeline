import subprocess
import sys
import os
import time

# Change working directory to the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# List of scripts to run in order
scripts = [
    'data_generation_script.py',
    'etl_pipeline.py',
    'db_loader.py'
]

# Run each script sequentially
for script in scripts:
    print(f"Running {script}...")
    result = subprocess.run([sys.executable, script], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running {script}:\n{result.stderr}")
        break
    else:
        print(f"Output from {script}:\n{result.stdout}")
    time.sleep(5) # Brief pause between scripts