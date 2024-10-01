
from Bike import Bike

honda = Bike(number_of_gears=5, number_of_wheels=3, brake_type="hand brake")
honda.set_brake_type("foot brake")

honda.set_current_gear(3)
honda.get_current_gear()

honda.reset_gear()
honda.get_current_gear()
honda.increase_gear()
honda.increase_gear()
honda.get_number_of_gears()
honda.decrease_gear()
honda.decrease_gear()
honda.get_number_of_gears()




