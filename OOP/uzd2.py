"""
Parašykite klasę CoffeeShop, kuri turi tris inicializuotos klasės kintamuosius:

name: str (iš esmės parduotuvės pavadinimas)

meniu : elementų sąrašas (list) (dict tipo), kuriame kiekvienas elementas turi elementą (elemento pavadinimą), tipą (ar tai maistas, ar gėrimas) ir kainą.

orders: tuščias list

ir septyni metodai:

add_order: į užsakymų sąrašo pabaigą įtraukia prekės pavadinimą, jei jis yra meniu, priešingu atveju grąžina "Šiuo metu šios prekės nėra!".

fulfill_order: jei užsakymų sąrašas nėra tuščias, grąžinama "{prekė} yra paruošta!". Jei užsakymų sąrašas tuščias, grąžinkite "Visi užsakymai įvykdyti!".

list_orders: grąžina priimtų užsakymų prekių pavadinimus, priešingu atveju - tuščią sąrašą.

due_amount: grąžina bendrą mokėtiną sumą už priimtus užsakymus.

cheapest_item: grąžina pigiausio meniu elemento pavadinimą.

drinks_only: grąžina tik meniu gėrimų tipo elementų pavadinimus.

food_only: grąžina tik meniu maisto tipo elementų pavadinimus.
"""


class CoffeeShop:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu
        self.orders = []

    def add_order(self, item):
        for menu_item in self.menu:
            if menu_item['item'] == item:
                self.orders.append(item)
                return f"{item} added to orders."
        return "This item is not currently available!"

    def fulfill_order(self):
        if self.orders:
            item = self.orders.pop(0)
            return f"{item} is ready!"
        else:
            return "All orders fulfilled!"

    def list_orders(self):
        return self.orders

    def due_amount(self):
        total_amount = 0
        for item in self.orders:
            for menu_item in self.menu:
                if menu_item['item'] == item:
                    total_amount += menu_item['price']
        return total_amount

    def cheapest_item(self):
        if not self.menu:
            return "Menu is empty."
        cheapest = min(self.menu, key=lambda x: x['price'])
        return cheapest['item']

    def drinks_only(self):
        return [item['item'] for item in self.menu if item['type'] == 'drink']

    def food_only(self):
        return [item['item'] for item in self.menu if item['type'] == 'food']


menu = [
    {'item': 'Latte', 'type': 'drink', 'price': 3.5},
    {'item': 'Croissant', 'type': 'food', 'price': 2.0},
    {'item': 'Espresso', 'type': 'drink', 'price': 2.5},
    {'item': 'Cake', 'type': 'food', 'price': 5.6}
]

my_coffee_shop = CoffeeShop("My Coffee Shop", menu)
print(my_coffee_shop.add_order("Latte"))
print(my_coffee_shop.add_order("Cake"))
print(my_coffee_shop.list_orders())
print(my_coffee_shop.due_amount())
print(my_coffee_shop.fulfill_order())
print(my_coffee_shop.fulfill_order())
print(my_coffee_shop.fulfill_order())
print(my_coffee_shop.fulfill_order())
print(my_coffee_shop.cheapest_item())
print(my_coffee_shop.drinks_only())
print(my_coffee_shop.food_only())






