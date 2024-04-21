from datetime import datetime

class Bus:
    def __init__(self, seats: int, kilos: int, number: str, caste: int, inspection_date: str, categories: str, gass_used: int, insurance_date: str):
        self.seats = seats
        self.kilos = kilos
        self.number = number
        self.caste = caste
        self.inspection_date = inspection_date
        self.categories = categories
        self.gass_used = gass_used
        self.insurance_date = insurance_date

    def check_inspection(self):
        today_date = datetime.now()
        bus_inspection_date = datetime.strptime(self.inspection_date, "%Y-%m-%d")

        if today_date >= bus_inspection_date:
            print("Need to inspection.")
        else:
            print("You still can drive.")

    def check_insurance(self):
        today_date = datetime.now()
        bus_insurance_date = datetime.strptime(self.insurance_date, "%Y-%m-%d")

        if today_date >= bus_insurance_date:
            print("Need to insurance your transport.")
        else:
            print("insurance will end in less then a month")

    def calculate_cost(self, distance):
        gas_price = 1.59
        gas_used = (self.gass_used / 100) * distance
        gas_cost = gas_price * gas_used
        result = gas_cost + self.caste

        return result

    def calculate_buses_needed(self, spots_needed: int):
        return spots_needed / self.seats

    def calculate_overall_price(self, spots_needed: int, distance):
        buses_needed = self.calculate_buses_needed(spots_needed)
        overall_cost = self.calculate_cost(distance)

        return buses_needed * overall_cost


bus = Bus(
    seats=45,
    kilos=5000,
    number="HYA584",
    caste=1350,
    inspection_date="2024-04-30",
    categories="D",
    gass_used=25,
    insurance_date="2025-05-21",
)

bus.check_inspection()
bus.check_insurance()
print("Price for 100 km:", bus.calculate_cost(100))
print("How many buses needed:", bus.calculate_buses_needed(175))
print("Overall price:", bus.calculate_overall_price(175, 100))

