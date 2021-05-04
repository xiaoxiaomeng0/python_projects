from menu import menu, resources


class CoffeeMachine:
    def __init__(self, class_menu, class_resources):
        self.menu = class_menu
        self.resources = class_resources
        self.is_on = True
        self.money = 0
        self.user_choice = None

    # TODO asking user "What would you like? (expresso/latte/cappuccino): "

    def machine_on(self):
        """
        :return: str
        """
        while self.is_on:
            self.user_choice = input("What would you like? (espresso/latte/cappuccino): ")
            if self.user_choice == "off":
                self.turn_off()
                print("Machine is off")
                return
            self.check_resource()

    # TODO Turn off the coffee machine by entering "off" to the prompt
    def turn_off(self):
        self.is_on = False

    # TODO Print report
    def report(self):
        water = self.resources["water"]
        milk = self.resources["milk"]
        coffee = self.resources["coffee"]
        print(f"Water: {water}ml \n"
              f"Milk: {milk}ml \n"
              f"Coffee: {coffee}ml \n"
              f"Money: ${self.money}")

# TODO Check resource sufficient?
    def check_resource(self):
        for key in self.menu:
            if self.user_choice == key:
                choice = self.menu[key]
                for ingredient in choice["ingredients"]:
                    if choice["ingredients"][ingredient] > self.resources[ingredient]:
                        print(f"Sorry there is not enough {ingredient}.")
                        return
                self.process_coin()

    def get_ingredients(self, choice):
        return choice["ingredients"]

# TODO process coins
    def process_coin(self):
        quarters = int(input("Insert your quarters: "))
        dimes = int(input("Insert your dimes: "))
        nickles = int(input("Insert your nickles: "))
        pennies = int(input("Insert your pennies: "))
        insert_value = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
        if self.menu[self.user_choice]["cost"] > insert_value:
            print("Sorry that's not enough money. Money refunded.")
            refund = insert_value
        else:
            self.money = self.menu[self.user_choice]["cost"]
            refund = round(insert_value - self.menu[self.user_choice]["cost"], 2)
            print(f"Here is your {self.user_choice}")
            for key in self.menu[self.user_choice]["ingredients"]:
                self.resources[key] -= self.menu[self.user_choice]["ingredients"][key]
        print(f"Here is ${refund} dollars in change.")

# TODO Check tranction successful?

# TODO make coffee


my_coffee_maker = CoffeeMachine(menu, resources)
my_coffee_maker.report()
my_coffee_maker.machine_on()



