import threading

class dataEntry:
    def __init__(self, year, courseName, grade, university):
        self.year = year
        self.courseName = courseName
        self.grade = grade
        self.university = university

    def __str__(self): #entry printing
        return f"{self.year} {self.courseName} {self.grade} {self.university}"

class dataset:
    def __init__(self):
        self.data_stack = []
        self.lock = threading.Lock()

    def addEntry(self, entry): #Add new entry
        with self.lock:
            print(f"Thread {threading.current_thread().name} Acquired a lock")
            self.data_stack.append(entry)
            print(f"Thread {threading.current_thread().name} added entry: {str(entry)}")

    def popEntry(self): #Get latest entry
        with self.lock:
            return self.data_stack.pop()

    def printStack(self): #Use to print all stack
        with self.lock:
            for entry in self.data_stack:
                print(f"Year: {entry.year}, Course Name: {entry.courseName}, Grade: {entry.grade}, University: {entry.university}")
