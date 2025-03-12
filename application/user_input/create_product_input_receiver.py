from infrastructure.cli import *


def get_product_name() :
    while True :
        product_name: str = input_validator("Name the product > ")
        if len(product_name) < 3 :
            print("❌ Choose longer name")
        else :
            return product_name

def get_needed_yarn() :
     while True :
        yarn_grams: int = int(input_validator("How much yarn will you use (grams) > "))
        if yarn_grams < 5 :
            print("❌ That's too little, chose a higher number")
        else :
            return yarn_grams

def get_needed_eyes() :
    while True :
        needed_eyes: int = int(input_validator("How many eyes would you need > "))
        if needed_eyes > 10 :
            print("❌ Isn't that too many? Choose a smaller number")
        else :
            return needed_eyes

def get_time_needed() :
    while True :
        time_in_minutes: int = int(input_validator("How much time will that take (minutes) > "))
        if time_in_minutes < 15 :
            print("❌ That's too little time, chose a higher number")
        else : 
            return time_in_minutes

def get_difficulty_level() :
    while True :
        difficulty_percent: int = int(input_validator("How difficult do you think that is (percent - 1 - 100) > "))
        if difficulty_percent < 1 or difficulty_percent > 100:
            print("❌ Difficulty percentage must be between 1 and 100. Choose again")
        else :
            return difficulty_percent