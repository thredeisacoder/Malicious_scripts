import os

# Path
log_dir = "D:\\"
log_file = os.path.join(log_dir, "logs.txt")
processed_log_file = os.path.join(log_dir, "translogs.txt")

def process_logs():
    print("Starting to process logs...")

    if not os.path.exists(log_file):
        print(f"The log file {log_file} does not exist.")
        return
    
    try:
        with open(log_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except UnicodeDecodeError:
        print("Failed to read the log file with UTF-8 encoding. Trying with latin-1 encoding.")
        with open(log_file, 'r', encoding='latin-1') as f:
            lines = f.readlines()
    
    print(f"Read {len(lines)} lines from log file.")

    with open(processed_log_file, 'w', encoding='utf-8') as f:
        for line in lines:
            # Remove the timestamp and only keep the key data
            key_data = line.split(': ', 1)[-1].strip()
            # Handle special keys
            if key_data.startswith("'") and key_data.endswith("'"):
                key_data = key_data[1:-1]
            elif key_data.startswith("Key."):
                key_data = f"[{key_data.split('.')[1]}]"
            
            f.write(key_data + '\n')

    print("Finished processing logs. Processed data written to translogs.txt.")

if __name__ == "__main__":
    print("Starting the log processing script.")
    process_logs()
