#oopbasic.py
class Student:

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

class Teacher:

    def __init__(self,name,age,subject):
        self.name = name
        self.age= age
        self.subject = subject


if __name__ == '__main__':

    student1 = Student('somchai','14','male')
    student2 = Student('somsri','14','female')

    teacher1 =Teacher('John','54','English')

    print(teacher1.name)
    print(teacher1.subject)
        

       