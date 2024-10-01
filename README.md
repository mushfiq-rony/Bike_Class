# **Bike Class**

## **Properties**
- **Number of Gears (1 - 15)**: 
  - The bike can have between 1 to 15 gears.
  
- **Current Gear (default: 1)**: 
  - This indicates the gear the bike is currently in, defaulting to 1.
  
- **Number of Wheels (1, 2, 3, or 4)**: 
  - The bike can have 1 to 4 wheels.
  
- **Brake Type ("hand brakes" or "foot brakes")**: 
  - Specifies the type of brakes used on the bike.

## **Methods**
- **Set & Get Number of Gears**
    - `set_number_of_gears(gears)`: Sets the number of gears.
    - `get_number_of_gears()`: Returns the number of gears.
  
- **Set & Get Current Gear**
    - `set_current_gear(gear)`: Sets the current gear.
    - `get_current_gear()`: Returns the current gear.
  
- **Set & Get Number of Wheels**
    - `set_number_of_wheels(wheels)`: Sets the number of wheels.
    - `get_number_of_wheels()`: Returns the number of wheels.
  
- **Set & Get Brake Type**
    - `set_brake_type(brake_type)`: Sets the type of brakes.
    - `get_brake_type()`: Returns the brake type.
  
- **Reset Gears**: 
    - `reset_gears()`: Sets the current gear back to 1.
  
- **Increase Gear**: 
    - `increase_gear()`: Increases the current gear by 1, ensuring it does not exceed the number of gears.
  
- **Decrease Gear**: 
    - `decrease_gear()`: Decreases the current gear by 1, ensuring it does not go below 1.

## **Usage Example**
- To create an instance of the bike, set the number of gears, increase the gear, and check the current gear.
