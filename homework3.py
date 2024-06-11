#*******************************************************************************************
# 1. შექმენი ფუნქცია, რომელიც მომხმარებლისგან მიღებულ ინფორმაციას გაასამმაგებს
# და დაბეჭდავს შემდეგნაირად:
# input: “word”
# Output: „Tripled: wordwordword“
#*******************************************************************************************


# def simplefunc(x):
#     result = x+x+x
#     return result
#
# print(simplefunc(input()))



#*******************************************************************************************
# 2. შექმენი ფუნქცია, რომელიც მიიღებს მომხმარებლის წონას და დააბრუნებს მის წონას
# მთვარეზე. (მთვარის გრავიტაცია 6_ჯერ ნაკლებია დედამიწისაზე)
#*******************************************************************************************


# print("\n\nHello, our digital program offers you \n to calculate  your weight  on the moon\n"
#     "please, pass your  name and weight: ")
# name = input("Name: ")
# if name != "":
#     pass
# else:
#     print("Name has invalid input!  try again!")
#
# try:
#     weight = int(input("Weight: "))
# except:
#     print("weight has invalid input!  try again!")
# def calculator(x):
#     moon_weight = x/6
#     return moon_weight
#
# print(f"""\nyour weight on the moon is: [{calculator(weight)}]""")



#*******************************************************************************************
# 3. შექმენი კალკულატორის ფუნქცია, რომელიც მიიღებს გამოსახულებას
# მომხმარებლისგან input() ფუნქციის დახმარებით (სამ მონაცემს _ პირველ რიცხვს,
# მოქმედებას (+ - * / ^), მეორე რიცხვს)
# მაგ. „2 * 6“ დათვლის და დააბრუნებს შედეგს. გაითვალისწინე რომ რიცხვის შეყვანის
# მაგიერ სიმბოლოების შეყვანის შემთხვევაში უნდა დააბრუნოს ფუნქციამ შესაბამისი
# მესიჯი. ასევე ნულზე გაყოფა არ შეიძ₾ება, ამ შემთხვევაშიც უნდა დააბრუნოს
# შესაბამისი მესიჯი. (დააბრუნოს და არა დაპრინტოს)
#*******************************************************************************************

# try:
#     m = int(input("Enter first number: "))
#     k = input("Enter equation symbol: ")
#     n = int(input("Enter second number: "))
#
#     if k == "/" and n == 0:
#        print("its not allowed to divide by zero! ")
# except:
#     a = "invalid input!  try again!"
#     print(a)
#
# def   calculator(x, y, z):
#       if y == '+':
#         result = x+z
#       elif y == '-':
#         result = x-z
#       elif y == '*':
#         result = x*z
#       elif y == '/':
#         result = x/z
#       elif y == '**':
#         result = x**z
#       return result
#       print(result)
#
# print("result is: ", calculator(m,k,n))












