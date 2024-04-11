from appliances.appliance import Appliance

class AirConditioner(Appliance):
  
  def __init__(self, color, heat_method="electric"):
        super().__init__(color, heat_method)
        
        def turn_on(self):
            print("The air conditioner is on")
