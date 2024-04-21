from datetime import datetime

class Car:
    def __init__(self, kilos: int, number: str, caste: int, inspection_date: str, categories: str, gass_used: int, insurance_date: str, gass_type: str):
        self.kilos = kilos
        self.number = number
        self.gass_type = gass_type
        self.caste = caste
        self.inspection_date = inspection_date
        self.categories = categories
        self.gass_used = gass_used
        self.insurance_date = insurance_date

    def cheking_inspection_insurance(self):
        today_date = datetime.now()
        inspection_c = False
        insurance_c = False
        if self.inspection_date is not None:
            need_inspection = self.inspection_date.replace(self.inspection_date.year + 1)
            if need_inspection <= today_date:
                inspection_c = True
        else:







car = Car(
    seats=45,
    kilos=5000,
    number="HYA584",
    caste=1350,
    inspection_date="2025-6-31",
    categories="D",
    gass_used=25,
    insurance_date="2024-4-30",
)

registration = datetime(2021, 8, 21)
insurance_registration = datetime(2022, 4, 30)
inspection_registration = datetime(2023, 6, 31)