from transport.auto import Auto

class Car(Auto):
    def __init__(self, predicted_km_per_year, number, fuel_type, fixed_cost, technical_date, driver_category,
                 fuel_consumption_per_100km, insurance_date):
        super().__init__(predicted_km_per_year, number, fuel_type, fixed_cost, technical_date, driver_category,
                         fuel_consumption_per_100km, insurance_date)

    def run(self):
        print("run")