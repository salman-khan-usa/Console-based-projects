class student :
    def __init__(self,name,rollno,age,classs,grade):
        self.name = name
        self.rollno = rollno
        self.age = age
        self.classs = classs
        self.grade = grade

    def display_student(self):
        print(f'Name: {self.name},Rollno : {self.rollno},Age : {self.age},class : {self.classs},Grade : {self.grade}')


class Student_Management:
    def __init__(self):
        self.students = {}

    def add_student(self):
        name = input('Enter students name:').strip()
        try:
         rollno = int(input('Enter students rollno:'))
         if rollno in self.students:
             print("Roll no already exists,enter a valid rollno.")
             return
            
         age = int(input('Enter students age:'))
        
        except ValueError:
            print("❌ Error: Age must be a valid number!")

        grade = input('Enter Students grade(eg : A,B<F) :')    
        classs = int(input('Enter students class:'))

        new_student = student(name,rollno,age,classs,grade)
        self.students[rollno] = new_student
        print("Student added successfully!")

        with open('data.txt','a') as file:
            file.write(f'Name:{new_student.name}, Rollno:{new_student.rollno}, Age:{new_student.age}, class:{new_student.classs}, grade:{new_student.grade}\n' )

learners = Student_Management()
learners.add_student()
