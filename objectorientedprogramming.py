class student:
    grade = 9
    name="codingal"
    def introduction(self):
        print("Hello i am student")
    def print_grade(self):
        print("my grade is",self.grade)
    def print_name(self):
        print("my name is",self.name)

object_student=student()
object_student.introduction()
object_student.print_grade()
object_student.print_name()

class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sing(self,song):
        return "{} sings{}".format(self.name,song)
    def dance(self):
        return "{} is now dancing".format(self.name)
    
blue=parrot("blu",10)
woo=parrot("woo",15)
print("Blu is a {}"+blue.name +"of age"+ str(blue.age))
print("Woo is a {}"+ woo.name + "of age"+ str(woo.age))
print(blue.sing("happy"))
print(woo.sing("happy"))
print(blue.dance())
print(woo.dance())
