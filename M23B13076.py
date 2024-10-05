class StudentData:
    def __init__(self, registration_number, student_name, year):
        self.registration_number = registration_number
        self.student_name = student_name
        self.year = year
        
    def __str__(self) -> str:
        return (f"registration number: {self.registration_number},"
                f"student name:{self.student_name},"
                f"year:{self.year}")
M23B13_001 = StudentData("M23B13/001","gian","2")   
M23B13_002 = StudentData("M23B13/002","messi","2")
M23B13_003 = StudentData("M23B13/003","onana","2")

print(M23B13_001)
print(M23B13_002)
print(M23B13_003)