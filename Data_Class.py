import threading, time

lock_check = input("Do you want to use threading lock? Y/n")

class dataEntry:
    def __init__(self, year, courseName, grade, university):
        self.year = year
        self.courseName = courseName
        self.grade = grade
        self.university = university

    def __str__(self): #entry printing
        return f"{self.year} {self.courseName} {self.grade} {self.university}"

class dataset:
    def __init__(self, filename="entries.txt"):
        self.filename = filename
        self.lock = threading.Lock()

    def _parse_line_to_data_entry(self, line_str):
        parts = line_str.strip().split(maxsplit=3)
        year = int(parts[0])
        course_name = parts[1]
                
        grade_str = parts[2]   
        grade = grade_str
        
        university = parts[3]
        return dataEntry(year, course_name, grade, university)
 
    def addEntry(self, entry): #Add new entry
        if lock_check == "y" or lock_check == "Y":
            with self.lock:
                time.sleep(0.1)
                print(f"Thread {threading.current_thread().name} Acquired a lock")
                with open(self.filename, 'a') as f:
                    f.write(str(entry) + '\n')
                print(f"Thread {threading.current_thread().name} added entry to file: {str(entry)}")
        else:
            print(f"Thread {threading.current_thread().name} is operating WITHOUT a lock")
            time.sleep(0.1)
            with open(self.filename, 'a') as f:
                f.write(str(entry) + '\n')
            print(f"Thread {threading.current_thread().name} added entry to file: {str(entry)}")