
from Bike import Bike

honda = Bike(number_of_gears=5, number_of_wheels=3, brake_type="hand brake")
honda.set_brake_type("foot brake")

honda.set_current_gear(3)
honda.decrease_gear()
honda.get_current_gear()
honda.decrease_gear()
honda.decrease_gear()
honda.set_number_of_gears(3)
honda.increase_gear()
honda.increase_gear()
honda.increase_gear()




