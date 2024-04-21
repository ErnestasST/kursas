from transport.auto import Auto
from math import ceil

class Truck(Auto):
    def __init__(self, predicted_km_per_year, number, fuel_type, fixed_cost, technical_date, driver_category,
                 fuel_consumption_per_100km, insurance_date, transported_weight, is_it_cable_drag_trailer,
                 trailer_weight):
        super().__init__(predicted_km_per_year, number, fuel_type, fixed_cost, technical_date, driver_category,
                         fuel_consumption_per_100km, insurance_date)

        self.transported_weight = transported_weight
        self.is_it_cable_drag_trailer = is_it_cable_drag_trailer
        self.trailer_weight = trailer_weight

    def raises_need(self, total_weight):
        trucks_need = ceil(total_weight / (self.transported_weight + self.trailer_weight))
        trailers_need = ceil((total_weight - trucks_need * self.transported_weight) / self.trailer_weight)
        if trailers_need <= 0:
            return trucks_need, 0
        return trucks_need, trailers_need

