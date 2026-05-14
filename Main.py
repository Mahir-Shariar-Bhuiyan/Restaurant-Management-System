from Food_Item import Fooditem
from Order import Order
from Restaurant import Restaurant
from Menu import Menu
from User import Customer,Admin,Employee

Bhuiyan_Food_Zone=Restaurant('Bhuiyan Food Zone')

def customer_menu():
    name=input('Enter Your Name : ')
    phone =input('Enter Your Phone Number : ')
    email=input('Enter Your Email : ')
    address=input('Enter Your Address : ')
    customer=Customer(name=name,phone=phone,email=email,address=address)

    while True:
        print(f'Welcome {customer.name}')
        print('1. View Menu')
        print('2. Add to cart')
        print('3. View Cart')
        print('4. Pay Bill')
        print('5. Exit')

        choice=int(input('Enter Your Choice : '))
        if choice==1:
            customer.view_menu(Bhuiyan_Food_Zone)
        elif choice==2:
            item_name=input('Enter the item name : ')
            quantity=int(input('Enter Quantity : '))
            customer.add_to_cart(Bhuiyan_Food_Zone,item_name,quantity)
        elif choice==3:
           customer.view_cart()
        elif choice==4:
            customer.pay_bill()
        elif choice==5:
            break
        else:
            print('Invalid Input')


def admin_menu():
    name=input('Enter Your Name : ')
    phone =input('Enter Your Phone Number : ')
    email=input('Enter Your Email : ')
    address=input('Enter Your Address : ')
    admin=Admin(name,phone,email,address)

    while True:
        print(f'Welcome {admin.name}')
        print('1. Add New Item')
        print('2. Add New Employee')
        print('3. View Empolyee')
        print('4. View Items')
        print('5. Delete Item')
        print('6. Exit')

        choice=int(input('Enter Your Choice : '))
        if choice==1:
            item_name=input('Enter Item Name : ')
            item_price=input('Enter Price : ')
            item_quantity=input('Enter Quantity : ')
            item=Fooditem(item_name,item_price,item_quantity)
            admin.add_item(Bhuiyan_Food_Zone,item)
        elif choice==2:
            em_name=input('Enter Employee Name : ')
            em_phone=input('Enter Employee Phone : ')
            em_email=input('Enter Employee Email : ')
            em_age=input('Enter Employee Age : ')
            em_designation=input('Enter Designation : ')
            em_salary=input('Enter Salary : ')
            em_address=input('Enter Employee Address : ')
            em=Employee(em_name,em_email,
                        em_phone,em_address,em_age,em_designation,em_salary)
            admin.add_employee(Bhuiyan_Food_Zone,em)

        elif choice==3:
           admin.view_emplpoyees(Bhuiyan_Food_Zone)
        elif choice==4:
            admin.view_menu(Bhuiyan_Food_Zone)
        elif choice==5:
            it_name=input('Enter Item Name : ')
            admin.delete_item(Bhuiyan_Food_Zone,it_name)
        elif choice==6:
            break
        else:
            print('Invalid Input!!')


while True:
    print('=====Welcome=====')
    print('1. Customer')
    print('2. Admin')
    print('3. Exit')
    choice=int(input('Enter Your Choice : '))
    if choice==1:
        customer_menu()
    elif choice==2:
        admin_menu()
    elif choice==3:
        break
    else:
        print('Invalid Input!!')
