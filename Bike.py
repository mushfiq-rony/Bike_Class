# Md Mushfiqur Rahman
# Email: mmrahman@umc.edu


# Creating a bike class
class Bike:
# Properties
# Number of gears (1-15)[Default value: 15] : set_number_of_gears(), get_number_of_gears()
# Current gear (default value: 1): set_current_gear(), get_current_gear()
# Number of wheels (1-4)[default value: 4): set_number_of_wheels(), get_number_of_wheels()
# brake type [default value: hand brake]: set_hand_brake(), get_hand_brake()

# Methods
# Set & Get Number of Gears.
# Set & Get Current Gear.
# Set & Get Number of Wheels.
# Set & Get Brake Type.
# Reset Gears: Set gear back to 1.
# Increase Gear: Increase Current Gear by 1, do not allow going over Number of Gears.
# Decrease Gear: Decrease Current Gear by 1, do not allow going under 1.
    _current_gear: int = 1

    def __init__(self, number_of_gears= 15, number_of_wheels =4, brake_type="hand brake", **temp):

    # validate number of gears
        if isinstance(number_of_gears, int) and 1 <= number_of_gears <= 15: # Ensures the value is an integer and value between 1 to 15
            self._number_of_gears = number_of_gears
        else:
            print("The number of gears should be an integer and between 1 to 15. Setting the default value of 15") # Print the error message
            self._number_of_gears = 15 # setting default value of the number of gears to 15

    # Current gear default to 1
        if 'current_gear' in temp  and not temp['current_gear']==1:
            print("'current_gear' is not an accepted keyword argument for Bike class."
                            "\nThe default value of current gear is set to 1")
            self.current_gear = 1
        elif 'current_gear' in temp and temp['current_gear'] == 1:
            print("'current_gear' is not an accepted keyword argument for bike class.\n"
                  "Since, you provided 'current_gear=1' it is same as the default value. So, it is set to 1")
            self.current_gear =1

    # Validate the number of wheels
        if isinstance(number_of_wheels, int) and 1 <= number_of_wheels <= 4:
            self._number_of_wheels = number_of_wheels
        else:
            print("Invalid Input: The number of values should be an integer and between 1 to 4. "
                  "\nNow setting the number of wheels to default value 4")
            self._number_of_wheels = 4 # Setting the default value to 4
    # Validating the brake type
        if brake_type not in ["hand brake", "foot brake"]:
            print('Invalid Input: The brake type should be either "hand brake" or "foot brake". \nNow setting it to the default "hand brake"')
            self._brake_type = "hand brake"
        else:
            self._brake_type = brake_type

#   Set number of gears
    def set_number_of_gears(self, gears):
        if not isinstance(gears, int):
            print("Invalid Input: The number of gears should be an integer")
        elif 1 <= self._current_gear <= gears <= 15:
             self._number_of_gears = gears
        else:
            print(f"Invalid Input: The number of gears ({gears}) is less than the current gear ({self._current_gear})") # it will set the previous given number of gears


#    Get number of gears
    def get_number_of_gears(self):
        print(f"The number of gears has been set to {self._number_of_gears}")

    # Set current gear
    def set_current_gear(self, gear):
        if not isinstance(gear, int):
            print(f"Invalid Input: The current gear should be an integer and values should be between 1 to the number of gears (i.e.{self._number_of_gears})")
        elif 1 <= gear <= self._number_of_gears <= 15:
            self._current_gear = gear
        else:
            print(f"Invalid Input: The current gear should be an integer and values should be between 1 to the number of gears (i.e.{self._number_of_gears})")

    # Get current gear
    def get_current_gear(self):
        print(f"The current gear has been set to {self._current_gear}")

    # set number of wheels
    def set_number_of_wheels(self, wheel):
        if not isinstance(wheel, int):
            print("Invalid Input: The number of wheels should be an integer from 1 to 4")
        else:
            self._number_of_wheels = wheel
    # Get number of wheels
    def get_number_of_wheels(self):
        print(f"The number of wheels has been set to {self._number_of_wheels}")
    # Set the brake type
    def set_brake_type(self, brake):
        if brake not in ["hand brake", "foot brake"]:
            print('Invalid Input: The brake type should be either "hand brake" or "foot brake"')
        else:
            self._brake_type = brake
    # Get brake type
    def get_brake_type(self):
        print(f"The brake type is set to {self._brake_type}")

    # Reset gear to 1
    def reset_gear(self):
        self._current_gear = 1
        print("Resetting the gear...")

    # increase gear
    def increase_gear(self):
        if self._current_gear < self._number_of_gears:
            self._current_gear += 1
            print("The gear has been increased by 1")
        else:
            print("Cannot increase: already reached maximum gears")

    # Decrease gear
    def decrease_gear(self):
        if 1 < self._current_gear:
            self._current_gear -= 1
            print("The gear has been decreased by 1")
        else:
            print("Cannot decrease: already at minimum gears")

#    String representation of the Bike object
    def __str__(self):
        return (f"Bike with {self._number_of_gears} number of gears with current gear {self._current_gear}, {self._number_of_wheels}"
                f" number of wheels with '{self._brake_type}' ")


