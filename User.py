from abc import ABC
from Order import Order
class User(ABC):
    def __init__(self,name,email,phone,address):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address


class Employee(User):
    def __init__(self, name, email, phone, address,age,designation,salary):
        super().__init__(name, email, phone, address)
        self.age=age
        self.designation=designation
        self.salary=salary


class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.employees=[]
    def add_employee(self,restaurant,employee):
        restaurant.add_employee(employee)
    def view_emplpoyees(self,restaurant):
        restaurant.view_employees()
    def add_item(self,restaurant,item):
        restaurant.menu.add_menu_item(item)
    def delete_item(self,restaurant,item):
        restaurant.menu.remove_item(item)
    def view_menu(self,restaurant):
        restaurant.menu.show_menu()



class Customer(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.cart=Order()
    def view_menu(self,restaurant):
        restaurant.menu.show_menu()
    def add_to_cart(self,restaurant,item_name,quantity):
        item=restaurant.menu.find_item(item_name)
        if item:
            if quantity > int(item.quantity):
                print('Item quantity exceeded!!')
            else:
                item.quantity-=quantity
                self.cart.add_items(item)
                print('Item added')
        else:
            print('Item not found')
    def view_cart(self):
        print('====Cart====')
        print('Name\tPrice\tQuantity')
        for item,quantity in self.cart.items.items():
            print(f'{item.name}\t{item.price}\t{quantity}')
            print(f'Total Price = {self.cart.total_price}')
    def pay_bill(self):
        print('Paid Successfully')
        self.cart.clear()





