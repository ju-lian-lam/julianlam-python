class Vehicle:

  # 
  def __init__(self, my_manufacturer, my_top_speed):
    self.manufacturer = my_manufacturer  # A 'private' attribute
    self.topSpeed = my_top_speed      # A 'private' attribute

  def honk_horn(self, honk_times):
    for n in range(honk_times):
      print("Beep!")

  def set_top_speed(self, new_speed):
      self.topSpeed = new_speed

  def get_top_speed(self):
      return self.topSpeed

  def get_manufacturer(self):
      return self.manufacturer

my_vehicle1 = Vehicle("Ford", 0)
my_vehicle2 = Vehicle("Tesla", 0)
fetchspeed = my_vehicle1.get_top_speed()
if (fetchspeed == 0):
    newspeed = int(input("Enter correct top speed: "))
    my_vehicle1.set_top_speed(newspeed)

print("top speed:", my_vehicle1.get_top_speed())
print("manufacturer:", my_vehicle1.get_manufacturer())
    



  

# (a) Add new methods to the Vehicle class above to:
#     - set_top_speed(self, new_speed)
#     - get_top_speed(self)
#     - get_manufacturer(self)

# (b) Write Python statements below to instantiate two new Vehicle objects,
# my_vehicle1 and my_vehicle2.
# my_vehicle1 is a "Ford" with topSpeed 0.
# my_vehicle2 is a "Tesla" with topSpeed 0.


# (c) Write Python statements below which will check the top speed
# of my_vehicle1 using its getter method.
# If the top speed is 0:
#   1. Ask the user to enter its correct top speed (using input()).
#   2. Convert the input to an integer.
#   3. Use the setter method to update the attribute.
# Finally, print the manufacturer and top speed of the vehicle using
# the getter methods.
