from appliances.kitchen import Dishwasher
from appliances.laundry import Dryer
from appliances.laundry import Washer
from appliances.kitchen.utility import Refrigerator
from appliances.kitchen import CoffeeMaker
from appliances.kitchen import CanOpener

whirlpool_dishwasher = Dishwasher(color="black")
whirlpool_dishwasher.wash_dishes()

samsung_washer = Washer("red")
samsung_dryer = Dryer("red", "gas")

lg_fridge = Refrigerator("stainless")
lg_fridge.make_ice()

mr_coffee = CoffeeMaker("white")
mr_coffee.make_coffee()

kitchen_aid = CanOpener("black")
kitchen_aid.open_can()
