# ******************************************************************************************
# 1. შექმენი ქვეყნის აბსტრაქტული კლასი. რომელსაც
# ექნება მინიმუმ სამი აბსტრაქტული მეთოდი.
# *******************************************************************************************


# from abc import ABC, abstractmethod
#
# class Country(ABC):
#     def __init__(self,name):
#         self.name = name
#
#     @abstractmethod
#     def capital(self):
#         pass
#
#     @abstractmethod
#     def population(self):
#         pass
#
#     @abstractmethod
#     def language(self):
#         pass
#
# class Germany(Country):
#     def capital(self):
#         return 'Berlin'
#
#     def population(self):
#         return  83000000
#
#     def language(self):
#         return 'German'
#
# germany = Germany("Germany")
#
# print(germany.capital())
# print(germany.population())
# print(germany.language())



# ******************************************************************************************
# 2. შექმენი მისგან საქართველოს კლასი, რომელსაც ექნება
# public, protected და private ცვლადები (მაგალითად
# ბიუჯეტი, მოსახლეობა და ა.შ.).
# ******************************************************************************************
#
# from abc import ABC, abstractmethod
#
# class Georgia(ABC):
#     def __init__(self,budget, population, religion):
#         self.budget = budget                 #public
#         self._population = population        #protected
#         self.__religion = religion           #private
#
#     @abstractmethod
#     def print_religion(self):
#         pass
#
#
# class ConcreteGeorgia(Georgia):
#     def print_religion(self):
#         return self.__religion
#
# georgia = ConcreteGeorgia(1000000000, 5000000, "orthodox")
# print(georgia.budget)
# print(georgia._population)
# print(georgia.print_religion())



# ******************************************************************************************
#შექმენი საქართველოს ობიექტი და გამოიყენე
#ზემოხსენებული მეთოდები.
# ******************************************************************************************


# from abc import ABC, abstractmethod
#
# class Country(ABC):
#
#     @abstractmethod
#     def capital(self):
#         pass
#
#     @abstractmethod
#     def population(self):
#         pass
#
#     @abstractmethod
#     def language(self):
#         pass
#
#
# class Georgia(Country):
#     def __init__(self,thecapital, population, language):
#         self._capital = thecapital                #public
#         self._population = population         #protected
#         self.__language = language            #private
#
#     def capital(self):
#         return self._capital
#
#     def population(self):
#         return  self._population
#
#     def language(self):
#         return self.__language
#
# georgia = Georgia("Tbilisi",5000000 ,"Georgian")
#
# print(georgia.capital())
# print(georgia.population())
# print(georgia.language())
