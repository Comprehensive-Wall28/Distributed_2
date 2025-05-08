from Data_Class import dataEntry, dataset

import threading
import time

dataset = dataset()
entry = dataEntry(2022, "CS101", 95, "MIT")
entry2 = dataEntry(2023, "CS102", 90, "Harvard")
entry3 = dataEntry(2024, "CS103", 85, "Stanford")
entry4 = dataEntry(2025, "CS104", 80, "Yale")
entry5 = dataEntry(2026, "CS105", 75, "Princeton")
entry6 = dataEntry(2027, "CS106", 70, "Columbia")
entry7 = dataEntry(2028, "CS107", 65, "UCLA")
entry8 = dataEntry(2029, "CS108", 60, "Berkeley")
entry9 = dataEntry(2030, "CS109", 55, "Cornell")
entry10 = dataEntry(2031, "CS110", 50, "NYU")

# Make a for loop that brings the txt files entries into a variable
# So that it puts entries into the data variables below :)
# Moaz

data = [entry, entry2, entry3, entry4, entry5]
data2 = [entry6, entry7, entry8, entry9, entry10]

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

thread = threading.Thread(target=thread_loop, name="LoopThread")
thread2 = threading.Thread(target=thread_loop2, name="LoopThread2")
thread.start()
thread2.start()

thread.join()
thread2.join()