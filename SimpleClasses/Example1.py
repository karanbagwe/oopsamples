class Employee:
    def __init__(self,name,salary_pa,age,role,status,location):
        self.name=name
        self.salary_pa = salary_pa
        self.age = age
        self.role = role
        self.status = status
        self.location = location
## the get methods
    def get_name(self):
        return self.name
    def get_salary(self):
        salary_pm = (self.salary_pa*100000)/12
        self.salary_pm = str(salary_pm)
#        print("Monthly : " + str(salary_pm))
#        print("Annual: " + str(self.salary_pa))
        return self.salary_pm,self.salary_pa
    def get_age(self):
        return self.age
    def get_role(self):
        return self.role
    def get_status(self):
        return self.status
    def get_location(self):
        return self.location
## the set methods
    def set_name(self,name):
        self.name=name
    def set_age(self,age):
        self.age=age
    def set_salary(self,salary_pa):
        self.salary_pa = salary_pa
    def set_role(self,role):
        self.role = role
    def set_status(self,status):
        self.status = status
    def set_location(self,location):
        self.location = location

e1=Employee("Karan",5.9,27,"Developer","Single","Offshore")
print(e1.get_name())
e1.get_salary()
print(str(e1.salary_pa) + "<-- This is Annual")
print(str(e1.salary_pm) + "<-- This is Monthly")
