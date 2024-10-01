# Md Mushfiqur Rahman
# Email: mmrahman@umc.edu


# Creating a bike class
class Bike:
# Properties
# Number of gears (1-15) : set_number_of_gears(), get_number_of_gears()
# Current gear (default value: 1): set_current_gear(), get_current_gear()
# Number of wheels (1-4): set_number_of_wheels(), get_number_of_wheels()


    def __init__(self, number_of_gears=4):
    # validate number of gears
        try:
            if isinstance(number_of_gears, int) and 1 <= number_of_gears <= 15: # Ensures the value is an integer and value between 1 to 15
                self._number_of_gears = number_of_gears
            else:
                print("The number of gears should be an integer and between 1 to 15") # Print the error message
                self._number_of_gears = 10 # setting default value of the number of gears to 10
        except ValueError:
            print("The number of gears should be an integer and between 1 to 15")  # Print the error message

# String representation of the Bike object
    def __str__(self):
        return (f"Bike with {self._number_of_gears} number of gears")

honda = Bike(number_of_gears = 5)

