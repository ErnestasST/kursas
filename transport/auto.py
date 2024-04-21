from datetime import datetime, timedelta
class Auto:
    def __init__(self, predicted_km_per_year, number, fuel_type, fixed_cost, technical_date, driver_category, fuel_consumption_per_100km, insurance_date,):
        self.insurance_date = insurance_date
        self.driver_category = driver_category
        self.technical_date = technical_date
        self.fixed_cost = fixed_cost
        self.fuel_type = fuel_type
        self.number = number
        self.predicted_km_per_year = predicted_km_per_year
        self.fuel_consumption_per_100km = fuel_consumption_per_100km

    def __check_next_month(self, date: datetime):
        today = datetime.today()
        next_month = today.replace(day=1) + timedelta(35)
        two_month_next = today.replace(day=1) + timedelta(65)

        if datetime(year=next_month.year, month=next_month.month, day=1) <= date < datetime(
                year=two_month_next.year, month=two_month_next.month, day=1):
            return True
        return False

    def check_if_next_month_needs_technical(self):
        if self.__check_next_month(self.technical_date):
            return True
        return False

    def check_if_next_month_needs_insurance(self):
        if self.__check_next_month(self.insurance_date):
            return True
        return False

    def calculate_costs(self, distance):
        fuel_consumed = (distance/100) * self.fuel_consumption_per_100km
        fuel_price_per_liter = self.fuel_pricing()
        total_cost_per_liter = fuel_consumed * fuel_price_per_liter
        total_cost_per_year = self.fixed_cost / 365 * (distance / self.predicted_km_per_year * 365)
        total_cost = total_cost_per_liter + total_cost_per_year
        return total_cost

    def fuel_pricing(self):
        return 1.59

