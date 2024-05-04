
# Parameterized constructor
class Employee:
    def __init__(self,sal,ag):
        self.salary=sal
        self.age=ag
e1=Employee(22000,21)
e2=Employee(24000,22)
print(e1.__dict__)
print(e2.__dict__)
print("--Parameterized constructor")

# Non-parameterized constructor
class Emp2:
    def __init__(self):
        self.salary=20000
        self.age=22
e11=Emp2()
print(e11.__dict__)       
print("--Non-parameterized constructor")

# Default constructor
class Emp3:
    pass
e3=Emp3()
print(e3.__dict__)
print("--Default constructor")

# without constructor object cannot be created
