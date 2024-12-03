class person(object):
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber 
    def display(self):
        print(self.name)
        print(self.idnumber)

class employee(person):
    def __init__(self,name,idnumber,salary,post):
        self.salary=salary
        self.post=post
        person.__init__(self,name,idnumber)
    def display2(self):
        print(self.salary)
        print(self.post)
        

ob1=employee("Maham",1718,1000000,"janitor")
ob1.display()
ob1.display2()