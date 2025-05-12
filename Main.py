from Data_Class import dataEntry, dataset
from collections import defaultdict

import threading
import time

dataset = dataset()

def read_entries_from_file(filename):
    entries = []
    with open(filename, 'r') as file:
        for line in file:
            if line.strip():  # Skip empty lines
                parts = line.strip().split(', ')
                if len(parts) == 4:  # Ensure we have all four fields
                    year, course, grade, university = parts
                    entries.append(dataEntry(int(year), course, int(grade), university))
    return entries

all_entries = read_entries_from_file("coursegrades.txt")

# Split entries into two parts for threading demonstration
data = all_entries[:len(all_entries)//2]
data2 = all_entries[len(all_entries)//2:]

def thread_loop():
    for entry in data:
        print(f"Thread {threading.current_thread().name} is processing entry: {entry.courseName}")
        dataset.addEntry(entry)
        time.sleep(1)
    dataset.printStack()

def thread_loop2():
    for entry in data2:
        print(f"Thread {threading.current_thread().name} is processing entry: {entry.courseName}")
        dataset.addEntry(entry)
        time.sleep(1)
    dataset.printStack()

def verify_dataset(filename):
    total_entries = 0
    course_counts = defaultdict(int)

    with open(filename, 'r') as file:
        for line in file:
            if line.strip():  # Skips empty lines
                total_entries += 1
                _, course, _, _ = line.strip().split(', ')
                course_counts[course] += 1

    print("Dataset Verification")
    print(f"Total entries: {total_entries}")
    print("\nCourse distribution:")
    for course, count in sorted(course_counts.items()):
        print(f"{course}: {count}")


thread = threading.Thread(target=thread_loop, name="LoopThread")
thread2 = threading.Thread(target=thread_loop2, name="LoopThread2")
thread.start()
thread2.start()

thread.join()
thread2.join()

verify_dataset("coursegrades.txt")