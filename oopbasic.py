#oopbasic.py
class Student:

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def study(self):
        print(f'{self.name} studying.....')
    
    def sawadee(self):
        if sef.gender == 'male':
            tail = 'krab'
            callme = 'Pom'
        else :
            tail = 'ka'
            callme = 'Noo'
        
        print(f'sawadee{tail} {callme}ชื่อ{self.name}')

class Specialstudent(Student):
    def __init__(self, name, age, gender,parent):
        super().__init__(name, age, gender)
        self.parent = parent
    def hello(self, person = 'friend'):
        if person == 'friend':
            print ( 'Hey what up!!, Do you have chicken??')
        else:
            print('Bye Bye')
    def sawadee(self):
        print(f'wadee name{self.name}')
    def myfather (self):
        print('Do you konw who is my farther!!!')
        print(f'I am son of{self.parent}')
        

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
    special_student = Specialstudent('Joy',13,'male','son of God')
    teacher1 =Teacher('John','54','English')

    print(teacher1.name)
    print(teacher1.subject)
    print('......8.30am..........')
    teacher1.teach()
    student1.study()
    student2.study()
    print('..........8.45..........')
    special_student.sawadee()
    print('walk walk walk')
    special_student.hello()
    print (f'teacher{teacher1.name}')
    special_student.myfather()
        

       