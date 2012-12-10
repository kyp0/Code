cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# There are 100 cars
print "There are", cars, "cars available."
# There are 30 drivers
print "There are only", drivers, "drivers available."
# There are (100-70) 70 empty cars
print "There will be", cars_not_driven, "empty cars today."
# We can transport (30 * 4) 120 people ttoday
print "We can transport", carpool_capacity, "people today."
# We have 90 to carpool today
print "We have", passengers, "to carpool today."
# We need to put about (90/30) 3 in each car
print "We need to put about", average_passengers_per_car, "in each car."