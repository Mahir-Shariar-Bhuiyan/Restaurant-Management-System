from Menu import Menu

class Restaurant:
    def __init__(self,name):
        self.name=name
        self.employees=[]
        self.menu=Menu()
    def add_employee(self,employee):
        self.employees.append(employee)
    def view_employees(self):
        print('Employee List!!')
        for em in self.employees:
            print(f'Name : {em.name}   Phone : {em.phone}   Email : {em.email}   Address : {em.address}')
