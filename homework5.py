#*****************************************************************************
# 1. შექმენი ტრანსპორტის კლასი მინიმუმ 4 კლასის პარამეტრით
#*****************************************************************************

class Transporti:
        mode = "Car"
        capacity = 5
        speed = 180
        fuel_type = "Gasoline"

transport1 = Transporti

print(transport1.mode)
print(transport1.capacity)
print(transport1.speed)
print(transport1.fuel_type)

#*****************************************************************************
# 2. დაამატე ერთი სტატიკური მეთოდი.
#*****************************************************************************

# class Transporti:
#     def __init__(self, mode, capacity, speed, fuel_type):
#         self.mode = mode
#         self.capacity = capacity
#         self.speed = speed
#         self.fuel_type = fuel_type
#
#     def information(self):
#         print(f"Mode of transport: {self.mode}")
#         print(f"Capacity: {self.capacity}")
#         print(f"Speed: {self.speed} km/h")
#         print(f"Fuel_type: {self.fuel_type}")
#
#     @staticmethod
#     def thanks():
#         return print("thanks for your information")
#
# transport1 = Transporti("Car", 5, 180, "Gasoline")
#
# transport1.information()
#
# print(Transporti.thanks())


#*****************************************************************************
# 3. დაამატე ორი კლასის მეთოდი.
#*****************************************************************************

# class Calculator:
#     @classmethod
#     def add(cls,x,y):
#         return x+y
#
#     @classmethod
#     def multiply(cls,x,y):
#         return x*y
#
# sum_result = Calculator.add(12,27)
# multiply_result = Calculator.multiply(20,5)
#
# print("sum of x and y = ", sum_result)
# print("multiplication of  x and y = ", multiply_result)

#*****************************************************************************
# 4. დაამატე __init__ magic მეთოდი და მინიმუმ 3 ობიექტის პარამეტრი.
#*****************************************************************************

# class Gadget:
#     def __init__(self, brand, name, model):
#         self.brand = brand
#         self.name = name
#         self.model = model
#
# gad = Gadget("samsung", "android", "Galaxy")
#
# print("Gadget brand: ", gad.brand)
# print("Gadget name: ", gad.name)
# print("Gadget model: ", gad.model)

#*****************************************************************************
# 5. დაამატე მინიმუმ 2, ობიექტის მეთოდი.
#*****************************************************************************

# class Animal:
#     def __init__(self, species, name, age):
#         self.species = species
#         self.name = name
#         self.age = age
#
#     def information(self):
#         return f"species: {self.species}  name: {self.name}   Age: {self.age}"
#
#     def Sound_of_animal(self, sound):
#         return f"{self.name} {sound}s"
#
# lion=Animal("lion", "simba", 6)
# elephant = Animal("elephant", "Dumbo", 10)
#
# print(lion.information())
# print(lion.Sound_of_animal("roar"))
# print(elephant.information())
# print(elephant.Sound_of_animal("trumpet"))


#*****************************************************************************
# 6. დაამატე __repr__ magic მეთოდი
#*****************************************************************************

# class Bird:
#     def __init__(self, species, name, color):
#         self.species = species
#         self.name = name
#         self.color = color
#
#     def __repr__(self):
#         return f"The {self.species} called {self.name} is {self.color}"
#
# parrot =  Bird("parrot", "Chico", "green and yellow")
#
# print(repr(parrot))

#*****************************************************************************
# 7. ზემოხსენებული კლასისგან შექმენი მინიმუმ 5 ობიექტი და
# გამოიძახე მისი ზოგიერთი მეთოდი და პარამეტრი.
#*****************************************************************************

# class City:
#     def __init__(self, name, population, country):
#         self.name = name
#         self.population = population
#         self.country = country
#
#     def information(self):
#         return f"the city called {self.name} is in {self.country} and  has a population of {self.population} people."
#
#     def is_metropolitan(self, threshold):
#         return self.population >= threshold
#
# # Creating objects of the City class
# new_york = City("New York", 8530000, "USA")
# tokyo = City("Tokyo", 9270000, "Japan")
# london = City("London", 8982000, "United Kingdom")
# paris = City("Paris", 2141000, "France")
# beijing = City("Beijing", 21540000, "China")
#
# # Calling methods and parameters of the City objects
# print(new_york.information())
# print(f"Is Tokyo a metropolitan city? {tokyo.is_metropolitan(9000000)}")
# print(london.country)
# print(paris.population)







