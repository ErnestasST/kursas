from datetime import datetime

from transport.truck import Truck
from transport.car import Car
from transport.bus import Bus


car = Car(
    predicted_km_per_year=20000,
    number='ANB205',
    fuel_type='Petrol',
    fixed_cost=4000,
    technical_date=datetime(year=2024, month=5, day=15),
    driver_category='B',
    fuel_consumption_per_100km=8,
    insurance_date=datetime(year=2024, month=4, day=15),
)

bus = Bus(
    predicted_km_per_year=10000,
    number="GAS250",
    fuel_type="Petrol",
    fixed_cost=1000,
    technical_date=datetime(year=2024, month=6, day=21),
    driver_category="D",
    insurance_date=datetime(year=2024, month=4, day=28),
    fuel_consumption_per_100km=8,
    seat_amounts=50,
)

truck = Truck(
    predicted_km_per_year=5000,
    number="GAS250",
    fuel_type="Petrol",
    fixed_cost=2500,
    technical_date=datetime(year=2025, month=5, day=1),
    driver_category="CE",
    insurance_date=datetime(year=2024, month=5, day=1),
    fuel_consumption_per_100km=8,
    transported_weight=12,
    trailer_weight=3,
    is_it_cable_drag_trailer=True
)


# print(car.check_if_next_month_needs_insurance())
# print(car.check_if_next_month_needs_technical())
# print(car.calculate_costs(distance=250))
# print(bus.check_if_next_month_needs_insurance())
# print(bus.check_if_next_month_needs_technical())
# print(bus.count_how_many_buses_need(252))
# print(bus.counting_total_cost(175, 200))
# print(truck.check_if_next_month_needs_insurance())
# print(truck.check_if_next_month_needs_technical())
# print(truck.raises_need(21))


