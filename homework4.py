#*******************************************************************************
# 1. ციკლის მეშვეობით 3 მომხმარებელს შეაყვანინე
# ინფორმაცია საკუთარი სახელის, გვარის და ასაკის
# შესახებ. თითოეული მომხმარებლის ინფორმაცია
# შეინახე ინდივიდუალურ სიაში. შემდეგ კი სამივე სია
# დაამატე საერთო ცალრიელ სიას სახელად consumer_info.
# Input_ის მეშვეობით მომხმარებლის ინდექსის შეყვანის
# შემთხვევაში პროგრამამ უნდა დაბრუნოს არჩეულ
# მომხმარებელზე ინფორმაცია შემდეგნაირად:
# Name: Elene
# Lastname: Khardava
# Age: 21
#*******************************************************************************

# i = 0
# while i < 3 :
#    name = input("enter your Name: ")
#    lastname = input("enter your Lastname: ")
#    age = input("enter your age: ")
#
#    if i == 0: person1 = [name,lastname,age]
#    elif i == 1: person2 = [name,lastname,age]
#    elif i == 2: person3 = [name,lastname,age]
#    i += 1
#
# consumer_info = []
# consumer_info.extend(person1)
# consumer_info.extend(person2)
# consumer_info.extend(person3)
#
# while True:
#    a = int(input("please enter the costumer index: "))
#    if a == 1: print(f"""Name: {consumer_info[0]}\nLastname: {consumer_info[1]}\nAge: {consumer_info[2]}""")
#    elif a == 2: print(f"""Name: {consumer_info[3]}\nLastname: {consumer_info[4]}\nAge: {consumer_info[5]}""")
#    elif a == 3: print(f"""Name: {consumer_info[6]}\nLastname: {consumer_info[7]}\nAge: {consumer_info[8]}""")
#    else: print("incorrect input!")



#*******************************************************************************
# 2. შექმენი ჩაშენებული სია, რომელშიც იქნება შენახული
# ცნობილი მსახიობების შესახებ ინფორმაცია.
# მომხმარებელს შემოჰყავს მსახიობის სახელი ან გვარი.
# თუ სიაში მოიძებნა მსახიობი, დაბეჭდe მის შესახებ
# არსებული ინფორმაცია რეზუმის სახით.
#*******************************************************************************

# actors = [
#     {"name": "Tom hanks", "age": 65, "movies": ["Forrest Gump", "Cast Away",], "awards": ["2 Oscars", "4 Golden Globes"]},
#     {"name": "Meryl streep", "age": 72, "movies": ["The Devil Wears Prada", "The Iron Lady"], "awards": ["3 Oscars", "8 Golden Globes"]},
#     {"name": "Leonardo dicaprio", "age": 46, "movies": ["Titanic", "Inception"], "awards": ["1 Oscar", "4 Golden Globes"]}
# ]
#
# # Accessing information about the actor
# actor_name = input("enter actor's Name  or Lastname: ").lower()
#
# found_actor = None
# for actor in actors:
#     if  actor_name.lower() in actor["name"].lower():
#         found_actor = actor
#         break
#
# if found_actor:
#     print("Name:", found_actor["name"])
#     print("Age:", found_actor["age"])
#     print("Movies:", found_actor["movies"])
#     print("Awards:", found_actor["awards"])
# else:
#     print("Actor not found in the list.")


#*******************************************************************************

# 3.შექმენი ფუნქცია რომელიც მიიღებს სიას და
# დააბრუნებს ასევე სიას, თუმცა უნიკალური
# ელემენტებით (გამოიყენე set მონაცემთა ტიპი).
#
# def unique_list():
# ...
# return ...
#*******************************************************************************

# def  list_function (dublicate_list):
#     unique_elements_list = list(set(dublicate_list))
#     return unique_elements_list
#
# my_list = []
# while True:
#     element =int(input("input elements: "))
#     my_list.append(element)
#     if element >30:
#         break
#
# unique_list = list_function(my_list)
# print("previous list: ", my_list)
# print("current list", unique_list)



#*******************************************************************************
# 4. შექმენი ფუნქცია რომელიც მიიღებს ორ set ტიპის
# მონაცემს, გააერთიანებს მათ, შემდეგ კი გადააქცევს
# tuple ტიპის მონაცემად და დააბრუნებს შედეგს.
#*******************************************************************************

# def combine_function (set1, set2):
#      combined_set= set1.union(set2)
#      combined_tuple = tuple(combined_set)
#      return combined_tuple
#
# set_a = {2,4,6,8,10}
# set_b = {1,3,5,7,9,11}
#
# tuple1 = combine_function(set_a,set_b)
# print("set1: ", set_a)
# print("set2: ", set_b)
# print("tuple of combined sets: ", tuple1)

#*******************************************************************************
# 5. დაწერე პროგრამა, რომელიც შეამოწმებს გადაცემული
# ლექსიკონი არის თუ არა ცარიელი.
#*******************************************************************************

# def empty_dictionary(any_dictionary):
#      a = bool(any_dictionary)
#      return a
#
# my_dict = {"kerketi":"kakali","cisferi":"mtebi","chito":"gvrito"}
# if empty_dictionary(my_dict)==True:
#      print("Dictionary in not empty")
# else: print("Dictionary is empty")


#*******************************************************************************
# 6. დაწერე პროგრამა რომელიც სტრიქონისგან ქმნის ლექსიკონს.
# დათვალე სტრიქონში კონკრეტული სიმბოლოს
# ოდენობა. მაგალითად პროგრამას გადავეცით
# სტრიქონი: &#39;w3schools&#39; უნდა დააბრუნოს ლექსიკონი:
#
# {&#39;w&#39;: 1, &#39;3&#39;: 1, ‘s&#39;: 2, ‘c&#39;: 1, ‘h&#39;: 1, &#39;o&#39;: 2, ‘l&#39;: 1}
#*******************************************************************************

# def count_symbols(any_string):
#     symbol_dictionary = {}
#     for symbol in any_string:
#         if symbol in symbol_dictionary:
#             symbol_dictionary[symbol] +=1
#         else:
#             symbol_dictionary[symbol] = 1
#     return symbol_dictionary
#
# customer_input = input("enter any string")
#
# result = count_symbols(customer_input)
# for key, value in result.items():
#     print(f""" symbol: {key} amount: {value}""")




#*******************************************************************************
# 18. მოცემულია სია:
# [“apple”, “orange”, “banana”, “strawberry”]
# მომხმარებელს შეაყვანინე სიტყვა, და თუ ეს სიტყვა
# მოიძებნა მოცემულ სიაში, ამობეჭდე მისი ინდექსი.
#*******************************************************************************

# def word_index(word, word_list):
#     if word in word_list:
#         return word_list.index(word)
#     else:
#         return "this Word not found in the list."
#
# word_list = ["apple", "orange", "banana", "strawberry"]
# user_word = input("Enter a word to search in the list: ")
# result = word_index(user_word, word_list)
# print(result)
#