import os
import requests
import threading
from queue import Queue
from colorama import init, Fore, Style

# Initialize colorama
init()

# Set up authentication
headers = {
    'Client-ID': '[YOUR_CLIENT_ID]',
    'Authorization': 'Bearer [YOUR_ACCESS_TOKEN]'
}

# Set up file paths
dirname = os.path.dirname(__file__)
usernames_file = os.path.join(dirname, "usernames.txt")
live_file = os.path.join(dirname, "live.txt")
offline_file = os.path.join(dirname, "offline.txt")

# Read list of usernames from file
with open(usernames_file, "r") as f:
    channels = f.read().splitlines()

# Create a queue to hold the usernames
queue = Queue()

# Add the usernames to the queue
for channel in channels:
    queue.put(channel)

# Function to check the stream status of a channel
def check_status(channel):
    # Send a request to the Twitch API to get the stream status of the channel
    url = "https://api.twitch.tv/helix/streams"
    params = {"user_login": channel}
    response = requests.get(url, headers=headers, params=params).json()

    # Check if the channel is live
    if response.get("data"):
        # Channel is live, add to LIVE.txt file
        with print_lock:
            print(Fore.GREEN + f"{channel} is live." + Style.RESET_ALL)
        return (channel, "live")
    else:
        # Channel is offline, add to offline.txt file
        with print_lock:
            print(Fore.RED + f"{channel} is offline." + Style.RESET_ALL)
        return (channel, "offline")

# Function to write the channel to the appropriate file
def write_to_file(channel, status):
    if status == "live":
        # Check if channel is already in the live.txt file
        with open(live_file, "r") as f:
            if channel in f.read():
                return
        # Channel is not in the file, add it
        with open(live_file, "a") as live_file_obj:
            live_file_obj.write(channel + "\n")
    else:
        # Check if channel is already in the offline.txt file
        with open(offline_file, "r") as f:
            if channel in f.read():
                return
        # Channel is not in the file, add it
        with open(offline_file, "a") as offline_file_obj:
            offline_file_obj.write(channel + "\n")

# Function for the worker thread
def worker():
    while True:
        # Get a username from the queue
        channel = queue.get()

        # Check the stream status of the channel
        result = check_status(channel)

        # Write the channel to the appropriate file
        write_to_file(result[0], result[1])

        # Mark the task as done
        queue.task_done()

# Create the worker threads
num_threads = 10
print_lock = threading.Lock()  # Create a lock for print statements
for i in range(num_threads):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()

# Wait for all tasks to be completed
queue.join()

# Print a message indicating the process is complete
print("Done checking.")
