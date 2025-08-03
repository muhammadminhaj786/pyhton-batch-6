

#oop
#object oriented programming
# classes
# constructor init function
# attributes
#self => current refrence of object 
# method= > function belongs to object

# student = []

# print(student)

# std1 = {
#     'name': "minhaj",
#     "rollNo": '123'
# }

# student.append(std1)

# print(student)

# std2 = {
#     "name": "ali",
#     "rollNo": "456"
# }

# student.append(std2)
# print(student)

# class => blue
# object => koi bhi chiz
# constructor => jab object create hoga contructor run hoga
# method =>function belongs to object

# book class title , author, pages
# account

class Student:
    def __init__(self,name,rollNo,marks):
        self.name = name
        self.rollNo =  rollNo
        self.marks = marks
        self.average = 0
    def show_info(self):
        print(f"hello {self.name} this is your roll no {self.rollNo}")

    def avg(self):
        total = 0
        for i in self.marks:
            total += i
        self.average = total / len(self.marks)
       
    def check_grade(self):
        if self.average > 80:
            print('A+')
        elif self.average > 70:
            print('A')
        else: 
            print('fail')


std1 = Student("minhaj","123", [56,78,88])
std1.avg()
std1.check_grade()
# std2 = Student("ali","456")
# std3 = Student("imran","886")
# print(std2.name)
# std2.show_info()
std2 = Student("ali","789b ", [53,23,78])
std2.show_info()
std2.avg()
std2.check_grade()