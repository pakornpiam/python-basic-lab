#oopbasic.py
class Student:

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def study(self):
        print(' studying.....')

class Teacher:

    def __init__(self,name,age,subject):
        self.name = name
        self.age= age
        self.subject = subject
    def teach(self):
        print('teacher{} teaching{}'.format(self.name,self.subject))


if __name__ == '__main__':

    student1 = Student('somchai','14','male')
    student2 = Student('somsri','14','female')

    teacher1 =Teacher('John','54','English')

    print(teacher1.name)
    print(teacher1.subject)
    print('................')
    teacher1.teach()
        

       