import threading
import time
import random


shared_data = []
data_lock = threading.Lock()

def add_data(thread_id, data):
    """Thread-safe function to add data to the shared dataset."""
    print(f"Thread {thread_id} attempting to acquire lock...")
    with data_lock:  # Acquire the lock
        print(f"Thread {thread_id} has acquired the lock.")
        shared_data.append(data)
        print(f"Thread {thread_id} added data: {data}")
        time.sleep(random.uniform(0.1, 0.5))  # Simulate processing time
    print(f"Thread {thread_id} released the lock.")

def thread_function(thread_id):
    """Function executed by each thread."""
    for i in range(3):
        data = f"Data-{thread_id}-{i}"
        add_data(thread_id, data)

threads = []
for i in range(5):  # Create 5 threads
    thread = threading.Thread(target=thread_function, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("\nFinal shared dataset:")
print(shared_data)