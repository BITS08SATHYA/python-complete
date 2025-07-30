class Student:
    "This is version 1.0"
    # Static variables
    college = 'NYU'
    # Constructor and instance variables
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
        print('In Constructor')

    def __str__(self):
        return 'This is Student Class'

    def display(self):
        print(self.name)
        print(self.age)
        print(self.marks)
        print(Student.college)



stu = Student('Sathya',10, 89)

print(stu.__init__)
print(stu.__str__())
print(stu.display())
