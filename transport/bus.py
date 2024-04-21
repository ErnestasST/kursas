from transport.auto import Auto
import math

class Bus(Auto):
    def __init__(self, predicted_km_per_year, number, fuel_type, fixed_cost, technical_date, driver_category,
                 insurance_date, seat_amounts, fuel_consumption_per_100km):
        super().__init__(predicted_km_per_year, number, fuel_type, fixed_cost, technical_date, driver_category,
                         fuel_consumption_per_100km, insurance_date)

        self.seat_amounts = seat_amounts
    def count_how_many_buses_need(self, passenger_spots):
        try:
            return math.ceil(passenger_spots / self.seat_amounts)
        except ZeroDivisionError as e:
            print("Can't divide by zero")

    def counting_total_cost(self, passengers, distance):
        try:
            buses_need = self.count_how_many_buses_need(passengers)
            total_cost = buses_need * distance * self.calculate_costs(100)
            return total_cost
        except ZeroDivisionError as e:
            print("Can't divide by zero")
