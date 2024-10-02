# Md Mushfiqur Rahman
# mmrahman@umc.edu

from Bike import Bike

###############################################
# Instantiating a new bike object named "gt"
###############################################
gt = Bike(number_of_gears = 15, number_of_wheels = 4, brake_type = "hand brake")
input("Hit [Enter] to print the bike object")
print(gt) # prints the bike object
print("")

# Setting the current gear to 10
input("Hit [Enter] to see the new number of gear")
gt.set_current_gear(10)
gt.get_current_gear()
print("")
print("")

# increase the gear
input("Hit [Enter] to check the current gear and then increase")
gt.get_current_gear()
gt.increase_gear()
gt.get_current_gear()
print("")
print("")
# increasing the gear to the maximum gear and try to bypass it
input("Hit [Enter] to increase the gear to the maximum number of gears (15)")
print("The current gear is 11. So, using 'increase gear' method 4 times to reach maximum gear of 15")
gt.increase_gear()
gt.increase_gear()
gt.increase_gear()
gt.increase_gear()
gt.get_current_gear()
print("")
input("To see what happens when we try to increase the gear when the current gear has reached 15. Hit [Enter]...")
gt.increase_gear()
print("")
print("")

# Decreasing the gear to the minimum gear and try to bypass it.
print("To decrease the current gear to the minimum gear 1 and then try to bypass it. We first reset the gear to 1")
gt.reset_gear()
gt.get_current_gear()
print("")
input("To see what happens when we try to decrease the gear when the current gear has reached 1. Hit [Enter]...")
gt.decrease_gear()
print("")
print("")

# Check electric brake type
input("Hit [Enter] to check whether 'electric' brake works or not")
gt.set_brake_type("electric")
print("")
print("")
# Have a final look at the bike object
input("Hit [Enter] to have a final look at the bike object")
print(gt)

