
class Student:

    passing_year=2024
    num_of_student=0
    
    def __init__(self,name,cgpa):
        self.name=name
        self.cgpa=cgpa
        Student.num_of_student+=1

    


student1=Student('tom',3.3)
student2=Student('Downy',3.2)

print(student1.name)
print(student1.cgpa)
print(student1.passing_year)
print(Student.num_of_student)
    