from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

coffee_machine_on = True

while coffee_machine_on:
    choice_str = input(f"What would you like? ({menu.get_items()}): ")
    if choice_str == 'off':
        coffee_machine_on = False
    elif choice_str == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        menu_choice = menu.find_drink(choice_str)
        if menu_choice is not None:
            if coffee_maker.is_resource_sufficient(menu_choice) and money_machine.make_payment(menu_choice.cost):
                coffee_maker.make_coffee(menu_choice)
