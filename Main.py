from Data_Class import dataEntry, dataset
from collections import defaultdict

import threading
import time

dataset = dataset()

data1 = [
    dataEntry(2022, "Data Structures", 96, "Oxford University"),
    dataEntry(2024, "Machine Learning", 72, "Cambridge University"),
    dataEntry(2023, "Machine Learning", 81, "Oxford University"),
    dataEntry(2022, "Artificial Intelligence", 91, "Stanford University"),
    dataEntry(2024, "Cyber Security", 84, "Stanford University")
]

data2 = [
    dataEntry(2024, "Software Engineering", 68, "UC Berkeley"),
    dataEntry(2023, "Software Engineering", 64, "Stanford University"),
    dataEntry(2023, "Artificial Intelligence", 97, "Cambridge University"),
    dataEntry(2022, "Computer Vision", 69, "UC Berkeley"),
    dataEntry(2022, "Machine Learning", 71, "Cambridge University")
]

data3 = [
    dataEntry(2023, "Software Engineering", 77, "UC Berkeley"),
    dataEntry(2022, "Machine Learning", 96, "Stanford University"),
    dataEntry(2024, "Machine Learning", 96, "Stanford University"),
    dataEntry(2024, "Machine Learning", 75, "Cambridge University"),
    dataEntry(2023, "Cyber Security", 67, "Oxford University")
]

data4 = [
    dataEntry(2023, "Computer Vision", 89, "MIT"),
    dataEntry(2022, "Computer Vision", 82, "Harvard University"),
    dataEntry(2023, "Cyber Security", 78, "Cambridge University"),
    dataEntry(2023, "Machine Learning", 75, "Stanford University"),
    dataEntry(2024, "Data Structures", 80, "Harvard University")
]

data5 = [
    dataEntry(2022, "Computer Vision", 76, "MIT"),
    dataEntry(2023, "Machine Learning", 66, "Harvard University"),
    dataEntry(2024, "Machine Learning", 66, "MIT"),
    dataEntry(2022, "Computer Vision", 95, "MIT"),
    dataEntry(2022, "Artificial Intelligence", 61, "Stanford University")
]

def thread_loop(entry_list, dataset_obj):
    for entry in entry_list:
        print(f"Thread {threading.current_thread().name} is processing entry: {entry.courseName}")
        dataset_obj.addEntry(entry)
        #time.sleep(0.5)

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


thread1 = threading.Thread(target=thread_loop, args=(data1, dataset), name="LoopThread(1)")
thread2 = threading.Thread(target=thread_loop, args=(data2, dataset), name="LoopThread(2)")
thread3 = threading.Thread(target=thread_loop, args=(data3, dataset), name="LoopThread(3)")
thread4 = threading.Thread(target=thread_loop, args=(data4, dataset), name="LoopThread(4)")
thread5 = threading.Thread(target=thread_loop, args=(data5, dataset), name="LoopThread(5)")

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()

verify_dataset("coursegrades.txt")