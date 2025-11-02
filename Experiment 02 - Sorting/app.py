class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    
    def __lt__(self, other):
        return self.marks < other.marks
    
    def __repr__(self):
        return f"{self.name} | Roll: {self.roll_no} | Marks: {self.marks}"


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name, roll_no, marks):
        self.students.append(Student(name, roll_no, marks))

    # ---------------- QUICK SORT ----------------
    def quick_sort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
            self.quick_sort(arr, low, pi - 1)
            self.quick_sort(arr, pi + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j].marks <= pivot.marks:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    # ---------------- MERGE SORT ----------------
    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            self.merge_sort(left)
            self.merge_sort(right)

            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i].marks <= right[j].marks:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

    def sort_students(self, algorithm="quick"):
        data = self.students.copy()
        if algorithm == "quick":
            self.quick_sort(data, 0, len(data) - 1)
        else:
            self.merge_sort(data)
        return data

    def display(self, list_data):
        print("\n--- Student Records ---")
        for s in list_data:
            print(s)


# ---------------- APPLICATION ----------------
def run_app():
    system = StudentManagementSystem()
    
    print("\n📘 Student Management & Sorting System")
    while True:
        print("\nMenu :")
        print("1. Add Student")
        print("2. View Students")
        print("3. Sort by Marks (Quick Sort)")
        print("4. Sort by Marks (Merge Sort)")
        print("5. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            name = input("\nEnter Name: ")
            roll = input("Enter Roll No: ")
            marks = int(input("Enter Marks: "))
            system.add_student(name, roll, marks)
            print("✅ Student Added!")

        elif choice == "2":
            if not system.students:
                print("No records found.")
            else:
                system.display(system.students)

        elif choice == "3":
            sorted_list = system.sort_students("quick")
            print("\nSorted using Quick Sort")
            system.display(sorted_list)

        elif choice == "4":
            sorted_list = system.sort_students("merge")
            print("\nSorted using Merge Sort")
            system.display(sorted_list)

        elif choice == "5":
            print("Exiting... Bye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    run_app()
