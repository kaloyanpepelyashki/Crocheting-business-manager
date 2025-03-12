import math
import json
from dataclasses import dataclass
from dataclasses import field
from typing import List

with open("pricingModel.json", "r") as file:
    data = json.load(file)
    parsed_data = json.loads(json.dumps(data))

# #The hourly pay rate
HOURLY_PAY_RATE: int = parsed_data["hourly_pay_rate"] #in dkk
# #The price for a gram of yarn
YARN_PRICE_PER_GRAM: int = parsed_data["yarn_price_per_gram"] #in grams
# #The price for the whole eyes pack
EYES_PACK_PRICE: int = parsed_data["eyes_pack_price"] #in dkk
# #The price for a pack of stuffing
STUFFING_PACK_PRICE: int = parsed_data["stuffing_pack_price"] #in dkk

@dataclass
class Product:
    needed_yarn_grams: int
    needed_time_minutes: int
    needed_eyes: int
    difficulty_rate_percent: float
    product_name: str


    def calculate_price(self, amount):
        difficulty_percent_multiplier = 1 + (self.difficulty_rate_percent/100)
        #The price for time taken
        time_price = (self.needed_time_minutes / 60) * HOURLY_PAY_RATE #in dkk
        price_of_eyes = (12/EYES_PACK_PRICE) * self.needed_eyes

        #The price for materials 
        base_price = (self.needed_yarn_grams * YARN_PRICE_PER_GRAM)  + price_of_eyes #in dkk
        price = math.ceil(((base_price + time_price) * difficulty_percent_multiplier))


        return  { "total_price": price * amount, "base_price": base_price * amount}
