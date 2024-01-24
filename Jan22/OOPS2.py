class Employee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
    def getData(self):
        print("the Employee id is",self.id)
        print("the Employee name is",self.name)
        print("The Employee salary",self.salary)
        
i=int(input("enter the id"))
n=input("Enter the name")
s=int(input("Enter the salary"))
#rahul=Employee(101,"Jeeva",30000)
rahul=Employee(i,n,s)
rahul.getData()
        